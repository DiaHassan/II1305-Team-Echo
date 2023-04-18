import sqlite3
import pandas as pd

sql_connect = sqlite3.connect('databasename?')

cursor = sql_connect.cursor()

#Values

#Examples
x = "example";
y = str(4);
date = TO_DATE(date)

argplaceholder = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
job_param_list = argplaceholder[0:8] # Get a sub-list from index 0 to 7
#job_param_list is the list of arguments for the job_listing table.
delimiter = ","
liststr = delimiter.join(job_param_list)

county = "placeholder"

municipality = "placeholder"
requirement = "placeholder"
years_of_exp = "placeholder"
work_hours = "placeholder"



#SQL commands to insert the job_listing, multiple ones because the information is spread among multiple tables.
# Also some values derived after insert functions 
Insert_job_listing = "INSERT INTO job_listing(parameters) VALUES (" + job_param_list + ");"

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
Insert_requirement_relation = "INSERT INTO requirement_relation(job_listing_id, requirement_id) VALUES (" + job_listing_id + "," + requirement_id + ");"


work_hours_id = "placeholder"

Inser_work_hours_relation = "INSERT INTO work_hours_relation(job_listing_id, work_hours_id) INSERT VALUES (" + job_listing_id + "," + work_hours_id +");"
