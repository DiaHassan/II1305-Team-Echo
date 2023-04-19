import requests
from bs4 import BeautifulSoup
from RequirmentFinder import find_req

print("\n Program is on \n")

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


def join_url(base_url, section):
    return base_url + section


# Returns date
def get_date(response):
    return response.find_all('span', class_='ml-2 text-muted small')[1].text


# Returns prerequiered
def get_prerequiered(response):
    return find_req(response.find('div', class_='mb-1').text)



    
##################################################
# Main function for testing the code
def main():
    response = get_code("https://ledigajobb.se/jobb/a752c9/automationstekniker-till-nytt-omr%C3%A5de-hos-combitech-i-stockholm")
    
    # job_listings = response.find_all('div', class_='col bg-light rounded-bottom pb-2 border-top')
    # temp = job_listings.find('div')
    # print(temp)

    #outer_div = response.find('div', class_='col bg-light rounded-bottom pb-2 border-top').find('div').find('div').find('ul').find_all('li')
    #for i in outer_div:
    #    print(i.text)
    
    # print(outer_div)
    # response = get_code(search_url)
    # temp = create_search_link(9,"utvecklare",3)
    # print(temp)
    # response = get_code(temp)
    # print("\n")
    # print(get_job_links(get_jobs(response)))
    # print("\n")
    # job_listings = get_jobs(response)
    # print("\n")
    # print(get_next_page(response))


if __name__ == '__main__':
    main()
    print("\n")