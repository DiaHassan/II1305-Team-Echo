from sqlite3 import connect
from sys import platform

def find_db_path():
    match platform:
        case "linux":
            return "Project/db/echo.db"
        case "darwin":
            return "Project/db/echo.db"
        case _:
            return "Project\db\echo.db"
db_path = find_db_path()

# ------------------------------------------- HELPERS -------------------------------------------------------

# [(a,b), (c,d)] --> [[a,b], [c,d]]
def list_of_tuples_to_2d_list(list_of_tuples):
    result = []
    for t in list_of_tuples:
       result.append(list(t)) 
    return result        


# Takes [[County, source, param(Optional), nr] ... ]
# Returns [[Xaxis-value 1, [scr1, [param(optional), nr], ..., [param(optional), nr]]], ... ]
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


# [[X, param(optional), nr] ... ] --> [[x, [param, nr], ...], ...]
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


# Connects to database and sends query
def send_query(query):
    with connect(db_path) as conn:
      cursor = conn.cursor()
      result = cursor.execute(query).fetchall()
      cursor.close()
    conn.close()
    return result
        
# ---------------------------------------------- PROFESSION QUERIES ----------------------------------------

# X-axis: given counties
# Y-axis: count of ads satisfy param for profession
def get_counties_for_profession(sources, counties, profession, param):
    result = []
    sources_str = []
    counties_str = []
    for c in sources:
        sources_str.append("'" + c + "'")
    for c in counties:
        counties_str.append("'" + c + "'")
    sources_str = ",".join(sources_str)
    counties_str = ",".join(counties_str)
    if param == 'null':
        query ='SELECT county, source, COUNT(*) \
                FROM job_listing j \
                JOIN job p ON j.job_id = p.id \
                WHERE p.profession LIKE "%' + profession + '%" \
                AND j.county IN (' + counties_str + ') \
                AND j.source IN (' + sources_str + ')\
                GROUP BY county, source \
                ORDER BY county, source'
    elif param == "requirement":
        query ='SELECT county, source, requirement, COUNT(jl.id) FROM job_listing AS jl \
                 INNER JOIN (requirement_relation AS rr \
                    INNER JOIN requirement AS r ON rr.requirement_id = r.id) \
                    ON jl.id = rr.job_listing_id \
                WHERE job_id IN (SELECT id FROM job WHERE profession LIKE "%' + profession  + '%") \
                AND jl.county IN (' + counties_str + ') AND jl.source IN (' + sources_str + ') \
                GROUP BY county, source, requirement \
                ORDER BY county, source'
    else:
        query ='SELECT county,source, j.' + param + ', COUNT(*) \
                FROM job_listing j \
                JOIN job p ON j.job_id = p.id \
                WHERE p.profession LIKE "%' + profession + '%" \
                AND j.' + param + ' IS NOT + "null"\
                AND j.county IN (' + counties_str + ') \
                AND j.source IN (' + sources_str + ') \
                GROUP BY county, source, j.' + param + '\
                ORDER BY county, source'
    fetch = list_of_tuples_to_2d_list(send_query(query))
    result = outer_format(fetch)
    return result

# ---------------------------------------- COUNTY QUERIES -------------------------------------------------

# X-axis: given professions 
# Y-axis: count of ads satisfying param in county
def get_professions_for_county(sources, county, professions, param): 
    result = []
    sources_str = []
    professions_str = []
    for c in sources:
        sources_str.append("'" + c + "'")
    for c in professions:
        professions_str.append("'" + c + "'")
    sources_str = ",".join(sources_str)
    professions_str = ",".join(professions_str)
    if param == 'null':
        query = 'SELECT profession, source, COUNT(job_listing.id) \
                FROM job_listing INNER JOIN job ON job.id = job_listing.job_id \
                WHERE job_listing.county = "' + county + '" \
                AND job_listing.source IN (' + sources_str + ') \
                AND profession IN (' + professions_str + ')\
                GROUP BY source, county, profession \
                ORDER BY profession, source'
    elif param == "requirement":
        query ='SELECT profession, source, requirement, COUNT(jl.id) FROM job_listing AS jl \
                INNER JOIN (requirement_relation AS rr \
                    INNER JOIN requirement AS r ON rr.requirement_id = r.id) \
                    ON jl.id = rr.job_listing_id \
                WHERE job_id IN (SELECT id FROM job WHERE profession IN (' + professions_str  + ') \
                AND jl.county = "' + county + '" AND jl.source IN (' + sources_str + ') \
                GROUP BY profession, source, requirement \
                ORDER BY profession, source'
    else:
        query ='SELECT profession, source,' + param + ', COUNT(job_listing.id) as "sum" \
                FROM job_listing INNER JOIN job ON job.id = job_listing.job_id \
                WHERE job_listing.county = "' + county + '" \
                AND job_listing.source IN (' + sources_str + ') \
                AND profession IN (' + professions_str + ')\
                AND ' + param + ' IS NOT "null" \
                GROUP BY profession, source, job_listing.' + param + ' \
                ORDER BY profession, source'
    fetch = list_of_tuples_to_2d_list(send_query(query))
    result = outer_format(fetch)
    return result

# -------------------------------- EXTRACT -------------------------------------------

# Callee
def extract(source, county, profession, param):
    # One profession, many counties
    if isinstance(county, list):
        return get_counties_for_profession(source, county, profession, param)
    # One county, many professions
    elif isinstance(profession, list):
        return get_professions_for_county(source, county, profession, param)


# Test
if __name__ == '__main__':
    print()

    # Extract
    print(extract(['Linkedin', 'ledigajobb'], 'Blekinge län', ['Utvecklare', 'Läkare', 'Sjuksköterska', 'Lärare'], 'employment_type'))
    
    # One profession, many counties
    #print(get_counties_for_profession(['platsbanken'], ['Stockholms län', 'Uppsala län'], 'Städare', 'null'))

    # One county many professions
    #print(get_professions_for_county(['platsbanken'], 'Stockholms län', ['Städare', 'Lärare'], 'employment_type'))
