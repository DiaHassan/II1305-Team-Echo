import sqlite3
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))


# Connect to database
def connect_db():
    conn = sqlite3.connect('echo.db')
    return conn.cursor()


# X-axis: all counties
# Y-axis: number of ads in variable profession 
def get_profession_per_county(cursor, profession):
    query = 'SELECT county, count(id) as "sum" FROM job_listing WHERE job_id = (SELECT id FROM job WHERE', profession, '= "yrke") GROUP BY county'
    return cursor.execute(query).fetchall()


# X-axis: all professions
# Y-axis: number of professions in variable county
def get_professions_in_county(cursor, county): 
    query = 'SELECT profession, count(job_listing.id) as "sum" FROM job_listing INNER JOIN job ON job.id = job_listing.job_id WHERE county =', county, 'GROUP BY profession'
    return cursor.execute(query).fetchall()




