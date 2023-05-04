# All code explicit for webscraping LinkedIn.com
import time
import requests
import traceback
import re
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__))) # Get the directory above
from reqfinder import find_req # Program to look through bodytext
from datetime import date, timedelta
from bs4 import BeautifulSoup, SoupStrainer



# Duplicates counter (REMOVE LATER)
duplicates = 0

# Removed counter
remove_counter = 0

# Keep track of unique adds
seen = {}

# Timer (REMOVE LATER)
start_time = time.time()

# Function to scrape websites
def linkedin_scraper(job, municipality, page_number):   
    next_page = f"https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords={str(job)}&geoId={str(municipality)}&start={str(page_number)}"
    print(next_page)
    # Establish connection
    while(True):
        response = requests.get(str(next_page))
        if(response.status_code == 200):
            break
    soup = BeautifulSoup(response.content,'lxml')

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
            if location_country not in ["Sweden", "Sverige"]:
                continue

            # Get unique identifier for each ad
            key_tag = ad['data-entity-urn']
            key = key_tag.split(':')[-1]

#----------------------------Extracts HTML from each ad-page----------------------------------
            print(job_title + " | " + location)
            seniority = None
            employment_type = None

            # Establish connection to ad-page
            while(True):
                ad_response = requests.get("https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/" + str(key))
                # print(ad_response)
                if(ad_response.status_code == 200 or ad_response.status_code == 500):
                    break
                print("RETRYING")
                time.sleep(0.1) # Delay because of status code 429
            if(ad_response.status_code == 500):
                global remove_counter
                print("SKIP")
                remove_counter = remove_counter + 1
                continue
            
            #Access only part of the HTML file
            strainer = SoupStrainer('section', attrs={'class':'core-section-container my-3 description'})
            ad_soup = BeautifulSoup(ad_response.content,'html.parser', parse_only=strainer)

            #Get HTML element for ad-page
            ad_criterias = ad_soup.find_all('li', class_='description__job-criteria-item')
            ad_description = ad_soup.find('div', 'show-more-less-html__markup').text

            # Look for seniority and employment type
            for item in ad_criterias:
                header = item.find('h3', class_='description__job-criteria-subheader').text.strip()
                # print(header)
                if(header == 'Seniority level'):
                    seniority = item.find('span', class_='description__job-criteria-text--criteria').text.strip()
                if(header == 'Employment type'):
                    employment_type = item.find('span', class_='description__job-criteria-text--criteria').text.strip()
            
            # Look through body text for education
            education = find_req(ad_description)

#----------------------------Saves parameters-------------------------------------------------
            
            employment_type, ad_publication_date, county, seniority = format(employment_type, ad_date, location, seniority)
            temp.append(["linkedin", employment_type, None, ad_publication_date, job, county, education, None, seniority, date.today().strftime('%Y-%m-%d'), key])

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


    if page_number < 975 and len(ads) == 25:
        page_number = page_number + 25
        linkedin_scraper(job, municipality, page_number)
    return(list)



def run():
    start_time = time.time()
    # Database
    db = []

    # Jobs
    jobs = ['lärare']#, 'läkare', 'utvecklare', 'sjuksköterska', 'tekniker', 'operatör', 'elektriker', 'logistiker', 'ingenjör', 'projektledare']

    # Geo ids
    geo_ids = [100564495] 
    # geo_ids = []
    # with open('project\code\linkedIn\geo_ids.txt', 'r') as f:
    #     for line in f:
    #         # Patternmatches for a number with a curly bracket before it and a comma sign after it.
    #         match = re.search(r'\{(\d+)\,', line)
    #         if match:
    #             geo_ids.append(int(match.group(1)))

    #Error handeling
    try:
        for job in jobs:
            for muni in geo_ids:
                data = linkedin_scraper(job, muni, 0)
                db = data + db
            # Reset seen unique adds when changing career
            global seen
            seen = {}

        print("\nSUCCESS")
        print("Duplicates: " + str(duplicates))
        print("Removed jobs: " + str(remove_counter))
    except BaseException as ex:
        # Get current system exception
        ex_type, ex_value, ex_traceback = sys.exc_info()

        # Extract unformatter stack traces as tuples
        trace_back = traceback.extract_tb(ex_traceback)

        # Format stacktrace
        stack_trace = list()

        for trace in trace_back:
            stack_trace.append("File : %s , Line : %d, Func.Name : %s, Message : %s" % (trace[0], trace[1], trace[2], trace[3]))

        print("\nException type : %s " % ex_type.__name__)
        print("Exception message : %s" %ex_value)
        print("Stack trace : %s" %stack_trace)
        print("\nFAILURE")
        print("Crashed while searching: " + db[-1][4] + ", " + db[-1][5])
        # traceback.print_exc()
    
    finally:
        print("Time it took: " + str(time.time()-start_time))
        print("Length of list: " + str(len(db)))

        for l in db:
            print(l)
        return db


# Extracts proper format for db
def format(emp_type, ad_date, location, seniority):

    # Translating employment type and changing it to lowercase
    if emp_type == 'Full-time': emp_type = 'heltid'
    elif emp_type == 'Part-time': emp_type = 'deltid'
    elif emp_type == 'Contract': emp_type = 'kontrakt'
    elif emp_type == 'Temporary': emp_type = 'tillfälligt'
    elif emp_type == 'Internship': emp_type = 'praktikplats'
    elif emp_type == 'Volunteer': emp_type = 'volontär'
    elif emp_type == 'Other': emp_type = 'övrigt'
    else: emp_type = 'null'

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


    # Extracting and translating county while changing it to lowercase
    try:
        county = location[location.index(', ')+2:location.index(' County')]
    except:
        county = location[location.index(', ')+2:location.index(', Sweden')]

    if county == 'Gavleborg': county = 'gävleborg'
    elif county == 'Jamtland': county = 'jämtland'
    elif county == 'Jonkoping': county = 'jonköping'
    elif county == 'Orebro': county = 'örebro'
    elif county == 'Ostergotland': county = 'östergötland'
    elif county == 'Sodermanland': county = 'södermanland'
    elif county == 'Varmland': county = 'värmland'
    elif county == 'Vastmanland': county = 'västmanland'
    elif county == 'Vastra Gotland': county = 'västra vötaland'
    else: county = county.lower()

    if county != 'blekinge' or 'kalmar' or 'skåne' or 'uppsala' or 'örebro':
        county = county + "s län"
    else:
        county = county + " län"


    # Translating seniority and changing it to lowercase
    if seniority == 'Associate': seniority = 'medarbetare'
    elif seniority == 'Director': seniority = 'chef'
    elif seniority == 'Entry level': seniority = 'basnivå'
    elif seniority == 'Executive': seniority = 'verksamhetschef'
    elif seniority == 'Internship': seniority = 'praktikplats'
    elif seniority == 'Mid-Senior level': seniority = 'mellannivå'
    elif seniority == 'Not Applicable': seniority = 'ej tillämpligt'
    else: seniority = 'null'


    return emp_type, ad_publication_date, county, seniority