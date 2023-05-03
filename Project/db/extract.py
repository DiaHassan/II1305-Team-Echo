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
    return result


# X-axis: counties
# Y-axis: number of ads in variable profession
def get_counties_for_profession(sources, counties, profession):
    result = []
    sourcestr = []
    countystr = []
    for i in sources:
        sourcestr.append("'" + i + "'")
    for i in counties:
        countystr.append("'" + i + "'")
    sourcestr = ",".join(sourcestr)
    countystr = ",".join(countystr)
    query = 'SELECT county, source, COUNT(*) \
            FROM job_listing j \
            JOIN job p ON j.job_id = p.id \
            WHERE p.profession LIKE "%' + profession + '%" \
            AND j.county IN (' + countystr + ') \
            AND j.source IN (' + sourcestr + ')\
                GROUP BY county, source'
    fetch = list_of_tuples_to_2d_list(send_query(query))
    result = outer_format(fetch)
    return result


# X-axis: all counties
# Y-axis: variable param of ads in variable profession
def get_counties_for_profession_with_param(sources, counties, profession, param):
    result = []
    sourcestr = []
    countystr = []
    for i in sources:
        sourcestr.append("'" + i + "'")
    for i in counties:
        countystr.append("'" + i + "'")
    sourcestr = ",".join(sourcestr)
    countystr = ",".join(countystr)
    if param == "requirement":
        query = 'SELECT county, source, requirement, COUNT(jl.id) FROM job_listing AS jl \
                 INNER JOIN (requirement_relation AS rr \
                    INNER JOIN requirement AS r ON rr.requirement_id = r.id) \
                      ON jl.id = rr.job_listing_id \
                WHERE job_id IN (SELECT id FROM job WHERE profession LIKE "%' + profession  + '%") \
                AND jl.county IN (' + countystr + ') AND jl.source IN (' + sourcestr + ') \
                GROUP BY county, source, requirement ORDER BY jl.job_id'
    else:
        query = 'SELECT county,source, j.' + param + ', COUNT(*) \
                FROM job_listing j \
                JOIN job p ON j.job_id = p.id \
                WHERE p.profession LIKE "%' + profession + '%" \
                AND j.' + param + ' IS NOT + "null"\
                AND j.county IN (' + countystr + ') \
                AND j.source IN (' + sourcestr + ') \
                GROUP BY county, source, j.' + param
    fetch = list_of_tuples_to_2d_list(send_query(query))
    result = outer_format(fetch)
    #outer_list.append(outer_format(fetch))

    #result = merge_list(result)
    return result

 #Takes [[County, source, param(Optional), nr] ... ]
 #Returns[ [Xaxis-value 1, [scr1, [param(optional), nr], ..., [param(optional), nr]]], ... ]
def outer_format(list):
    if not list:
        return []
    brist = format(list)
    result = []
    for i in brist:
        r = format(i[1:])
        r.insert(0, i[0])
        result.append(r)
    return result
        
#Takes [[X, param(optional), nr] ... ]
#Returns [[x, [param, nr], ...], ...]
def format(list):
    r = []
    sourceList = []
    src = None
    for i in list:
        if i[0] == src:
            sourceList.append(i[1:])
        else:
            if sourceList:
                r.append(sourceList)
            src = i[0]
            sourceList = [src, i[1:]]
    r.append(sourceList)
    return r
        

# ---------------------------------------- COUNTY QUERIES -------------------------------------------------

# X-axis: all professions without param
# Y-axis: number of professions in variable county
def get_professions_for_county(sources, county, professions): 
    result = []
    sourcestr = []
    professionstr = []
    for i in sources:
        sourcestr.append("'" + i + "'")
    for i in professions:
        professionstr.append("'" + i + "'")
    sourcestr = ",".join(sourcestr)
    professionstr = ",".join(professionstr)
    query = 'SELECT profession, source, county, COUNT(job_listing.id) \
             FROM job_listing INNER JOIN job ON job.id = job_listing.job_id \
             WHERE job_listing.county = "' + county + '" \
             AND job_listing.source IN (' + sourcestr + ') \
             AND profession IN (' + professionstr + ')\
             GROUP BY source, county' 
    fetch = list_of_tuples_to_2d_list(send_query(query))
    result = outer_format(fetch)
    return result


# X-axis: all professions and param
# Y-axis: number of professions in variable county
def get_professions_for_county_with_param(sources, county, professions, param): 
    result = []
    sourcestr = []
    professionstr = []
    for i in sources:
        sourcestr.append("'" + i + "'")
    for i in professions:
        professionstr.append("'" + i + "'")
    sourcestr = ",".join(sourcestr)
    professionstr = ",".join(professionstr)
    if param == "requirement":
        query = 'SELECT profession, source, requirement, COUNT(jl.id) FROM job_listing AS jl \
                 INNER JOIN (requirement_relation AS rr \
                    INNER JOIN requirement AS r ON rr.requirement_id = r.id) \
                      ON jl.id = rr.job_listing_id \
                WHERE job_id IN (SELECT id FROM job WHERE profession IN (' + professionstr  + ') \
                AND jl.county = "' + county + '" AND jl.source IN (' + sourcestr + ') \
                GROUP BY profession, source, requirement ORDER BY jl.job_id'
    else:
        query = 'SELECT profession, source,' + param + ', COUNT(job_listing.id) as "sum" \
            FROM job_listing INNER JOIN job ON job.id = job_listing.job_id \
            WHERE job_listing.county = "' + county + '" \
            AND job_listing.source IN (' + sourcestr + ') \
            AND profession IN (' + professionstr + ')\
            AND ' + param + ' IS NOT "null" \
            GROUP BY profession, source, job_listing.' + param 
    fetch = list_of_tuples_to_2d_list(send_query(query))
    result = outer_format(fetch)
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
    #print(extract(['platsbanken'], 'Stockholms län', ['Städare', 'Lärare'], 'employment_type'))
    
    # One profession, many counties
    print(get_counties_for_profession(['platsbanken'], ['Stockholms län', 'Uppsala län'], 'Städare'))
    #print(get_counties_for_profession_with_param(['platsbanken'], ['Stockholms län', 'Uppsala län'], 'Lärare', 'requirement'))

    # One county many professions
    #print(get_professions_for_county(['platsbanken'], 'Stockholms län', ['Städare', 'Lärare']))
    #print(get_professions_for_county_with_param(['platsbanken'], 'Stockholms län', ['Städare', 'Lärare'], 'employment_type'))
