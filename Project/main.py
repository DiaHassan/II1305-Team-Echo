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
    # path = os.path(os.walk('dashboard'))
    # print(path)
    # os.system("cd C:\\Users\\hassa\\OneDrive\\Documents\\Echo\\Project\\dashboard ; npm run start")
    path = os.path.join(os.path.dirname(__file__), 'dashboard')
    
    # p1 = multiprocessing(subprocess.run("npm start", shell=True, cwd=path))
    # Dashboard
    # p2 = multiprocessing(Fortabletest.run())
    os.startfile("Project\db\Fortabletest.py")
    # t2 = threading.Thread(target = Fortabletest.run())
    # t1 = threading.Thread(target = subprocess.run("npm start", shell=True, cwd=path))
    subprocess.run("npm start", shell=True, cwd=path)
    # t2.start()
    

    # -- npm stuff --   

# Execute
if __name__ == '__main__':
    run()
