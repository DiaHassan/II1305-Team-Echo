from sys import platform
from os.path import exists
from sqlite3 import connect
# from code import webscrape
from db import Fortabletest , extract
import subprocess
import threading
import os
import sys
#import subprocess
#import pynpm

# DB path
db_path = 'Project/db/echo.db'
sql_path = 'Project/db/db_sqlite.sql'
            
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
def build_db():

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
    if not exists(db_path):
        build_db()
    
    # Fill database
    # webscrape.run()

    # Dashboard
    table_path = os.path.join(os.path.join('Project', 'db'), 'Fortabletest.py')
    os.startfile(table_path)
    path = os.path.join(os.path.dirname(__file__), 'dashboard')
    subprocess.run("npm start", shell=True, cwd=path)
    
# Execute
if __name__ == '__main__':
    run()
