import requests
from bs4 import BeautifulSoup

print("\n Program is on \n")

# Define the URL to scrape
base_url = 'https://ledigajobb.se'
search_url = 'https://ledigajobb.se/sok?'


# Send a GET request to get the HTML response and parse it
def get_code(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

def get_jobs(response):
    # Find all the job listings on the page
    job_listings = response.find_all('div', {'class': 'posting-title'})
    return job_listings

# Get all jobs
def get_job_links(job_listings):
    # Loop through each job listing and print the job title and company name
    for job in job_listings:
        job_link = job.find('a').get("href")
        print(job_link)

def get_next_page(response):
    next_btn_link = response.find('a', {'class': 'page-link', 'aria-label': 'Next'}).get("href")
    return next_btn_link

# Main function for testing the code
def main():
    response = get_code(search_url)
    job_listings = get_jobs(response)
    print(get_next_page(response))


if __name__ == '__main__':
    main()
    print("\n")