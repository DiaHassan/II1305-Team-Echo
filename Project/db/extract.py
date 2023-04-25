import sqlite3
import pandas as pd

#Extract Data from Database
def extract_data(x_axis, x_category, y_axis, y_category, sql_connect, cursor):
    
    #TODO, decide arguments. 
    #x_axis is the parameter we want to group by. 
    #y_axis is the paremeter we want to measure. 
    #x/y category is the category x/y_axis belongs to. This is to make the code more efficient.
    #filter, additional filters.


    delimiter = "','"
    # liststr = delimiter.join(job_param_list)

    #SQL commands to insert the job_listing, multiple ones because the information is spread among multiple tables.
    # Also some values derived after insert functions 
    #
    #Get id has to be executed right after the row has been inserted.
    query_string = "SELECT"

    if 


    #getting job id for job_listing insert
    job_exists_query = "SELECT * FROM job WHERE profession = '" + argument_list[4] + "';"

    job_exist_result = cursor.execute(job_exists_query).fetchall()



def send_data(list, path):
    with sqlite3.connect(path) as sql_connect:
        # with sql_connect.cursor() as cursor:
        cursor = sql_connect.cursor()
        insert_data(list, sql_connect, cursor) 
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





