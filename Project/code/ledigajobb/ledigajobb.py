# Imports
from requests import get
from bs4 import BeautifulSoup

# Imports for paths
from os import path as os_path
from sys import platform, path as sys_path
sys_path.append(os_path.dirname(os_path.dirname(__file__)))
from reqfinder import find_req

# Import counties
try:
    from ledigajobb_counties import counties
except ImportError:
    from .ledigajobb_counties import counties


# Retrieves list of all professions to webscrape
def get_profession_list():
    s = '/' if (platform == 'linux' or platform =='darwin') else '\\'
    file = os_path.dirname(os_path.dirname(os_path.dirname(__file__))) + s + 'professions.txt'
    return open(file, encoding='utf-8').read().splitlines()


# Define the URL to scrape
base_url = 'https://ledigajobb.se'
search_url = 'https://ledigajobb.se/sok?'


# Send a GET request to get the HTML response and parse it
def get_code(url):
    try:
        response = get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup
    except:
        return "No data"


# Find all the job listings on the page
def get_jobs(response):
    job_listings = response.find_all('div', {'class': 'posting-title'})
    return job_listings


# Get all jobs
def get_job_links(job_listings):
    # Loop through each job listing and print the job title and company name
    job_links = []
    for job in job_listings:
        job_links.append(job.find('a').get("href"))
    return job_links
        

# Get the link to the next page
def get_next_page(response):
    try:
        next_btn_link = response.find('a', {'class': 'page-link', 'aria-label': 'Next'}).get("href")
        return base_url + next_btn_link 
    except:
        return False


# Creates link to initiate search 
def create_search_link(lan, work, page):
    new_string = f"https://ledigajobb.se/sok?cc={lan}&s={work}&p={page}"
    return new_string


# Replacing the index of the link to get to the next page
def replace_after(my_string, to_replace, replacement):
    index = my_string.find(to_replace) + len(to_replace)
    new_string = my_string[:index] + replacement + my_string[index+1:]


# Joins url to build link to job ad
def join_url(base_url, section):
    return base_url + section


# Returns date
def get_date(response):
    try:
        return response.find_all('span', class_='ml-2 text-muted small')[1].text
    except:
        return "None"


# Returns prerequiered
def get_prerequiered(response):
    try:
        return find_req(response.find('div', class_='mb-1').text)
    except: 
        return 'None'
  


# Returns employment type, duration, and seniority
def get_profession_details(response):
    try:
        # Result and path
        info=[]
        outer_div = response.find('div', class_='col bg-light rounded-bottom pb-2 border-top').find('div').find('div').find('ul').find_all('li')

        # Initial fill
        for i in outer_div:
            info.append(i.text)
        
        if(len(info) == 3):
            #Sorting the scrapped information
            info[0] = info[0].lower()
            if(info[1] == "Tillsvidare"):
                info[1] = 0
            elif(info[1] == "3 - 6 Månader"):
                info[1] = 3
            elif(info[1] == "6 Månader eller längre"):
                info[1] = 6
            elif(info[1] == "11 Dagar - 3 Månader"):
                info[1] = 2
            elif(info[1] == "Max 10 dagar"):
                info[1] = 1
            else:
                info[1] = 0 
            info[2] = info[2].strip().split()

            try:
                info[2] = info[2][0] + ' ' +info[2][1]
            except:
                info[2] = info[2][0]
        else:
            info[0] = "övrigt"
            info.append("None")
            info.append("None")

        return info
    except:
        return [None,None,None]


# Find lan
def find_county(county_nb):
    for county in counties:
        if (county_nb == county[0]):
            return county[1]



# Scrape all required details from the ad
def scrape_ad(job_link, county, profession):
    # Init
    job_code = get_code(job_link)
    work_details = get_profession_details(job_code)

    # Data
    source = "ledigajobb"
    employment_type = work_details[0]
    duration = work_details[1]
    publication_date = get_date(job_code)
    profession = profession
    county = find_county(county)
    prerequierment = get_prerequiered(job_code)
    #seniority = work_details[2]

    return [source, 
            employment_type, 
            duration, 
            publication_date, 
            profession, 
            county, 
            prerequierment, 
            0,
            None,
            "2023-04-20"
            ]


# Get all info using all parameters
def run():
    i = 0
    n = 0
    all_jobs = []
    professions = get_profession_list()
    # Going through all jobs and locations
    for profession in professions:
        for county_index in range(2,21):
            next_page = True
            response = get_code(create_search_link(county_index, profession, 1))
            # Looping through and printing out each page
            while next_page:
                if(next_page == "Twees"): break
                try:
                    job_links = get_job_links(get_jobs(response))
                except:
                    try:
                        n += 1 
                        print("\n N is vvvvvv")
                        print(n) 
                        next_page = get_next_page(response)
                        if (next_page == False): next_page = "Twees"
                        response = get_code(next_page)
                        continue
                    except: continue
                # Gets all the sub links then to joing them with the base url and 
                for half_link in job_links:
                    i += 1
                    print("\n I is vvvvvv")
                    print(i) 
                    all_jobs.append(scrape_ad(base_url+half_link,county_index, profession))
                next_page = get_next_page(response)
                if (next_page == False): next_page = "Twees"
                response = get_code(next_page)
    return all_jobs      


if __name__ == '__main__':
    run()
    print("\n")