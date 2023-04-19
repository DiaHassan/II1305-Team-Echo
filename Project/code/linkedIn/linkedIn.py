# All code explicit for webscraping LinkedIn.com
import csv
import codecs
import time
import requests
from bs4 import BeautifulSoup


# Function to scrape websites
def linkedin_scraper(webpage, page_number):
    next_page = webpage + str(page_number)
    print(str(next_page))
    response = requests.get(str(next_page))
    soup = BeautifulSoup(response.content,'html.parser')

    # List of all adds per page.
    # If the titel of the job posting contains the link, then the tag won't be a div
    jobs = soup.find_all(['div', 'a'], class_='base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card')
    for job in jobs:
        # If the posting is newly published, it's tag is different
        job_title = job.find('h3', class_='base-search-card__title')
        if job_title == None:
            job_title = job.find('h3', class_='base-search-card__title--new').text.strip()
        else:
            job_title = job_title.text.strip()

        # If the posting is newly published, it's tag is different
        ad_date = job.find('time', class_='job-search-card__listdate')
        if ad_date == None:
            ad_date = job.find('time', class_='job-search-card__listdate--new').text.strip()
        else:
            ad_date = ad_date.text.strip()

        company = job.find('h4', class_='base-search-card__subtitle').text.strip()

        location = job.find('span', class_='job-search-card__location').text.strip()

        # Depending on if the title contains the link        
        link = job.find('a', class_='base-card__full-link')
        if link == None:
            link = job['href']
        else:
            link = link['href']

        print()
        print(job_title + " | " + company + " | " + location + " | " + ad_date)
        print(link)
        print()

    if page_number < 1000 and len(jobs) == 25:
        page_number = page_number + 25
        time.sleep(3)
        linkedin_scraper(webpage, page_number)

# geo_id_file = codecs.open("geo_ids.txt", "r")
# geo_ids = geo_id_file.read
# print(geo_ids)
linkedin_scraper('https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=&location=Sandviken%2C%2BG%C3%A4vleborg%2C%2BSverige&geoId=101153912&trk=public_jobs_jobs-search-bar_search-submit&start=0', 0)
# https://www.linkedin.com/jobs/search?keywords=&geoId=