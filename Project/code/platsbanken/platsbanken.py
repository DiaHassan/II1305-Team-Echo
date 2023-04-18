import sys
import logging
import datetime
import requests
import json
from settings import LOG_LEVEL, LOG_DATE_FORMAT, LOG_FORMAT, DB_TABLE_NAME, STREAM_URL, DATE_FORMAT, PLACES, OCCUPATIONS


# Log
log = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=LOG_LEVEL, format=LOG_FORMAT, datefmt=LOG_DATE_FORMAT)


# Global variable for timestamp
date = 0


# Retrieves all ads in full
def get_ads():

    # Declare variables
    url = STREAM_URL
    date = datetime.datetime.now() - datetime.timedelta(1)
    params = {'date': date.strftime(DATE_FORMAT)}

    # If the search query requires PLACE or OCCUPATION ()
    if PLACES:
        params['location-concept-id'] = PLACES
    if OCCUPATIONS:
        params['occupation-concept-id'] = OCCUPATIONS

    # Writing log info to the terminal
    log.info(f'Collecting ads from: {url} with params {params}')

    # Send GET request to JobStream API 
    headers = {'Accept': 'application/json'}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    list_of_ads = json.loads(response.content.decode('utf8'))
    log.info(f"Got {len(list_of_ads)} ads from {url}. Params: {params}")

    return list_of_ads


# Loads all ads into a list with appropiate parameters
def load_all(all_ads):
    list = []
    count = 0  # dumb
    for ad in all_ads:
      if count>10: break  # dumb
      list.append(insert_one_ad(ad)) 
      count+=1  # dumb
    log.debug(f'Insert multiple ads: ({len(all_ads)} ads)')
    print(list)
    return list


# Creates a list for one ad with correct parameters
def insert_one_ad(ad):
    ad_id = ad['id']
    email = ad.get('application_details', {}).get('email', ' ')
    city = ad.get('workplace_address', {}).get('municipality', ' ')
    occupation = ad.get('occupation', {}).get('label', ' ')
    return [ad_id, email, city, occupation]


# Main script
if __name__ == '__main__':

    all_ads = get_ads()
    load_all(all_ads)
    log.info(f'Loaded {len(all_ads)} into the database table "{DB_TABLE_NAME}". Timestamp: {date}')