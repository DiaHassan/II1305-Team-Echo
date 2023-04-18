# All code explicit for webscraping LinkedIn.com
import csv
import requests
from bs4 import BeautifulSoup


# Function to scrape websites
def linkedin_scraper(webpage, page_number):
    next_page = webpage + str(page_number)
    print(str(next_page))
    response = requests.get(str(next_page))
    soup = BeautifulSoup(response.content,'html.parser')

    jobs = soup.find_all('div', class_='base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card')
    for job in jobs:
        job_title = job.find('h3', class_='base-search-card__title')
        if job_title == None:
            job_title = job.find('h3', class_='base-search-card__title--new').text.strip()
        else:
            job_title = job_title.text.strip()
        company = job.find('h4', class_='base-search-card__subtitle').text.strip()
        location = job.find('span', class_='job-search-card__location').text.strip()
        ad_date = job.find('time', class_='job-search-card__listdate').text.strip()
        print()
        print(job_title + " | " + company + " | " + location + " | " + ad_date)
        print()

    if page_number < 25:
        page_number = page_number + 25
        linkedin_scraper(webpage, page_number)
    
linkedin_scraper('https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=Engineer&location=Stockholm%2C%20Stockholm%2C%20Sverige&geoId=103264854&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0&start=0', 0)