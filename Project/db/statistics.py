import sqlite3
from countyprof import profession_list

# Database path
db_path = 'Project\db\echo.db'


# X-axis: all counties
# Y-axis: number of ads in variable profession 
def get_profession_in_counties(profession):
    with sqlite3.connect(db_path) as conn:
        result = []
        cursor = conn.cursor()
        query = 'SELECT county, count(id) as "sum" FROM job_listing WHERE job_id = (SELECT id FROM job WHERE profession LIKE "%' + profession + '%") AND county IS NOT "null" GROUP BY county'
        fetch = cursor.execute(query).fetchall()
        fetch.insert(0, profession)  
        result.append(fetch)
        cursor.close()
    conn.close()
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
    print(result)
    return result


# Test
if __name__ == '__main__':
    get_profession_in_counties('Städare')
    #get_professions_in_county('Stockholms län')
