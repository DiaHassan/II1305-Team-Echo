import requests
import datetime
import logging
import json
import sys
import os
from reqfinder import find_req, find_seniority
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
  
# URL and format for settings
BASE_URL = 'https://jobstream.api.jobtechdev.se'
STREAM_URL = f"{BASE_URL}/stream"
DATE_FORMAT = "%Y-%m-%dT%H:%M:%S"


# Logging for settings
LOG_LEVEL = logging.INFO  # Change INFO to DEBUG for verbose logging
LOG_FORMAT = '%(asctime)s  %(levelname)-8s %(message)s'
LOG_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

# Logging for termnial
log = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=LOG_LEVEL, format=LOG_FORMAT, datefmt=LOG_DATE_FORMAT)


# Main function that retrieves all ads and outputs their data in a 2d list
def run():
   # Creates a list with all ads from a specific time to now
   all_ads = get_ads()

   # Creates a 2d list of ads containting sought parameters
   list = extract_data_all_ads(all_ads)
   print(list[0])
   print(list[500])
   print(list[1000])  
   return list


# Retrieves all ads in full
def get_ads():
    # Declare variables
    url = STREAM_URL
    date = datetime.datetime.now() - datetime.timedelta(1)  # test, timedelta parameter is days and should be 30
    params = {'date': date.strftime(DATE_FORMAT)}

    # Writing log info to the terminal
    log.info(f'Collecting ads from: {url} with params {params}')

    # Send GET request to JobStream API 
    headers = {'Accept': 'application/json'}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    list_of_ads = json.loads(response.content.decode('utf8'))

    # Log and return
    log.info(f"Got {len(list_of_ads)} ads from {url}. Params: {params}")
    return list_of_ads


# Loads all ads into a list with appropiate parameters
def extract_data_all_ads(all_ads):
    list = []
    for ad in all_ads:
      list.append(extract_data_ad(ad)) 
    log.debug(f'Insert multiple ads: ({len(all_ads)} ads)')
    return list


# Takes first 
def extract_duration(duration):
    duration = str(duration)
    for char in duration:
        if char.isnumeric():
          return char
    return 0
    

# Creates a list for one ad with correct parameters
def extract_data_ad(ad):
    prereq = []
    employment_type = ad.get('working_hours_type', {}).get('label', ' ')
    duration = extract_duration(ad.get('duration', {}).get('label', ' '))
    publication_date = ad.get('publication_date', ' ')
    occupation_group = ad.get('occupation_group', {}).get('label', ' ')
    county = ad.get('workplace_address', {}).get('region', ' ') 
    date_extracted = datetime.datetime.today().strftime('%Y-%m-%d')
    description = ad.get('description', {}).get('text', ' ')
    education = find_req(description)

    experience = ad.get('experience_required', ' ')
    years = ""

    if experience:
        years = find_seniority(description)
        if years == "Not specified":
            years = None

    if education == "Not specified":
        prereq.append(None)
    else:
        prereq.append(education)
    
    # Formatting the publication_date from YYYY-MM-DDTHH:MM:SS to YYYY-MM-DD
    publication_date = publication_date[:10]

    # seniority
    return ["platsbanken", employment_type, duration, publication_date, occupation_group, county, prereq, years, None, date_extracted]
  

# Main script
if __name__ == '__main__':
    run()
