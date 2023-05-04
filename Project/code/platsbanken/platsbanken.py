import requests
import datetime
import logging
import json
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from reqfinder import find_req, find_seniority
from .get_occupation_id import get_occupational_ids


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
    # Retrieves the 10 occupations and their ids
    print("----before occ-----")
    occupational_ids = get_occupational_ids()
    print("----after occ-----")


    all_ads = []

    # Go through each occupation list of ids and adds them to a list of ads
    for index, occupation in enumerate(occupational_ids):
        occupation_ads = get_ads(occupation)
        all_ads.append(extract_data_all_ads(occupation_ads, index))

    return all_ads


# Retrieves all ads in full
def get_ads(ids):

    # Declare variables
    url = STREAM_URL
    date = datetime.datetime.now() - datetime.timedelta(1)  
    params = {
        'date': date.strftime(DATE_FORMAT),
        'occupation-concept-id': ids
        }

    # Writing log info to the terminal
    log.info(f'Collecting ads from: {url}')

    # Send GET request to JobStream API 
    headers = {'Accept': 'application/json'}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    list_of_ads = json.loads(response.content.decode('utf8'))

    # Log and return
    log.info(f"Got {len(list_of_ads)} ads from {url}")
    return list_of_ads


# Loads all ads into a list with appropiate parameters
def extract_data_all_ads(all_ads, index):
    list = []
    for ad in all_ads:
      list.append(extract_data_ad(ad, index)) 
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
def extract_data_ad(ad, index):

    index_dict = {
        0: "Ingenjör",
        1: "Utvecklare",
        2: "Läkare",
        3: "Sjuksköterska",
        4: "Lärare",
        5: "Operatör",
        6: "Tekniker",
        7: "Elektriker",
        8: "Projektledare",
        9: "Logistiker"
    }
    
    ad_id = ad['id']
    employment_type = ad.get('working_hours_type', {}).get('label', ' ')
    duration = extract_duration(ad.get('duration', {}).get('label', ' '))
    publication_date = ad.get('publication_date', ' ')
    occupation = index_dict[index]
    county = ad.get('workplace_address', {}).get('region', ' ') 
    date_extracted = datetime.datetime.today().strftime('%Y-%m-%d')
    description = ad.get('description', {}).get('text', ' ')
    prereq = find_req(description)
    years = find_seniority(description)

    # Formatting the publication_date from YYYY-MM-DDTHH:MM:SS to YYYY-MM-DD
    publication_date = publication_date[:10]

    # Return
    return ["platsbanken",
            employment_type, 
            duration, 
            publication_date, 
            occupation, 
            county, 
            prereq, 
            years, 
            None, 
            date_extracted]
  

# Main script
if __name__ == '__main__':
    run()
