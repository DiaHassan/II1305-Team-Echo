from os import startfile
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


# Creates endpoint and starts website on port 3000
def init_dashboard():
    data_handler_path = join(join('Project', 'db'), 'data_handler.py')
    startfile(data_handler_path)
    dashboard_path = join(dirname(__file__), 'dashboard')
    subprocess_run("npm start", shell=True, cwd=dashboard_path)


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
    init_dashboard()


# Execute main function
if __name__ == '__main__':
    run()
