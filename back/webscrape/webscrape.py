from os import path as os_path
from sys import path as sys_path
sys_path.append(os_path.dirname(os_path.dirname(__file__)))
from db.insert import send_2d_list
from ledigajobb import ledigajobb
from platsbanken import platsbanken
from linkedIn import linkedIn

db_path = 'Project/db/echo.db'

# Webscrape all available websites
def run():
    print('Running all webscrapers...')
    run_platsbanken()
    run_linkedin()
    run_ledigajobb()

# Platsbanken
def run_platsbanken():
    print('Webscraping platsbanken...')
    platsbanken_list = platsbanken.run()
    send_2d_list(platsbanken_list, db_path)
    print('Platsbanken done')

# LedigaJobb
def run_ledigajobb():
    print('Webscraping ledigajobb...')
    ledigajobb_list = ledigajobb.run()
    send_2d_list(ledigajobb_list, db_path)
    print('LedigaJobb done')

# LinkedIn
def run_linkedin():
    print('Webscraping linkedin...')
    linkedIn_list = linkedIn.run()
    send_2d_list(linkedIn_list, db_path)
    print('LinkedIn done')

# Main
if __name__ == '__main__':
    # run()
    run_platsbanken()
    #run_ledigajobb()
    #run_linkedin()
