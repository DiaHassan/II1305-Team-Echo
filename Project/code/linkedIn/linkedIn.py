# All code explicit for webscraping LinkedIn.com
import time
import requests
import re
from datetime import date, timedelta
from bs4 import BeautifulSoup

# Database
db = []

# Jobs
jobs = ["Lärare",
"Läkare",
"Utvecklare"
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

    # Check that ads actually exist on page
    found_jobs = soup.find('li')
    if found_jobs is None:
        print("no ads found")
        return
    else:
        # List of all adds per page.
        # If the titel of the job posting contains a link, then the tag won't be a div
        ads = soup.find_all(['div', 'a'], class_='base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card')
        for ad in ads:
            # If the posting is newly published, it's tag is different
            # DATA NOT NEEDED, DELETE LATER
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


            # DATA NOT NEEDED, DELETE LATER
            #company = ad.find('h4', class_='base-search-card__subtitle').text.strip()


            location = ad.find('span', class_='job-search-card__location').text.strip()
            
            # Removes non swedish ads
            location_country = location.split(", ")[-1]
            if location_country not in ["Sweden", "sweden", "Svergie", "sverige"]:
                continue


            # Depending on if the title contains the link        
            link = ad.find('a', class_='base-card__full-link')
            if link == None:
                link = ad['href']
            else:
                link = link['href']


            # Loads ad page and finds their criterias
            ad_response = requests.get(link)
            ad_soup = BeautifulSoup(ad_response.content,'html.parser')
            
            criteria = ad_soup.find_all('span', 'description__job-criteria-text')

            seniority = criteria[0].text.strip()
            employment_type = criteria[1].text.strip()
            

            
            db.append(["Linkedin", employment_type, "", ad_publication_date, "Job", location.split(',')[1].strip().split()[0], [], date.today().strftime('%Y-%m-%d'), seniority])
            # print()
            # print(ad_title + " | " + company + " | " + location + " | " + ad_date)
            # print(link)   
            time.sleep(1) #Delay to prevent status code 429

    # if page_number < 1000 and len(ads) == 25:
    #     page_number = page_number + 25
    #     time.sleep(3) #Delay to prevent status code 429 (Might be able to lower it)
    #     linkedin_scraper(webpage, page_number)

#DEBUG PRINT, DELETE LATER
linkedin_scraper("https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=&geoId=106710379&start=0", 0)
for data in db:
    print(data)

# for job in jobs:
#     for muni in geo_ids:
#         linkedin_scraper("https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords="+str(job)+"&geoId="+str(muni)+"&start=", 0)
#         print()
#         print()
#         print()
#     for data in db:
#         print(data)