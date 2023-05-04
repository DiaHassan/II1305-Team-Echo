from playwright.sync_api import sync_playwright
from sys import platform
from countyprof import county_list, profession_list
from bs4 import BeautifulSoup

# Path to dashboard folder for running the website
def get_html_create_path():
    match platform:
        case 'linux':
            return 'Project/code/indeed/html.txt'
        case 'darwin':
            return 'Project/code/indeed/html.txt'
        case _:
            return 'Project\code\indeed\html.txt'

# Main
def run():
    result = []
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        for profession in profession_list:
            for county in county_list:
                result.append(get_html(page, profession, county))
        context.close()
        browser.close()
    return result

# Runs 
def get_html(page, profession, county): 
    page.goto(f'https://se.indeed.com/jobb?q={profession}&l={county}&radius=0')
    data = page.content().encode('ascii', 'replace').decode('ascii')
    return data

# Test
if __name__ == '__main__':
    #run()
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        data = (get_html(page, 'Lärare', 'Stockholms län'))
        soup = BeautifulSoup(data,'html')
        employment_type = soup.find_all('div', class_="attribute_snippet")
        print(len(employment_type))
        context.close()
        browser.close()
    