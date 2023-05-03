import sqlite3
from sys import platform


def find_db_path(platform):
    match platform:
        case "linux":
            return "Project/db/echo.db"
        case "darwin":
            return "Project/db/echo.db"
        case _:
            return "Project\db\echo.db"

db_path = find_db_path(platform)

# ------------------------------------------- HELPERS -------------------------------------------------------

# [(a,b), (c,d)] --> [[a,b], [c,d]]
def list_of_tuples_to_2d_list(list_of_tuples):
    result = []
    for t in list_of_tuples:
       result.append(list(t)) 
    return result        


# Merges list with key-value
# [[a, x], [b, y], [b,z]] --> [[a, x], [b, [y,z]]]
def merge_list(lst):
    # Group the elements by their first value
    groups = {}
    for elem in lst:
        key = elem[0]
        if key not in groups:
            groups[key] = []
        groups[key].append(elem[1:])

    # Combine the second and third values of each group into a list
    result = []
    for key, values in groups.items():
        combined = [key]
        for i in range(len(values[0])):
            combined.append([v[i] for v in values])
        result.append(combined)

    return result


#[[a, b, c], [a, d, e]] --> [a, [[b,c], [d,e]]]
def merge_data(list):
    key = list[0][0]
    result = [key]
    brisk = []
    for item in list:
        brisk.append([item[1], item[2]])
    result.append(brisk)
    return result
        

# ---------------------------------------------- PROFESSION QUERIES ----------------------------------------

# Connects to database and sends query
def send_query(query):
    with sqlite3.connect(db_path) as conn:
      cursor = conn.cursor()
      result = cursor.execute(query).fetchall()
      cursor.close()
    conn.close()
    return result


# X-axis: counties
# Y-axis: number of ads in variable profession 
def get_counties_for_profession(sources, counties, profession):
    result = []
    for county in counties:
        outer_list = [county]
        for source in sources: 
            inner_list = [source]
            query = 'SELECT COUNT(*) \
                    FROM job_listing j \
                    JOIN job p ON j.job_id = p.id \
                    WHERE p.profession LIKE "%' + profession + '%" \
                    AND j.county == "' + county + '" \
                    AND j.source == "' + source + '"'
            fetch = send_query(query)
            pop = fetch[0]
            fetch = [pop[0]]
            inner_list.append(fetch)
            outer_list.append(inner_list)
        result.append(outer_list)
    result = merge_list(result)
    return result


# X-axis: all counties
# Y-axis: variable param of ads in variable profession
def get_counties_for_profession_with_param(sources, counties, profession, param):
    result = []
    for county in counties:
        outer_list = [county]
        for source in sources: 
            inner_list = [source]
            if param == "requirement":
                query = 'SELECT requirement, COUNT(jl.id) FROM job_listing AS jl \
                         INNER JOIN (requirement_relation AS rr \
                            INNER JOIN requirement AS r ON rr.requirement_id = r.id) \
                              ON jl.id = rr.job_listing_id \
                        WHERE job_id IN (SELECT id FROM job WHERE profession LIKE "%' + profession  + '%") \
                        AND jl.county = "' + county + '" AND jl.source = "' + source + '" \
                        GROUP BY requirement ORDER BY jl.job_id'
            else:
                query = 'SELECT j.' + param + ', COUNT(*) \
                        FROM job_listing j \
                        JOIN job p ON j.job_id = p.id \
                        WHERE p.profession LIKE "%' + profession + '%" \
                        AND j.' + param + ' IS NOT + "null"\
                        AND j.county == "' + county + '" \
                        AND j.source == "' + source + '" \
                        GROUP BY j.' + param
            fetch = list_of_tuples_to_2d_list(send_query(query))
            inner_list.append(fetch)
            outer_list.append(inner_list)
        result.append(outer_list)
    result = merge_list(result)
    return result


# ---------------------------------------- COUNTY QUERIES -------------------------------------------------

# X-axis: all professions without param
# Y-axis: number of professions in variable county
def get_professions_for_county(sources, county, professions): 
    result = []
    for profession in professions:
        list = [profession]
        for source in sources:
            query = 'SELECT source, COUNT(job_listing.id) as "sum" \
                    FROM job_listing INNER JOIN job ON job.id = job_listing.job_id \
                    WHERE job_listing.county = "' + county + '" \
                    AND job_listing.source = "' + source + '" \
                    AND profession LIKE "%' + profession + '%"' 
            fetch = send_query(query)
            if not fetch: return fetch
            fetch = list_of_tuples_to_2d_list(fetch)
            pop = fetch.pop()
            fetch = [pop[0], [pop[1]]]
            list.append(fetch)
            result.append(list)
    return result


# X-axis: all professions and param
# Y-axis: number of professions in variable county
def get_professions_for_county_with_param(sources, county, professions, param): 
    result = []
    for profession in professions:
        list = [profession]
        for source in sources:
            if param == "requirement":
                query = 'SELECT source, requirement, COUNT(jl.id) FROM job_listing AS jl \
                         INNER JOIN (requirement_relation AS rr \
                            INNER JOIN requirement AS r ON rr.requirement_id = r.id) \
                              ON jl.id = rr.job_listing_id \
                        WHERE job_id IN (SELECT id FROM job WHERE profession LIKE "%' + profession  + '%") \
                        AND jl.county = "' + county + '" AND jl.source = "' + source + '" \
                        GROUP BY requirement ORDER BY jl.job_id'
            else:
                query = 'SELECT source,' + param + ', COUNT(job_listing.id) as "sum" \
                    FROM job_listing INNER JOIN job ON job.id = job_listing.job_id \
                    WHERE job_listing.county = "' + county + '" \
                    AND job_listing.source = "' + source + '" \
                    AND profession LIKE "%' + profession + '%"\
                    AND ' + param + ' IS NOT "null" \
                    GROUP BY job_listing.' + param 
            fetch = send_query(query)
            if not fetch: return fetch
            fetch = list_of_tuples_to_2d_list(fetch)
            fetch = merge_data(fetch)
            list.append(fetch)
            result.append(list)
    return result


# -------------------------------- EXTRACT -------------------------------------------
# Callee
def extract(source, county, profession, param):
    # One profession, many counties
    if isinstance(county, list):
        if param == 'null':
            return get_counties_for_profession(source, county, profession)
        return get_counties_for_profession_with_param(source, county, profession, param)
    # One county, many professions
    elif isinstance(profession, list):
        if param == 'null':
            return get_professions_for_county(source, county, profession)
        return get_professions_for_county_with_param(source, county, profession, param)


# Test
if __name__ == '__main__':

    # Extract
    print(extract(['platsbanken'], 'Stockholms län', ['Städare', 'Lärare'], 'employment_type'))
    
    # One profession, many counties
    #print(get_counties_for_profession(['platsbanken'], ['Stockholms län', 'Uppsala län'], 'Städare'))
    #print(get_counties_for_profession_with_param(['platsbanken'], ['Stockholms län', 'Uppsala län'], 'Städare', 'requirement'))

    # One county many professions
    #print(get_professions_for_county(['platsbanken'], 'Stockholms län', ['Städare', 'Lärare']))
    #print(get_professions_for_county_with_param(['platsbanken'], 'Stockholms län', ['Städare', 'Lärare'], 'employment_type'))
