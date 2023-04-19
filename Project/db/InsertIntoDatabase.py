import sqlite3
import pandas as pd


#Source: https://towardsdatascience.com/starting-with-sql-in-python-948e529586f2













#Extract Data from DB

# SELECT COUNT(id) FROM job_listing WHERE location_id IN (SELECT location_id FROM location WHERE county IN ("lan") );

# Displays the number of jobs in each county
# SELECT COUNT(id), location.county FROM job_listing INNER JOIN location ON location.id = job_listing.location_id GROUP BY county;

def insert_data(argument_list, sql_connect, cursor):



    job_param_list = argument_list[0:4] + argument_list[5] + argument_list[7] # Get a sub-list from index 0 to 7
    #job_param_list is the list of arguments for the job_listing table.
    delimiter = ","
    liststr = delimiter.join(job_param_list)

    #SQL commands to insert the job_listing, multiple ones because the information is spread among multiple tables.
    # Also some values derived after insert functions 
    #
    #Get id has to be executed right after the row has been inserted.

    #getting job id for job_listing insert
    job_exists_query = "SELECT * FROM job WHERE job = " + argument_list[4] + ";"

    job_exist_result = cursor.execute(job_exists_query).fetchall()

    if not job_exist_result:
        insert_job = "INSERT INTO job(job) VALUES (" + argument_list[4] + ");"
        pd.read_sql_query(insert_job, sql_connect)


    get_job_id = "SELECT id FROM job WHERE job = " + argument_list[4] + ";"
    job_id = cursor.execute(get_job_id).fetchall()[0]

    

    #Getting work_hours_id 
    



    #Create Job listing here and get job_listing_id
    #TODO Make sure publication date is in a uniform format and check attributes.
    # Index 0-3 is source, employment type, duration and publication date. These are already strings, job id is a foreing key so the id from job_id is entered there instead of proffession.

    insert_job_listing = "INSERT INTO job_listing(source, employment_type, duration, publication_date, job_id, county, date_gathered, seniority) VALUES (" + delimiter.join(job_param_list[0:4]) + "," + job_id + "," + delimiter.join(job_param_list[4:-1]) + ");"
    job_listing_id = cursor.execute(insert_job_listing).fetchall()[0]



    #
    for i in argument_list[6]:
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







def for2dlist(list, path):
    sql_connect = sqlite3.connect(path)

    cursor = sql_connect.cursor()

    for x in list:
        insert_data(x, sql_connect, cursor) 
    
    #Close connection 
    sql_connect.close()


    
    

if __name__ == '__main__':

    for2dlist(test, path)





