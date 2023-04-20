import sqlite3
import pandas as pd


#Source: https://towardsdatascience.com/starting-with-sql-in-python-948e529586f2













#Extract Data from DB

# SELECT COUNT(id) FROM job_listing WHERE location_id IN (SELECT location_id FROM location WHERE county IN ("lan") );

# Displays the number of jobs in each county
# SELECT COUNT(id), location.county FROM job_listing INNER JOIN location ON location.id = job_listing.location_id GROUP BY county;

def insert_data(argument_list, sql_connect, cursor):

    argument_list[2] = str(argument_list[2])
    argument_list[7] = str(argument_list[7])

    # dumb demo
    # print(argument_list)

    #job_param_list is the list of arguments for the job_listing table.
    job_param_list = argument_list[0:4] + [argument_list[5], argument_list[7], argument_list[8], argument_list[9]]
    delimiter = "','"
    # liststr = delimiter.join(job_param_list)

    #SQL commands to insert the job_listing, multiple ones because the information is spread among multiple tables.
    # Also some values derived after insert functions 
    #
    #Get id has to be executed right after the row has been inserted.

    #getting job id for job_listing insert
    job_exists_query = "SELECT * FROM job WHERE profession = '" + argument_list[4] + "';"

    job_exist_result = cursor.execute(job_exists_query).fetchall()

    #If job_exist_result is empty(empty lists are interpreted as false), insert profession. 
    if not job_exist_result:
        insert_job = "INSERT INTO job(profession) VALUES ('" + argument_list[4] + "');"
        cursor.execute(insert_job)
        sql_connect.commit()


    get_job_id = "SELECT id FROM job WHERE profession = '" + argument_list[4] + "';"
    job_id = str(cursor.execute(get_job_id).fetchall()[0][0])



    #Create Job listing here and get job_listing_id
    # Index 0-3 is source, employment type, duration and publication date. These are already strings, job id is a foreing key so the id from job_id is entered there instead of proffession.


    if not job_param_list[1]:
            job_param_list[1] = "null"
    if not job_param_list[5]:
            job_param_list[5] = "0"
    if not job_param_list[6]:
            job_param_list[6] = "null"
    if not job_param_list[7]:
            job_param_list[7] = "null"


    insert_job_listing = "INSERT INTO job_listing (source, employment_type, duration, publication_date, job_id, county, years_of_experience, seniority, date_gathered) VALUES ('" + delimiter.join(job_param_list[0:4]) + "'," + job_id + ",'" + delimiter.join(job_param_list[4:]) + "');"

    cursor.execute(insert_job_listing)
    sql_connect.commit()
    job_listing_id = str(cursor.lastrowid)



    #For each requirement in the job listing, create/find that requirement and create a many-many relation between the job_listing and requirement.
    for i in argument_list[6]:
        i = i.replace("'","")
        requirement_exist_query = "SELECT id FROM requirement WHERE requirement = '" + i + "';"
        requirement_exist_result = cursor.execute(requirement_exist_query).fetchall()
        if not requirement_exist_result:
            Insert_requirement = "INSERT INTO requirement(requirement) VALUES ('" + i + "');"
            cursor.execute(Insert_requirement)
            sql_connect.commit()
        
        get_requirement_id = "SELECT id FROM requirement WHERE requirement = '" + i + "';"
        requirement_id = str(cursor.execute(get_requirement_id).fetchall()[0][0])

        #Creates row for many to many relation table requirement_relation
        insert_requirement_relation = "INSERT INTO requirement_relation(job_listing_id, requirement_id) VALUES (" + job_listing_id + "," + requirement_id + ");"
        cursor.execute(insert_requirement_relation)
        sql_connect.commit()



def send_data(list, path):
    with sqlite3.connect(path) as sql_connect:
        # with sql_connect.cursor() as cursor:
        cursor = sql_connect.cursor()
        insert_data(list, sql_connect, cursor) 
        cursor.close()
        #Close connection 
    sql_connect.close()



def send_2d_list(list, path):

    with sqlite3.connect(path) as sql_connect:
        # with sql_connect.cursor() as cursor:
        cursor = sql_connect.cursor()
        for x in list:
            insert_data(x, sql_connect, cursor) 
        cursor.close()
        #Close connection 
    sql_connect.close()
    


    
    

if __name__ == '__main__':


    # test = [ 
    #     [
    #      "Platsbanken", 
    #      "Heltid", 
    #      "Tillsvidare", 
    #      "19/04/2023",  
    #      "Lärare", 
    #      "Stockholms län", 
    #      [ 
    #         "Lärarutbildning", 
    #         "Lärar erfarenhet", 
    #         "B Körkort"
    #      ], 
    #      "4",
    #      "Mid-level",
    #      "19/04/2023"
    #     ] 
    #     ,   
    #     ["Platsbanken", 
    #     "Heltid", 
    #     "Tillsvidare", 
    #     "19/04/2023",  
    #     "Ingenjör", 
    #     "Stockholms län", 
    #     [], 
    #     None,
    #     "Mid-level",
    #     "19/04/2023"
    #     ] 
    #     ]
    
    test = [
            ['ledigajobb', 'deltid', 0, '2023-04-19', 'Lärare', 'Västra Götalands län', ['Requires a relevant degree'], 0, None, '2023-04-20'],
            ['ledigajobb', 'heltid', 0, '2023-04-19', 'Lärare', 'Västra Götalands län', [], 0, None, '2023-04-20']
    ]
    send_2d_list(test, "echo.db")





