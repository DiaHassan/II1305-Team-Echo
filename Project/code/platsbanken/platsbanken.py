import requests
import datetime
import logging
import json
import sys
from settings import LOG_LEVEL, LOG_DATE_FORMAT, LOG_FORMAT, DATE_FORMAT, STREAM_URL


# Logging
log = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=LOG_LEVEL, format=LOG_FORMAT, datefmt=LOG_DATE_FORMAT)


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
    print(list[0]) # test
    print(list[500]) # test
    print(list[1000]) # test
    return list


# Creates a list for one ad with correct parameters
def extract_data_ad(ad):
    ad_id = ad['id']
    email = ad.get('application_details', {}).get('email', ' ')
    city = ad.get('workplace_address', {}).get('municipality', ' ')
    occupation = ad.get('occupation', {}).get('label', ' ')
    return [ad_id, email, city, occupation]


# Main script
if __name__ == '__main__':

    # Creates a list with all ads from a specific time to now
    all_ads = get_ads()

    # Creates a 2d list of ads containting sought parameters
    list = extract_data_all_ads(all_ads)
