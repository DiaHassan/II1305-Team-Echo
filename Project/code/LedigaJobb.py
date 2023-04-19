import requests
from bs4 import BeautifulSoup
from RequirmentFinder import find_req


# Define the URL to scrape
base_url = 'https://ledigajobb.se'
search_url = 'https://ledigajobb.se/sok?'


# Send a GET request to get the HTML response and parse it
def get_code(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup


# Find all the job listings on the page
def get_jobs(response):
    job_listings = response.find_all('div', {'class': 'posting-title'})
    return job_listings


# Get all jobs
def get_job_links(job_listings):
    # Loop through each job listing and print the job title and company name
    for job in job_listings:
        job_link = job.find('a').get("href")
        # print(job_link)


# Get the link to the next page
def get_next_page(response):
    next_btn_link = response.find('a', {'class': 'page-link', 'aria-label': 'Next'}).get("href")
    return next_btn_link


# Creates link to initiate search 
def create_search_link(lan, work, page):
    new_string = f"https://ledigajobb.se/sok?cc={lan}&s={work}&p={page}"
    return new_string


# Replacing the index of the link to get to the next page
def replace_after(my_string, to_replace, replacement):
    index = my_string.find(to_replace) + len(to_replace)
    new_string = my_string[:index] + replacement + my_string[index+1:]
    # print(new_string) 


# Joins url to build link to job ad
def join_url(base_url, section):
    return base_url + section


# Returns date
def get_date(response):
    return response.find_all('span', class_='ml-2 text-muted small')[1].text


# Returns prerequiered
def get_prerequiered(response):
    return find_req(response.find('div', class_='mb-1').text)


# Returns employment type, duration, and seniority
def get_work_details(response):
    # Result and path
    info=[]
    outer_div = response.find('div', class_='col bg-light rounded-bottom pb-2 border-top').find('div').find('div').find('ul').find_all('li')

    # Initial fill
    for i in outer_div:
        info.append(i.text.strip().split())

    # Array Clean
    info[0] = info[0][0]
    info[1] = info[1][0]
    info[2] = info[2][0] + ' ' +info[2][1]

    return info


# Run from 
def run():
    print("")


def scrape_ad(job_link):
    # Init
    job_code = get_code(job_link)
    work_details = get_work_details(job_code)
    result = []

    # Data
    source = "ledigajobb"
    employment_type = work_details[0]
    duration = work_details[1]
    publication_date = get_date(job_code)
    profession = ""  # need list of jobs
    county = ""  # need function for converting id to län
    prerequierment = get_prerequiered(job_code)
    seniority = work_details[2]

    return [source, 
            employment_type, 
            duration, 
            publication_date, 
            profession, 
            county, 
            prerequierment, 
            seniority]


    

    
##################################################
# Main function for testing the code
def main():
    response = get_code("https://ledigajobb.se/jobb/a4c766/trainee-backend-utvecklare")
    
    print(scrape_ad("https://ledigajobb.se/jobb/a7ed79/nynas-s%C3%B6ker-tv%C3%A5-processingenj%C3%B6rer-omg%C3%A5ende"))


if __name__ == '__main__':
    main()
    print("\n")