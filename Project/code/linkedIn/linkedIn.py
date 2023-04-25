# All code explicit for webscraping LinkedIn.com
import time
import requests
import re
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__))) # Get the directory above
from reqfinder import find_req
from urllib.parse import urlparse, parse_qs #parses url
from datetime import date, timedelta
from bs4 import BeautifulSoup

# Duplicates counter (REMOVE LATER)
duplicates = 0

# Timer (REMOVE LATER)
start_time = time.time()

# Function to scrape websites
def linkedin_scraper(job, municipality, page_number):
    try:     
        url1 = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords="     
        url2 = "&geoId="     
        url3 = "&start="     
        next_page = url1 + str(job) + url2 + str(municipality) + url3 + str(page_number)
        print(str(next_page))
        response = requests.get(str(next_page))
        soup = BeautifulSoup(response.content,'html.parser')

        # temp list for every ad per proffesion per municipality
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
                # If the posting is newly published, its tag is different
                # DATA NOT NEEDED, DELETE LATER
                job_title = ad.find('h3', class_='base-search-card__title')
                if job_title == None:
                    job_title = ad.find('h3', class_='base-search-card__title--new').text.strip()
                else:
                    job_title = job_title.text.strip()


                # If the posting is newly published, its tag is different
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
                
                # Removes non-Swedish ads
                location_country = location.split(", ")[-1]
                if location_country not in ["Sweden", "sweden", "Sverige", "sverige"]:
                    continue


                # Depending on if the title contains the link        
                link = ad.find('a', class_='base-card__full-link')
                if link == None:
                    link = ad['href']
                else:
                    link = link['href']

                # Get unique key for each ad
                parsed_url = urlparse(link)
                query_params = parse_qs(parsed_url.query)
                key = query_params.get('trackingId', [None])[0]

                # Loads ad page and finds their criterias
                ad_response = requests.get(link)
                ad_soup = BeautifulSoup(ad_response.content,'html.parser')
                
                # DELETE LATER, TEST
                # ad_description = ad_soup.find('div', 'show-more-less-html__markup')
                # if ad_description == None:
                #     if ad_soup.find('p', 'authwall-join-form__swap-cta') != None:
                #         print("FUUUUUUUCK")
                #         break
                #     else:
                #         print("Try again")
                # criteria = ad_soup.find_all('li', class_='description__job-criteria-item')
                
                while(True):
                    ad_response = requests.get(link)
                    ad_soup = BeautifulSoup(ad_response.content,'html.parser')
                
                    criteria = ad_soup.find_all('li', class_='description__job-criteria-item')
                    ad_description = ad_soup.find('div', 'show-more-less-html__markup')
                    if(ad_description is not None):
                        break
                    print("RETRYING")
                    
                ad_description = ad_description.text
                seniority = None
                employment_type = None

                # Check if ad has these criterias
                for item in criteria:
                    header = item.find('h3', class_='description__job-criteria-subheader').text.strip()
                    
                    if(header == 'Yrkesnivå'):
                        seniority = item.find('span', class_='description__job-criteria-text--criteria').text.strip()
                    if(header == 'Anställningstyp'):
                        employment_type = item.find('span', class_='description__job-criteria-text--criteria').text.strip()

                education = find_req(ad_description)

                print(job_title + " | " + location )
                temp.append(["Linkedin", employment_type, None, ad_publication_date, job, location.split(',')[1].strip().split()[0], education, None, date.today().strftime('%Y-%m-%d'), seniority, key])  
                
                time.sleep(1) #Delay to prevent status code 429

        if page_number < 1000 and len(ads) == 25:
            page_number = page_number + 25
            linkedin_scraper(job, municipality, page_number)

        # for l in temp:
        #     print(l)


        #Remove duplicates and the key element 
        seen = {}
        list = []
        for item in temp:
            identifier = item[-1]
            if identifier not in seen:
                seen[identifier] = True
                list.append(item[:-1])
            else:
                global duplicates
                duplicates = duplicates + 1

        print(duplicates)
        return(list)
    except:
        print()
        print("Time it took: " + str(time.time()-start_time))
        print("Fail")
        print("Duplicates: " + str(duplicates))


def run():
    start_time = time.time()
    # Database
    db = []

    # Jobs
    jobs = ["Lärare", "Läkare", "Utvecklare", "Sjuksköterska", "Kock", "Operatör", "Personlig assistent", "Mekaniker", "Butikssäljare", "Civilingenjör", "Projektledare", "Städare"]

    # Geo ids
    # geo_ids = [100937224] 
    geo_ids = []
    with open('geo_ids.txt', 'r') as f:
        for line in f:
            # Patternmatches for a number with a curly bracket before it and a comma sign after it.
            match = re.search(r'\{(\d+)\,', line)
            if match:
                geo_ids.append(int(match.group(1)))

    for job in jobs:
        for muni in geo_ids:
            data = linkedin_scraper(job, muni, 0)
            # print("DATA")
            # print(data)
            # print()
            # print("DB")
            # print(db)
            db = data + db

    for entries in db:
        print(entries)
    print("Time it took: " + str(time.time()-start_time))
    print("Success")
    print("Duplicates: " + str(duplicates))
    # return db

#DEBUG PRINT, DELETE LATER
# linkedin_scraper("https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=&geoId=106710379&start=0", 0)
# for data in db:
#     print(data)

# for job in jobs:
#     for muni in geo_ids:
#         linkedin_scraper("https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords="+str(job)+"&geoId="+str(muni)+"&start=", 0)
#         print()
#         print()
#         print()
#     for data in db:
#         print(data)