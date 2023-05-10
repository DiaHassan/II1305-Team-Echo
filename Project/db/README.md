# Documentation

## [db_sqlite.sql](https://github.com/DiaHassan/II1305-Team-Echo/tree/main/Project/db/db_sqlite.sql)
Database of job listings from different sources with specific paramaters extracted.

**job_listing:**
Contains all data parameters for an ad, has FK to table job.

**job:**
Only contains profession.

**requirement**
Only contains pre-requirements for jobs, such as bachelor's degree


## [data_handler.py](https://github.com/DiaHassan/II1305-Team-Echo/tree/main/Project/db/data_handler.py)
Connects json request to python extract of database.


## [insert.py](https://github.com/DiaHassan/II1305-Team-Echo/tree/main/Project/db/insert.py)
Inserts data into the SQL database.

### Functions
**insert_data(argument_list, sql_connect, cursor):**
Inserts arguments in list from an ad into database using a connection and cursor.

**send_data(list, path):**
Connects to database and forwards connection and list of data from ad to function insert_data.

**send_2d_list(list, path):**
Connects to database and sends each list in 2d list to function send_data.


## [extract.py](https://github.com/DiaHassan/II1305-Team-Echo/tree/main/Project/db/extract.py)
Extracts data from database. 

### Functions:

**send_query(query):**
Connects to database and sends given query to it, returns result in 2d list.

**get_counties_for_profession(sources, counties, profession, param, date):**
Queries for extracting data with multiple counties and single profession with optional parameter during specific year-month.

**get_professions_for_county(sources, county, professions, param, date):**
Queries for extracting data with multiple professions and single county with optional parameter during specific year-month.

**extract(source, county, profession, param, date):**
Callee, checks if county or profession is a list and then passes arguments to correct function.
