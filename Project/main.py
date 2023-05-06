from sys import platform
from os.path import exists, chdir
from sqlite3 import connect
from code import webscrape
#import subprocess
#import pynpm

# Path to database
def find_db_path():
    match platform:
        case "linux":
            return "Project/db/echo.db"
        case "darwin":
            return "Project/db/echo.db"
        case _:
            return "Project\db\echo.db"

# Path to sql for building database
def find_sql_path():
    match platform:
        case "linux":
            return "Project/db/db_sqlite.sql"
        case "darwin":
            return "Project/db/db_sqlite.sql"
        case _:
            return "Project\db\db_sqlite.sql"
            
# Path to dashboard folder for running the website
def find_dashboard_path():
    match platform:
        case 'linux':
            return 'Project/dashboard'
        case 'darwin':
            return 'Project/dashboard'
        case _:
            return 'Project\dashboard'
            
# Builds database
def build_db(db_path, sql_path):

    connection = connect(db_path)
    cursor = connection.cursor()

    sql_file = open(sql_path, "r")
    sql_script = sql_file.read()
    sql_file.close()

    cursor.executescript(sql_script)
    cursor.close()
    connection.close()


# Main 
def run():
  # Builds db with tables if it does not already exists
  db_path = find_db_path()
  if not exists(db_path):
    build_db(db_path, find_sql_path())
  
  # Fill database
  webscrape.run()

  # Dashboard
  # TODO
  # -- npm stuff --   

# Execute
if __name__ == '__main__':
    run()
