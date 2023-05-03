import sqlite3
from countyprof import profession_list
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


# [[(a,b)], [(c,d)]] --> [[a,b], [c,d]]
def list_of_list_tuple_to_2d_list(list_of_list_tuple):
    result = []
    for list_tuple in list_of_list_tuple:
       result.append(list(list_tuple.pop()))  
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
    for item in list:
        result.append([item[1], item[2]])
    return result

# ---------------------------------------------- PROFESSION QUERIES ----------------------------------------

# Connects to database and sends query
def send_query(query):
    with sqlite3.connect(db_path) as conn:
      cursor = conn.cursor()
      result = cursor.execute(query).fetchall()
      cursor.close()
    conn.close()
    result = list_of_tuples_to_2d_list(result)
    return result


# X-axis: all counties
# Y-axis: number of ads in variable profession 
def get_profession_in_counties(profession):
    query = 'SELECT jl.county, COUNT(j.id) as job_count \
            FROM job_listing jl \
            LEFT JOIN job j ON jl.job_id = j.id AND j.profession LIKE "%' + profession + '%" \
            WHERE county IS NOT "null" \
            GROUP BY jl.county'
    result = send_query(query)
    result.insert(0, profession)
    return result


# X-axis: all counties
# Y-axis: variable param of ads in variable profession
def get_param_per_county(profession, param): 
    query = 'SELECT j.county, j.' + param + ', COUNT(*) as count \
            FROM job_listing j \
            JOIN job p ON j.job_id = p.id \
            WHERE p.profession LIKE "%' + profession + '%" AND ' + param + ' IS NOT + "null"\
            GROUP BY j.county, j.' + param
    result = send_query(query)
    result = merge_list(result)
    result.insert(0, (profession, param))
    return result


# ---------------------------------------- COUNTY QUERIES -------------------------------------------------

# X-axis: all professions without param
# Y-axis: number of professions in variable county
def get_professions_in_county(sources, county, professions): 
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        result = []
        for profession in professions:
            list = [profession]
            for source in sources:
                query = 'SELECT source, COUNT(job_listing.id) as "sum" \
                        FROM job_listing INNER JOIN job ON job.id = job_listing.job_id \
                        WHERE job_listing.county = "' + county + '" \
                        AND job_listing.source = "' + source + '" \
                        AND profession LIKE "%' + profession + '%"' 
                fetch = cursor.execute(query).fetchall()
                if not fetch: return fetch
                fetch = list_of_tuples_to_2d_list(fetch)
                pop = fetch.pop()
                fetch = [pop[0], pop[1]]
                list.append(fetch)
                result.append(list)
        cursor.close()
    conn.close()
    return result


# X-axis: all professions and param
# Y-axis: number of professions in variable county
def get_professions_in_county_with_param(sources, county, professions, param): 
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
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
                fetch = cursor.execute(query).fetchall()
                if not fetch: return fetch
                fetch = list_of_tuples_to_2d_list(fetch)
                fetch = merge_data(fetch)
                list.append(fetch)
                result.append(list)
        cursor.close()
    conn.close()
    return result


# Callee
def extract(source, county, professions, param):
    return get_professions_in_county_with_param(source, county, professions, param)


# Test
if __name__ == '__main__':
    #print(get_profession_in_counties('Städare'))
    #print(get_param_per_county('Läkare', 'duration'))
    print(get_professions_in_county(['platsbanken'], 'Stockholms län', ['Städare', 'Lärare']))
    #print(get_professions_in_county_with_param(['platsbanken'], 'Stockholms län', ['Städare', 'Lärare'], 'employment_type'))
