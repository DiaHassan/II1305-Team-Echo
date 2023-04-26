# All code explicit for webscraping LinkedIn.com
import time
import requests
import re
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__))) # Get the directory above
from reqfinder import find_req # Program to look through bodytext
from datetime import date, timedelta
from bs4 import BeautifulSoup

# Duplicates counter (REMOVE LATER)
duplicates = 0

# Keep track of unique adds
seen = {}

# Timer (REMOVE LATER)
start_time = time.time()

# Function to scrape websites
def linkedin_scraper(job, municipality, page_number):
    # try:     
    url1 = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords="     
    url2 = "&geoId="     
    url3 = "&start="     
    next_page = url1 + str(job) + url2 + str(municipality) + url3 + str(page_number)
    print(str(next_page))
    # Establish connection
    while(True):
        response = requests.get(str(next_page))
        if(response.status_code == 200):
            break
    soup = BeautifulSoup(response.content,'html.parser')

    # Temp list for every ad per proffesion per municipality
    temp = []

    # Check that ads actually exist on page
    found_jobs = soup.find('li')
    if found_jobs is None:
        return([])
    else:
        # List of all adds per page
        # If the title of the job posting contains a link, then the tag won't be a div
        ads = soup.find_all(['div', 'a'], class_='base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card')
        for ad in ads:
#----------------------------Get HTML elements------------------------------------------------
            # Job title
            # DATA NOT NEEDED, DELETE LATER
            job_title = ad.find('h3', class_='base-search-card__title')
            if job_title == None:
                # Ad published today
                job_title = ad.find('h3', class_='base-search-card__title--new').text.strip()
            else:
                job_title = job_title.text.strip()

            # Ad date
            ad_date = ad.find('time', class_='job-search-card__listdate')
            if ad_date == None:
                # Ad published today
                ad_date = ad.find('time', class_='job-search-card__listdate--new').text.strip()
            else:
                ad_date = ad_date.text.strip()

            # Ad url        
            link = ad.find('a', class_='base-card__full-link')
            if link == None:
                link = ad['href']
            else:  
                link = link['href']
            
            # Location (Only allows sweden)
            location = ad.find('span', class_='job-search-card__location').text.strip()
            location_country = location.split(", ")[-1]
            if location_country not in ["Sweden", "sweden", "Sverige", "sverige"]:
                continue

            # Get unique identifier for each ad
            key_tag = ad['data-entity-urn']
            key = key_tag.split(':')[-1]

#----------------------------Extracts proper format-------------------------------------------

            # Calculating the estimated publication date (unable to be exact)
            ad_date_list = ad_date.split(" ")
            match ad_date_list[1]:
                case 'days' | 'day':
                    ad_publication_date = date.today() - timedelta(days=int(ad_date_list[0]))
                case 'weeks' | 'week':
                    ad_publication_date = date.today() - timedelta(weeks=int(ad_date_list[0]))
                case 'months' | 'month':
                    ad_publication_date = date.today() - timedelta(days=int(ad_date_list[0])*31)
                case _:
                    ad_publication_date = date.today()
            ad_publication_date = str(ad_publication_date)

            # Extracting county
            try:
                county = location[location.index(', ')+2:location.index(' County')]
            except:
                county = location[location.index(', ')+2:location.index(', Sweden')]

#----------------------------Extracts HTML from each ad-page----------------------------------

            seniority = None
            employment_type = None

            # Establish connection to ad-page
            wait = 0
            while(True):
                ad_response = requests.get(link)
                if(ad_response.status_code == 200):
                    break
                print("RETRYING")
                wait = wait + 1
                print(ad_response)
                print(ad_response.headers) 
                time.sleep(0.1) # Delay because of status code 429
                if wait == 15:  # Bigger delay incase it gets stuck
                    print("WAIT")
                    time.sleep(9.9) 
                    wait = 0
            wait = 0
            ad_soup = BeautifulSoup(ad_response.content,'html.parser')
            
            #Get HTML element for ad-page
            ad_criterias = ad_soup.find_all('li', class_='description__job-criteria-item')
            ad_description = ad_soup.find('div', 'show-more-less-html__markup').text

            # Look for seniority and employment type
            for item in ad_criterias:
                header = item.find('h3', class_='description__job-criteria-subheader').text.strip()
                
                if(header == 'Yrkesnivå'):
                    seniority = item.find('span', class_='description__job-criteria-text--criteria').text.strip()
                if(header == 'Anställningstyp'):
                    employment_type = item.find('span', class_='description__job-criteria-text--criteria').text.strip()
            
            # Look through body text for education
            education = find_req(ad_description)

#----------------------------Saves parameters-------------------------------------------------

            print(job_title + " | " + location )
            temp.append(["Linkedin", employment_type, None, ad_publication_date, job, county, education, None, date.today().strftime('%Y-%m-%d'), seniority, key])

    #Remove duplicates and the key element 
    list = []
    for item in temp:
        identifier = item[-1]
        if identifier not in seen:
            seen[identifier] = True
            list.append(item[:-1])
        else:
            global duplicates
            duplicates = duplicates + 1


    if page_number < 1000 and len(ads) == 25:
        page_number = page_number + 25
        linkedin_scraper(job, municipality, page_number)
    return(list)
    
    
    # except:
    #     print()
    #     print("Time it took: " + str(time.time()-start_time))
    #     print("Fail")
    #     print("Duplicates: " + str(duplicates))


def run():
    start_time = time.time()
    # Database
    db = []

    # Jobs
    jobs = ["Lärare"]#, "Läkare", "Utvecklare", "Sjuksköterska", "Kock", "Operatör", "Personlig assistent", "Mekaniker", "Butikssäljare", "Civilingenjör", "Projektledare", "Städare"]

    # Geo ids
    # geo_ids = [106366684] 
    geo_ids = []
    with open('project\code\linkedIn\geo_ids.txt', 'r') as f:
        for line in f:
            # Patternmatches for a number with a curly bracket before it and a comma sign after it.
            match = re.search(r'\{(\d+)\,', line)
            if match:
                geo_ids.append(int(match.group(1)))

    for job in jobs:
        for muni in geo_ids:
            data = linkedin_scraper(job, muni, 0)
            db = data + db
        # Reset seen unique adds when changing career
        global seen
        seen = {}

    print("Time it took: " + str(time.time()-start_time))
    print("Success")
    print("Duplicates: " + str(duplicates))
    print("Length of list: " + str(len(db)))
    return db