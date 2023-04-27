import sqlite3
from countyprof import profession_list

# Database path
db_path = 'Project\db\echo.db'


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
    print(result)
    return result     


# X-axis: all counties
# Y-axis: number of ads in variable profession 
def get_profession_in_counties(profession):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        query = 'SELECT county, count(id) as "sum" FROM job_listing WHERE job_id = (SELECT id FROM job WHERE profession LIKE "%' + profession + '%") AND county IS NOT "null" GROUP BY county'
        result = cursor.execute(query).fetchall()  
        cursor.close()
    conn.close()
    result = list_of_tuples_to_2d_list(result)
    result.insert(0, profession)
    print(result)
    return result


# X-axis: all professions
# Y-axis: number of professions in variable county
def get_professions_in_county(county): 
    with sqlite3.connect(db_path) as conn:
        result = []
        cursor = conn.cursor()
        for profession in profession_list:
            query = 'SELECT "' + profession +  '" AS profession, count(job_listing.id) as "sum" FROM job_listing INNER JOIN job ON job.id = job_listing.job_id WHERE county = "' + county + '" AND profession LIKE "%' + profession + '%"'
            result.append(cursor.execute(query).fetchall())
        cursor.close()
    conn.close()
    result = list_of_list_tuple_to_2d_list(result)
    result.insert(0, county)
    print(result)
    return result

# X-axis: employment type per county
# Y-axis: number of ads in variable profession
def get_employment_type_per_county(profession): 
    with sqlite3.connect(db_path) as conn:
        result = []
        cursor = conn.cursor()
        query = 'SELECT j.county, j.employment_type, \
                    CASE WHEN p.profession LIKE "%' + profession + '%" THEN "' + profession + '" ELSE p.profession END AS profession, \
                    COUNT(*) as count \
                FROM job_listing j \
                JOIN job p ON j.job_id = p.id \
                WHERE p.profession LIKE "%' + profession + '%" AND employment_type IS NOT + "null"\
                GROUP BY j.county, j.employment_type, \
                    CASE WHEN p.profession LIKE "%' + profession + '%" THEN "' + profession + '" ELSE p.profession END;'
        result.append(cursor.execute(query).fetchall())
        cursor.close()
    conn.close()
    result = list_of_tuples_to_2d_list(result)
    result.insert(0, profession)
    print(result)
    return result


# Test
if __name__ == '__main__':
    # get_profession_in_counties('Städare')
    # get_professions_in_county('Stockholms län')
    get_employment_type_per_county('Läkare')

