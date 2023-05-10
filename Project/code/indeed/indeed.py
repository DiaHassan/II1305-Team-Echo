from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from time import sleep
from os.path import dirname
from sys import path
path.append(dirname(dirname(__file__)))
from file_to_list import file_to_list


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
    

# Extracts data from one ad     
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
def get_ads_on_page(page, profession, county, page_index):
    page.goto(f'https://se.indeed.com/jobb?q={profession}&l={county}&radius=0&start={page_index}')
    sleep(1)
    close_popup(page)
    for i in range(1, 18):
        try:
            page.locator(f'xpath=//*[@id="mosaic-provider-jobcards"]/ul/li[{str(i)}]/div/div[1]/div/div[1]').click(timeout=10000)
            data = page.content().encode('ascii', 'replace').decode('ascii')
            soup = BeautifulSoup(data, features='lxml')
            ad = soup.find('div', class_="jobsearch-RightPane")
            extract_ad(ad)
        except:
            print(i)
            print("epic fail")
            sleep(1)
            continue
    

# Returns a list of all ads for a specified profession and county
def get_ads_all_pages(page, profession, county):
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