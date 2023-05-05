import requests
import datetime
import logging
import json
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from reqfinder import find_req, find_seniority, find_req_ai
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
    # Retrieves the 10 requested occupations and their ids 
    # [Ingenjör, Utvecklare, Läkare, Sjuksköterska, Lärare, 
    # Operatör, Tekniker, Elektriker, Projektledare, Logistiker]
    occupation_ids = get_occupational_ids()

    # Create an instance of the ads list variable
    all_ads = []

    # Adds every requested job to the list with the help of their occupation_ids
    # The get_ads func can take multiple ids at once, so every id for "ingenjör"
    # is inputed at the same time, same for the 9 other occupations
    for index, occupation in enumerate(occupation_ids):
        occupation_ads = get_ads(occupation)
        all_ads.extend(extract_data_all_ads(occupation_ads, index))

    return all_ads


# Retrieves all ads (with given ids) in full json format
def get_ads(ids):

    # Declare variables
    # OBS: date = amount of days to look back for gathering
    #             data, change 1 to desired days
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


# Takes first duration found
def extract_duration(duration):
    duration = str(duration)
    for char in duration:
        if char.isnumeric():
          return char
    return 0
    

# Creates a list for one ad with correct parameters
def extract_data_ad(ad, index):

    # Dictionary with all occupation names, in order
    # of how they appear in the occupation_ids list in run().
    # It is used to give job ads the same desired name
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
    
    # Extract all desired job descriptions
    ad_id = ad['id']
    employment_type = ad.get('working_hours_type', {}).get('label', ' ')
    duration = extract_duration(ad.get('duration', {}).get('label', ' '))
    publication_date = ad.get('publication_date', ' ')
    occupation = index_dict[index]
    county = ad.get('workplace_address', {}).get('region', ' ') 
    date_extracted = datetime.datetime.today().strftime('%Y-%m-%d')
    description = ad.get('description', {}).get('text', ' ')
    #prereq_ai = find_req_ai(ad_id, occupation, description)
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
            date_extracted,
            ad_id
            ]


# Main script
if __name__ == '__main__':
    run()
