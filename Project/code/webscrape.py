from os import path as os_path
from sys import path as sys_path
sys_path.append(os_path.dirname(os_path.dirname(__file__)))
from db.insert import send_2d_list
from code.ledigajobb import ledigajobb
from code.platsbanken import platsbanken
from code.linkedIn import linkedIn

db_path = 'db/echo.db'

# Webscrape all available websites
def runWebscrape(inp):
    print('Running all webscrapers...')
    if(inp%2 == 0):
        run_platsbanken()
    if(inp%3 == 0):
        run_linkedin()
    if(inp%5 == 0):
        run_ledigajobb()

# Platsbanken
def run_platsbanken():
    print('Webscraping platsbanken...')
    platsbanken_list = platsbanken.runPlatsbanken()
    send_2d_list(platsbanken_list, db_path)
    print('Platsbanken done')

# LedigaJobb
def run_ledigajobb():
    print('Webscraping ledigajobb...')
    ledigajobb_list = ledigajobb.runLedigajobb()
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
    # run_ledigajobb()
    #run_linkedin()
