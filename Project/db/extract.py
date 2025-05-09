from sqlite3 import connect

# Sometimes path error
# db_path = 'Project/db/echo.db'
db_path = 'db/echo.db'

# ------------------------------------------- HELPERS -------------------------------------------------------

# ['a', 'b', 'c'] -> 'a, b, c'
def list_to_string(list:list) -> str:
    result = []
    for c in list:
        result.append("'" + c + "'")
    return ",".join(result)


# [(a,b), (c,d)] --> [[a,b], [c,d]]
def list_of_tuples_to_2d_list(list_of_tuples:list) -> list:
    result = []
    for t in list_of_tuples:
       result.append(list(t)) 
    return result        


# Takes [[County, source, param(Optional), nr] ... ]
# Returns [[Xaxis-value 1, [scr1, [param(optional), nr], ..., [param(optional), nr]]], ... ]
def outer_format(list:list) -> list:
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
def format(list:list) -> list:
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
def send_query(query:str) -> list:
    with connect(db_path) as conn:
      cursor = conn.cursor()
      result = cursor.execute(query).fetchall()
      cursor.close()
    conn.close()
    return result
      
# ---------------------------------------------- PROFESSION QUERIES ----------------------------------------

# X-axis: given counties
# Y-axis: count of ads satisfy param for profession
def get_counties_for_profession(sources:list, counties:list, profession:str, param:str, date:str) -> list:
    result = []
    sources_str = list_to_string(sources)
    counties_str = list_to_string(counties)
    if param == 'null':
        query = f'SELECT county, source, COUNT(*) \
                FROM job_listing j \
                JOIN job p ON j.job_id = p.id \
                WHERE p.profession = "{profession}" \
                AND j.county IN ({counties_str}) \
                AND j.source IN ({sources_str})\
                AND strftime("%Y-%m", j.date_gathered) = "{date}" \
                GROUP BY county, source \
                ORDER BY county, source'
    elif param == "requirement":
        query = f'SELECT county, source, requirement, COUNT(jl.id) FROM job_listing AS jl \
                 INNER JOIN (requirement_relation AS rr \
                    INNER JOIN requirement AS r ON rr.requirement_id = r.id) \
                    ON jl.id = rr.job_listing_id \
                WHERE job_id IN (SELECT id FROM job WHERE profession = "{profession}") \
                AND jl.county IN ({counties_str}) AND jl.source IN ({sources_str}) \
                AND strftime("%Y-%m", jl.date_gathered) = "{date}" \
                GROUP BY county, source, requirement \
                ORDER BY county, source'
    else:
        query = f'SELECT county,source, j.{param}, COUNT(*) \
                FROM job_listing j \
                JOIN job p ON j.job_id = p.id \
                WHERE p.profession = "{profession}" \
                AND j.county IN ({counties_str}) \
                AND j.source IN ({sources_str}) \
                AND strftime("%Y-%m", j.date_gathered) = "{date}" \
                GROUP BY county, source, j.{param} \
                ORDER BY county, source'
    fetch = list_of_tuples_to_2d_list(send_query(query))
    result = outer_format(fetch)
    return result

# ---------------------------------------- COUNTY QUERIES -------------------------------------------------

# X-axis: given professions 
# Y-axis: count of ads satisfying param in county
def get_professions_for_county(sources:list, county:str, professions:list, param:str, date:str) -> list: 
    result = []
    sources_str = list_to_string(sources)
    professions_str = list_to_string(professions)
    if param == 'null':
        query = f'SELECT profession, source, COUNT(jl.id) \
                FROM job_listing jl INNER JOIN job ON job.id = jl.job_id \
                WHERE jl.county = "{county}" \
                AND jl.source IN ({sources_str}) \
                AND profession IN ({professions_str}) \
                AND strftime("%Y-%m", jl.date_gathered) = "{date}" \
                GROUP BY source, county, profession \
                ORDER BY profession, source'
    elif param == "requirement":
        query = f'SELECT profession, source, requirement, COUNT(jl.id) FROM job_listing AS jl \
                INNER JOIN (requirement_relation AS rr \
                INNER JOIN requirement AS r ON rr.requirement_id = r.id) \
                ON jl.id = rr.job_listing_id \
                INNER JOIN (SELECT * FROM job WHERE profession IN ({professions_str})) AS a ON a.id = jl.job_id \
                WHERE jl.county = "{county}" \
                AND jl.source IN ({sources_str}) \
                AND strftime("%Y-%m", jl.date_gathered) = "{date}" \
                GROUP BY profession, source, requirement \
                ORDER BY profession, source'
    else:
        query = f'SELECT profession, source, {param}, COUNT(jl.id) as "sum" \
                FROM job_listing jl INNER JOIN job ON job.id = jl.job_id \
                WHERE jl.county = "{county}" \
                AND jl.source IN ({sources_str}) \
                AND profession IN ({professions_str}) \
                AND strftime("%Y-%m", jl.date_gathered) = "{date}" \
                GROUP BY profession, source, jl.{param} \
                ORDER BY profession, source'
    fetch = list_of_tuples_to_2d_list(send_query(query))
    result = outer_format(fetch)
    return result

# Delete rows gathered on a specific date, e.g. on '2023-08-06'
def delete_rows(date: str):
    # Step 1: Connect to the database
    connection = connect(db_path)

    try:
        # Step 2: Create a cursor
        cursor = connection.cursor()

        # Step 3: Execute the query
        cursor.execute('DELETE FROM job_listing WHERE date_gathered=?;', (date,))

        # Step 4: Commit the changes
        connection.commit()

    except Error as e:
        print(f"Error occurred: {e}")

    finally:
        # Step 5: Close the cursor and connection
        cursor.close()
        connection.close()
        print(f'Row(s) gathered from {date} have been deleted')

def fetch_all_job_listings():
    connection = connect(db_path)
    try:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM job_listing;')
        rows = cursor.fetchall()
        all_entries = []

        for row in rows:
            all_entries.append(list(row))

    finally:
        cursor.close()
        connection.close()

        return all_entries

# -------------------------------- EXTRACT -------------------------------------------

# Callee
def extract(source:list, county: (list), profession: (list), param:str, date:str) -> list:
    # One profession, many counties
    if isinstance(county, list):
        return get_counties_for_profession(source, county, profession, param, date)
    # One county, many professions
    elif isinstance(profession, list):
        return get_professions_for_county(source, county, profession, param, date)


# Test
if __name__ == '__main__':

    # Extract
    # print(extract(['linkedin', 'platsbanken', 'ledigajobb'], 'stockholms län', ['ingenjör', 'lärare'], 'null', '2023-05'))
    
    # One profession, many counties
    #print(get_counties_for_profession(['linkedin', 'platsbanken', 'ledigajobb'], ['stockholms län', 'uppsala län'], 'ingenjör', 'employment_type', '2023-05'))

    # One county many professions
    #print(get_professions_for_county(['linkedin', 'platsbanken', 'ledigajobb'], 'stockholms län', ['ingenjör', 'lärare'], 'requirement', '2023-05'))

    # Delete rows gathered from specific date
    date = 'enter-date' # example: 2023-05-11
    delete_rows('date')

    # Fetch all job_listings from database
    job_listings = fetch_all_job_listings()
