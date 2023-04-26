import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from db.insert import send_2d_list
from ledigajobb import ledigajobb
from platsbanken import platsbanken
from linkedIn import linkedIn


# Database
database_name = "Project\db\echo.db"

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

# Main
if __name__ == '__main__':
    #run_platsbanken()
    #run_ledigajobb()
    run_linkedin()