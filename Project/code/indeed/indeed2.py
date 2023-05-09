from playwright.sync_api import sync_playwright
from sys import platform
from bs4 import BeautifulSoup
from time import sleep
from os import path

# Path to dashboard folder for running the website
def get_html_path():
    match platform:
        case 'linux':
            return 'Project/code/indeed/html.txt'
        case 'darwin':
            return 'Project/code/indeed/html.txt'
        case _:
            return 'Project\code\indeed\html.txt'
        
# Returns list of all counties to scrape
def file_to_list(txt):
    s = '/' if (platform == 'linux' or platform =='darwin') else '\\'
    file_path = path.dirname(path.dirname(path.dirname(__file__))) + s + txt
    return open(file_path, encoding='utf-8').read().splitlines()

# Defeats popups
def close_popup(page):
    try:
        if page.locator('//*[@id="mosaic-modal-mosaic-provider-desktopserp-jobalert-popup"]/div/div/div[1]') is not None:
            print("time to pop you, popup")
            page.locator('//*[@id="google-Only-Modal"]/div/div[1]/button').click(timeout=1000, force=True)
            sleep(1)
            page.locator('//*[@id="mosaic-modal-mosaic-provider-desktopserp-jobalert-popup"]/div/div/div[1]/div/button').click(timeout=1000, force=True)
            return
    except:
        print("failed")
        return

# Returns the parameters of one ad
def get_ad(page, profession, county, page_index, ad_list):
    page.goto(f'https://se.indeed.com/jobb?q={profession}&l={county}&radius=0&start={page_index}')
    sleep(1)
    data = page.content().encode('ascii', 'replace').decode('ascii')
    html = BeautifulSoup(data, features='lxml')
    close_popup(page)
    for i in range(1, 18):
        try:
            page.locator(f'xpath=//*[@id="mosaic-provider-jobcards"]/ul/li[{str(i)}]/div/div[1]/div/div[1]').click(timeout=1000)
            sleep(1)
        except:
            print(i)
            continue
    sleep(100000) #Fortsätt här!!

# Returns a list of all ads for a specified profession and county
def get_all_ads(page, profession, county):
    page.goto(f'https://se.indeed.com/jobb?q={profession}&l={county}&radius=0&start={0}')
    data = page.content().encode('ascii', 'replace').decode('ascii')
    html = BeautifulSoup(data, features='lxml')

    # finds the total amount of jobs found
    job_count = html.find('div', {'class': 'jobsearch-JobCountAndSortPane-jobCount'}).find('span')
    chars_to_remove = "spanjob<>/"
    for char in chars_to_remove:
        job_count = str(job_count).replace(char, "")
    job_count = int(job_count)

    # scrape data on all pages until max_ads_scraped >= job_count
    ad_list = []
    page_index = 0
    max_ads_scraped = 0
    while max_ads_scraped < job_count:
        ad_list = (get_ad(page, profession, county, page_index, ad_list))
        print(max_ads_scraped)
        page_index += 10
        max_ads_scraped += 15
    return ad_list

    sleep(1000000)

def run():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        professions = file_to_list('professions.txt')
        counties = file_to_list('counties.txt')
        result = []
        for profession in professions:
            for county in counties:
                result.append(get_all_ads(page, profession, county))
        context.close()
        browser.close()

if __name__ == '__main__':
    run()