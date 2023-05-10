###########################
# As of 10/5-2023, broken #
###########################

# Imports
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from time import sleep
from os.path import dirname
from sys import path
path.append(dirname(dirname(__file__)))
from file_to_list import file_to_list
import random


# Path to hmtl.txt
html_path = 'Project/code/indeed/html.txt'


# Annihilates popups
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
    
# FORTSÄTT HÄR
# Should annihilate popup tabs
def handle_popup_tab(popup):
    popup.wait_for_load_state()
    print(popup.title())

# Extracts data from one ad   
# nu orkar jag inte koda på Githubs laggiga sida så fortsätt med: byt så att argumentet ad istället är en page, och gör så
# all extraktion är gjord med playwrights locator istället
def extract_ad(ad):
    # [source, employment_type, duration, publication_date, profession, county, req, years, seniority, date_extracted, desc]
    data = []
    print(ad.find('div', class_='jobsearch-JobInfoHeader-title-container'))
    # employment_type = ad.find('div', {'class': 'css-m539th eu4oa1w0'})

    print(employment_type)
    if ad.find('Heltid') is not None:
        employment_type = 'heltid'
    elif ad.find('Deltid') is not None:
        employment_type = 'deltid'
    else:
        employment_type = 'null'
    print(employment_type)    
    return data

# Returns the parameters of one ad
def get_ads_on_page(page, profession:str, county:str, page_index:int):
    page.goto(f'https://se.indeed.com/jobb?q={profession}&l={county}&radius=0&start={page_index}')
    sleep(1)
    close_popup(page)
    for i in range(1, 18):
        try:
            page.locator(f'xpath=//*[@id="mosaic-provider-jobcards"]/ul/li[{str(i)}]/div/div[1]/div/div[1]').click(timeout=1000)
            data = page.content().encode('ascii', 'replace').decode('ascii')
            html = BeautifulSoup(data, features='lxml')
            ad = html.find('div', class_="jobsearch-RightPane")

            # finds the job title
            #job_title = html.find('div', {'class': 'css-1p3gyjy e1xnxm2i0'})
            sleep(0.5)
            job_title = page.locator('//*[@id="jobsearch-ViewjobPaneWrapper"]/div/div/div/div[1]/div/div/div[1]/div[1]/h2').all_text_contents()
            employment_type = page.locator('//*[@id="jobDetailsSection"]/div[2]/div[2]/div/div[1]').all_text_contents()
            body_text = page.locator('//*[@id="jobDescriptionText"]').all_text_contents()
            # chars_to_remove = "span<>/"
            # for char in chars_to_remove:
            #     job_title = str(job_title).replace(char, "")
            print(job_title)
            print(employment_type)
            print(body_text)

            sleep(0.5)
        except:
            print(i)
            print("epic fail")
            continue
  
# Returns a list of all ads for a specified profession and county
def get_ads_all_pages(page, profession:str, county:str):
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
        ad_list.append((get_ads_on_page(page, profession, county, page_index)))
        print(max_ads_scraped)
        page_index += 10
        max_ads_scraped += 15
        sleep(random.randint(1, 3))
    return ad_list

# Main function
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
                result.append(get_ads_all_pages(page, profession, county))
        context.close()
        browser.close()

# Run test
if __name__ == '__main__':
    run()