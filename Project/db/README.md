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
Contains SQL queries to extract data from database.

### Functions:

**send_query(query):**
Connects to database and sends given query to it, returns result in 2d list.

**get_profession_in_counties(profession)**
Recieves profession, returns list of tuples containing counties and their respective amount of ads for the profession.

**get_param_per_county(profession, param):**
Recieves a profession and a parameter in the job_listing SQL table (such as employment_type) and returns a list of tuples countaining counties and the amount of ads in the categories of param.

**get_professions_in_county(county)**
Recieves county, returns list of tuples containing professions and their number of ads in the county.  
