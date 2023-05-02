import os
import sys
from sys import platform
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from db.insert import send_2d_list
from ledigajobb import ledigajobb
from platsbanken import platsbanken
from linkedIn import linkedIn


def find_db_path(platform):
    match platform:
        case "linux":
            return "Project/db/echo.db"
        case "darwin":
            return "Project/db/echo.db"
        case default:
            return "Project\db\echo.db"

database_name = find_db_path(platform)

# Platsbanken
def run_platsbanken():
    platsbanken_list = platsbanken.run()
    send_2d_list(platsbanken_list, database_name)
    print('Platsbanken done')

# LedigaJobb
def run_ledigajobb():
    ledigajobb_list = ledigajobb.run()
    send_2d_list(ledigajobb_list, database_name)
    print('LedigaJobb done')

# LinkedIn
def run_linkedin():
    linkedIn_list = linkedIn.run()
    send_2d_list(linkedIn_list, database_name)
    print(' LinkedIn done')

# Main
if __name__ == '__main__':
    run_platsbanken()
    # run_ledigajobb()
    # run_linkedin()