import sqlite3
import pandas as pd
from os.path import exists
from sys import platform

#Source: https://towardsdatascience.com/starting-with-sql-in-python-948e529586f2


def find_db_path(platform):
        match platform:
            case "linux":
                return "Project/db/echo.db"
            case "darwin":
                return "Project/db/echo.db"
            case _:
                return "Project\db\echo.db"

def find_db_sqlite_path(platform):
        match platform:
            case "linux":
                return "Project/db/db_sqlite.sql"
            case "darwin":
                return "Project/db/db_sqlite.sql"
            case _:
                return "Project\db\db_sqlite.sql"

# Builds database
def build_db():

    connection = sqlite3.connect(find_db_path(platform))
    cursor = connection.cursor()

    sql_file = open(find_db_sqlite_path(platform), "r")
    sql_script = sql_file.read()
    sql_file.close()

    cursor.executescript(sql_script)
    cursor.close()
    connection.close()


# Extract Data from DB

# SELECT COUNT(id) FROM job_listing WHERE location_id IN (SELECT location_id FROM location WHERE county IN ("lan") );

# Displays the number of jobs in each county
# SELECT COUNT(id), location.county FROM job_listing INNER JOIN location ON location.id = job_listing.location_id GROUP BY county;

def insert_data(argument_list, sql_connect, cursor):

    argument_list[2] = str(argument_list[2])
    argument_list[7] = str(argument_list[7])

    # dumb demo
    # print(argument_list)

    #job_param_list is the list of arguments for the job_listing table.
    job_param_list = argument_list
    delimiter = "','"
    # liststr = delimiter.join(job_param_list)

    #SQL commands to insert the job_listing, multiple ones because the information is spread among multiple tables.
    # Also some values derived after insert functions 
    #
    #Get id has to be executed right after the row has been inserted.

    if(argument_list[4] == "" or argument_list[4] == " "):
        return
    


    #Create Job listing here and get job_listing_id
    # Index 0-3 is source, employment type, duration and publication date. These are already strings, job id is a foreing key so the id from job_id is entered there instead of proffession.

    # Handling 'None' inputs
    if not job_param_list[1]:           # Employment type   
            job_param_list[1] = "null"
    if job_param_list[2] == "None":     # Duration
            job_param_list[2] = "null"
    if not job_param_list[3]:           # Publication Date
         job_param_list[3] = "null"
    if not job_param_list[6]:           # Education
            job_param_list[6] = "null"
    if job_param_list[7] == "None":     # Years of experience
        job_param_list[7] = "null"
    if not job_param_list[8]:           # Seniority
            job_param_list[8] = "null"


    insert_job_listing = "INSERT INTO job_listing (source, employment_type, duration, publication_date, profession, county, education, years_of_experience, seniority, date_gathered) VALUES ('" + delimiter.join(job_param_list) + "');"

    cursor.execute(insert_job_listing)
    sql_connect.commit()
    job_listing_id = str(cursor.lastrowid)


# Recieves 1d list of ad and inserts into db
def send_data(list, path):
    with sqlite3.connect(path) as sql_connect:
        # with sql_connect.cursor() as cursor:
        cursor = sql_connect.cursor()
        insert_data(list, sql_connect, cursor) 
        cursor.close()
        #Close connection 
    sql_connect.close()


# Recieves 2d list of ads and inserts them into db
def send_2d_list(list, path):

    # Builds db with tables if it does not already exists
    if not exists(path):
        build_db()
        
    with sqlite3.connect(path) as sql_connect:
        # with sql_connect.cursor() as cursor:
        cursor = sql_connect.cursor()
        for x in list:
            insert_data(x, sql_connect, cursor) 
        cursor.close()
        #Close connection 
    sql_connect.close()
    

# Test if run
if __name__ == '__main__':
    
    test = [
            ['ledigajobb', 'deltid', 0, '2023-04-19', 'Lärare', 'Stockholms län', 'Requires a relevant degree', 0, None, '2023-04-20'],
            ['ledigajobb', 'heltid', 0, '2023-04-19', 'Lärare', 'Västra Götalands län', None, 0, 'basnivå', '2023-04-20']
    ]
    #send_2d_list(test, find_db_path(platform))