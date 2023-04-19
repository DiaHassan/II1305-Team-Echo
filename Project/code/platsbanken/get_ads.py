import sys
import json
import logging
import requests
import datetime
from settings import LOG_LEVEL, LOG_DATE_FORMAT, LOG_FORMAT, DATE_FORMAT, STREAM_URL, PLACES, OCCUPATIONS


# Logging
log = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=LOG_LEVEL, format=LOG_FORMAT, datefmt=LOG_DATE_FORMAT)


# For bootstrap.py
date = 0


# Retrieves all ads in full
def get_ads():

    # Declare variables
    url = STREAM_URL
    date = datetime.datetime.now() - datetime.timedelta(8)
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