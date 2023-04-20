# All code explicit for webscraping LinkedIn.com
import csv
import time
import requests
import re
from datetime import date
from bs4 import BeautifulSoup

# Database
db = []

# Jobs
jobs = ["Lärare",
"Läkare",
"Utvecklare",
]

# Geo ids
geo_ids = []
with open('geo_ids.txt', 'r') as f:
    for line in f:
        # Patternmatches for a number with a curly bracket before it and a comma sign after it.
        match = re.search(r'\{(\d+)\,', line)
        if match:
            geo_ids.append(int(match.group(1)))


# Function to scrape websites
def linkedin_scraper(webpage, page_number):
    next_page = webpage + str(page_number)
    print(str(next_page))
    response = requests.get(str(next_page))
    soup = BeautifulSoup(response.content,'html.parser')

    found_jobs = soup.find('main', class_='two-pane-serp-page__results')

    if found_jobs is None:
        print("no ads found")
        return
    else:
        # List of all adds per page.
        # If the titel of the job posting contains the link, then the tag won't be a div
        ads = soup.find_all(['div', 'a'], class_='base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card')
        for ad in ads:
            # If the posting is newly published, it's tag is different
            job_title = ad.find('h3', class_='base-search-card__title')
            if job_title == None:
                job_title = ad.find('h3', class_='base-search-card__title--new').text.strip()
            else:
                job_title = job_title.text.strip()

            # If the posting is newly published, it's tag is different
            ad_date = ad.find('time', class_='job-search-card__listdate')
            if ad_date == None:
                ad_date = ad.find('time', class_='job-search-card__listdate--new').text.strip()
            else:
                ad_date = ad_date.text.strip()

            company = ad.find('h4', class_='base-search-card__subtitle').text.strip()

            location = ad.find('span', class_='job-search-card__location').text.strip()

            # Depending on if the title contains the link        
            link = ad.find('a', class_='base-card__full-link')
            if link == None:
                link = ad['href']
            else:
                link = link['href']

            
            db.append(["Linkedin", "", "", ad_date, "Job", location.split(",")[1].strip().split()[0], [], date.today().strftime("%d/%m/%Y"), ""])
            # print()
            # print(job_title + " | " + company + " | " + location + " | " + ad_date)
            # print(link)
            print(job_title + " | " + location)
            print()

    # if page_number < 1000 and len(ads) == 25:
    #     page_number = page_number + 25
    #     time.sleep(3)
    #     linkedin_scraper(webpage, page_number)

#DEBUG PRINT, DELETE LATER
# linkedin_scraper("https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=&geoId=106710379&start=0", 0)

# for job in jobs:
#     for muni in geo_ids:
#         linkedin_scraper("https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords="+str(job)+"&geoId="+str(muni)+"&start=", 0)
#         print()
#         print()
#         print()
#     print(str(db))