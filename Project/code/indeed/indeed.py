from playwright.sync_api import sync_playwright
from sys import platform
from bs4 import BeautifulSoup
from time import sleep
from os import path


# Returns list of all counties to scrape
def file_to_list(txt):
    s = '/' if (platform == 'linux' or platform =='darwin') else '\\'
    file_path = path.dirname(path.dirname(path.dirname(__file__))) + s + txt
    return open(file_path, encoding='utf-8').read().splitlines()


# Path to dashboard folder for running the website
def get_html_path():
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
        professions = file_to_list('professions.txt')
        counties = file_to_list('counties.txt')
        for profession in professions:
            for county in counties:
                result.append(get_all_ads(page, profession, county))
        context.close()
        browser.close()
    return result


# Extracts all ads on all pages
def get_all_ads(page, profession, county):
    result = []
    prev_res = []
    number = 0
    while True:
        new_res = get_ads_on_page(page, profession, county, number)
        if new_res == prev_res:
            break
        prev_res = new_res
        result.append(new_res)
        number += 1
    return result

# Extracts data from all ads on one page
def get_ads_on_page(page, profession, county, number): 
    result = [] 
    page.goto(f'https://se.indeed.com/jobb?q={profession}&l={county}&radius=0&start={number}')
    data = page.content().encode('ascii', 'replace').decode('ascii')
    # For each ad on page
    # Return get_ad
    
    
# Extracts data from one ad
def get_ad(ad):
    return #['indeed', profession, county, duration, employment_type, years_of_experience...]


# Defeats popups
def close_popup(page_html):
    try:
        if page_html.find('//*[@id="mosaic-modal-mosaic-provider-desktopserp-jobalert-popup"]/div/div/div[1]') is not None:
            print("found you")
            page_html.find('//*[@id="mosaic-modal-mosaic-provider-desktopserp-jobalert-popup"]/div/div/div[1]/div/button').click(timeout=1000)
            return
    except:
        return

# Test
if __name__ == '__main__':
    #run()
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        data = (get_ads_on_page(page, 'Ingenjör', 'Stockholms län', 15))
        soup = BeautifulSoup(data, features='lxml')
        close_popup(page)
        job_ads = soup.find_all('div', class_="slider_container css-77eoo7 eu4oa1w0")
        print(len(job_ads))
        job_titles = soup.find_all('h2', {'class': 'jobTitle css-1h4a4n5 eu4oa1w0'})
        for job_title in job_titles:
            print(job_title.find('span').get('title').encode('ascii', 'replace').decode('ascii'))
        for i in range(1, 18):
            try:
                if i == 6 or i == 9:
                    continue
                test = page.locator(f'xpath=//*[@id="mosaic-provider-jobcards"]/ul/li[' + str(i) + ']/div/div[1]/div/div[1]').click(timeout=1000)
                ad = soup.find('div', class_="jobsearch-RightPane")
                # Finds the entire job description of an ad
                body_text = ad.find('div', {'class': 'jobsearch-jobDescriptionText jobsearch-JobComponent-description'})
                for paragraph in body_text:
                    print(paragraph)
                #sleep(1)
            except:
                continue
        # context.close()
        # browser.close()

        sleep(1000000)
