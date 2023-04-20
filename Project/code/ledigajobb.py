import requests
from bs4 import BeautifulSoup
from requirementfinder import find_req
from job_lan import lan_list, yrke_list

# Define the URL to scrape
base_url = 'https://ledigajobb.se'
search_url = 'https://ledigajobb.se/sok?'


# Send a GET request to get the HTML response and parse it
def get_code(url):
    try:
        response = requests.get(url)
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
        return next_btn_link 
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
        info.append(i.text)

    # Array Clean

    info[2] = info[2].strip().split()
    info[2] = info[2][0] + ' ' +info[2][1]

    return info


# Find lan
def find_lan(lan_nb):
    for lan in lan_list:
        if (lan_nb == lan[0]):
            return lan[1]


# Run from 
def run():
    print("")


def scrape_ad(job_link,lan,work):
    # Init
    job_code = get_code(job_link)
    work_details = get_work_details(job_code)
    result = []

    # Data
    source = "ledigajobb"
    employment_type = work_details[0]
    duration = work_details[1]
    publication_date = get_date(job_code)
    profession = work
    county = find_lan(lan)
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


def get_all():
    for work in yrke_list:
        for lan in lan_list:
            next_page = True
            response = get_code(create_search_link(lan,work,1))
            while next_page:
                if(next_page == "Twees"): break
                job_links = get_job_links(get_jobs(response))
                for half_link in job_links:
                    print(scrape_ad(base_url+half_link,lan, work))
                next_page = get_next_page(response)
                if (next_page == False): next_page = "Twees"
                response = get_code(next_page)
            
    return [1][2]

    

    
##################################################
# Main function for testing the code
def main():
    # response = get_code("https://ledigajobb.se/jobb/a4c766/trainee-backend-utvecklare")
    
    #print(scrape_ad("https://ledigajobb.se/jobb/a7ed79/nynas-s%C3%B6ker-tv%C3%A5-processingenj%C3%B6rer-omg%C3%A5ende"))
    # print(yrke_list)
    # get_all("link")

    # job_links = get_job_links(get_jobs(get_code(create_search_link(15,"lärare",1))))
    # print(job_links)
    # print(get_next_page(get_code("https://ledigajobb.se/sok?cc=15&s=l%C3%A4rare&p=2")))

    next_page = True
    response = get_code(create_search_link(15,"lärare",1))
    while next_page:
        if(next_page == "Twees"): break
        job_links = get_job_links(get_jobs(response))
        for half_link in job_links:
            print(scrape_ad(base_url+half_link,15,"lärare"))
        next_page = get_next_page(response)
        if (next_page == False): next_page = "Twees"
        response = get_code(base_url+next_page)

if __name__ == '__main__':
    main()
    print("\n")