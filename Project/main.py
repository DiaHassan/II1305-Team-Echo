import os
from os.path import exists, dirname, join
from sqlite3 import connect
from subprocess import run as subprocess_run
#import code.webscrape as webscrape


# DB path
db_path = 'Project/db/echo.db'
sql_path = 'Project/db/db_sqlite.sql'
   

# Builds database
def build_db():
    connection = connect(db_path)
    cursor = connection.cursor()
    sql_file = open(sql_path, "r")
    sql_script = sql_file.read()
    sql_file.close()
    cursor.executescript(sql_script)
    cursor.close()
    connection.close()


# Main function
def run():
    # Builds db with tables if it does not already exists
    if not exists(db_path):
        build_db()
    
    # Run separately for now
    # --------------------------
    # Fill database
    #webscrape.run()
    # --------------------------

    # Dashboard
    table_path = join(join('Project', 'db'), 'data_handler.py')
    os.startfile(table_path)
    # path = join(dirname(__file__), 'dashboard')
    # subprocess_run("npm start", shell=True, cwd=path)


# Execute main function
if __name__ == '__main__':
    run()
