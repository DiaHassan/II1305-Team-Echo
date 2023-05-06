# Documentation

## Necessary installations:  
- sqlite3 (Python library)
- pandas (Python library)


## [db_sqlite.sql](https://github.com/DiaHassan/II1305-Team-Echo/tree/main/Project/db/db_sqlite.sql)

**job_listing:**
Contains all data parameters for an ad, has FK to table job.

**job:**
Only contains profession.


## [Fortabletest.py](https://github.com/DiaHassan/II1305-Team-Echo/tree/main/Project/db/Fortabletest.py)
[TODO]


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

**get_counties_for_profession(sources, counties, profession, param):**
Queries for extracting data with multiple counties and single profession with optional parameter.

**get_professions_for_county(sources, county, professions, param):**
Queries for extracting data with multiple professions and single county with optional parameter.

**extract(source, county, profession, param):**
Callee, checks if county or profession is a list and then passes arguments to correct function.
