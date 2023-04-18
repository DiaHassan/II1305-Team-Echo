import sqlite3
import pandas as pd


#Source: https://towardsdatascience.com/starting-with-sql-in-python-948e529586f2


sql_connect = sqlite3.connect('databasename?')

cursor = sql_connect.cursor()

#Values

#Examples
x = "example";
y = str(4);
date = TO_DATE(date)

argplaceholder = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



county = "placeholder"

municipality = "placeholder"
requirement = "placeholder"
years_of_exp = "placeholder"
work_hours = "placeholder"





#440 bits = 55 bytes per row.


#Get id has to be executed right after the row has been inserted.
get_job_listing_id = "SELECT SCOPE_IDENTITY();"

Insert_job = "INSERT INTO job(job) VALUES (" + job + ");"

get_job_id = "SELECT SCOPE_IDENTITY();"

Insert_location = "INSERT INTO location(county, municipality) VALUES (" + county + "," + municipality + ");"

get_location_id = "SELECT SCOPE_IDENTITY();"

Insert_requirement = "INSERT INTO requirement(requirement, years_of_experience) VALUES (" + requirement + "," + years_of_exp + ");"

get_requirement = "SELECT SCOPE_IDENTITY();"

Insert_work_hours = "INSERT INTO work_hours(work_hours) VALUES (" + work_hours + ");"

get_work_hours_id = "SELECT SCOPE_IDENTITY();"


#TODO Make code to execute previous SQL commands.
job_listing_id = "placeholder"
requirement_id = "placeholder"



work_hours_id = "placeholder"

Inser_work_hours_relation = "INSERT INTO work_hours_relation(job_listing_id, work_hours_id) INSERT VALUES (" + job_listing_id + "," + work_hours_id +");"


#Execute SQL commands and store results

results_job_listing = cursor.execute(Insert_job_listing).fetchall()

results_insert_job = cursor.execute(Insert_job).fetchall()

results_location = cursor.execute(Insert_location).fetchall()

results_requirement = cursor.execute(Insert_requirement).fetchall()

results_work_hours = cursor.execute(Insert_work_hours).fetchall()



#Running Queries TODO

pd.read_sql_query(Insert_job_listing,sql_connect)




#Close connection 

sql_connect.close()

#Extract Data from DB

# SELECT COUNT(id) FROM job_listing WHERE location_id IN (SELECT location_id FROM location WHERE county IN ("lan") );

# Displays the number of jobs in each county
# SELECT COUNT(id), location.county FROM job_listing INNER JOIN location ON location.id = job_listing.location_id GROUP BY county;

def insert_data(argument_list):
    job_param_list = argument_list[0:8] # Get a sub-list from index 0 to 7
    #job_param_list is the list of arguments for the job_listing table.
    delimiter = ","
    liststr = delimiter.join(job_param_list)

    #SQL commands to insert the job_listing, multiple ones because the information is spread among multiple tables.
    # Also some values derived after insert functions 
    #
    #Get id has to be executed right after the row has been inserted.

    #getting job id for job_listing insert
    job_exists_query = "SELECT * FROM job WHERE job = " + argument_list[7] + ";"

    job_exist_result = cursor.execute(job_exists_query).fetchall()

    if not job_exist_result:
        insert_job = "INSERT INTO job(job) VALUES (" + argument_list[7] + ");"
        pd.read_sql_query(insert_job,sql_connect)


    get_job_id = "SELECT id FROM job WHERE job = " + argument_list[7] + ";"
    job_id = cursor.execute(get_job_id).fetchall()[0]

    #TODO getting location id for job_listing insert and creating location if it doesn't exist
    

    #Getting work_hours_id 




    #Create Job listing here and get job_listing_id
    #TODO Make sure publication date is in a uniform format
    insert_job_listing = "INSERT INTO job_listing(source, employment_type, duration, min_salary, max_salary, salary_type, publication_date, job_id, location_id, date_gathered) VALUES (" + job_param_list + ");"
    job_listing_id = cursor.execute(insert_job_listing).fetchall()[0]




    for i in argument_list[10]:
        requirement_exist_query = "SELECT id FROM requirement WHERE requirement = " + i[0] + " AND years_of_experience = " + i[1] + ";"
        requirement_exist_result = cursor.execute(requirement_exist_query).fetchall()
        if not requirement_exist_result:
            Insert_requirement = "INSERT INTO requirement(requirement, years_of_experience) VALUES ( + " + i[0] + "," + i[1] + ");"
            pd.read_sql_query(Insert_requirement, sql_connect)
        
        get_requirement_id = "SELECT id FROM requirement WHERE requirement = " + i[0] + " AND years_of_experience = " + i[1] + ";"
        requirement_id = cursor.execute(get_requirement_id).fetchall()[0]

        #Creates row for many to many relation table requirement_relation
        insert_requirement_relation = "INSERT INTO requirement_relation(job_listing_id, requirement_id) VALUES (" + job_listing_id + "," + requirement_id + ");"
        cursor.execute(insert_requirement_relation, sql_connect)







    
    








