import sqlite3
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from job_info import yrke_list, lan_list

# Database path
db_path = 'Project\db\echo.db'


# X-axis: all counties
# Y-axis: number of ads in variable profession 
def get_profession_in_counties():
    with sqlite3.connect(db_path) as conn:
        result = []
        cursor = conn.cursor()
        for profession in yrke_list:
            query = 'SELECT county, count(id) as "sum" FROM job_listing WHERE job_id = (SELECT id FROM job WHERE profession = "' + profession + '") GROUP BY county'
            result.append(cursor.execute(query).fetchall())
        cursor.close()
    conn.close()
    print(result)
    return result



# X-axis: all professions
# Y-axis: number of professions in variable county
def get_professions_in_county(): 
    with sqlite3.connect(db_path) as conn:
        result = []
        cursor = conn.cursor()
        for county in lan_list:
            query = 'SELECT profession, count(job_listing.id) as "sum" FROM job_listing INNER JOIN job ON job.id = job_listing.job_id WHERE county = "' + county[1] + '" GROUP BY profession'
            print(query)
            result.append(cursor.execute(query).fetchall())
        cursor.close()
    conn.close()
    print(result)
    return result



if __name__ == '__main__':
    #get_profession_in_counties()
    get_professions_in_county()
