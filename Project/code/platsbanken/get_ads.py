import sys
import json
import logging
import requests

from settings import LOG_LEVEL, LOG_DATE_FORMAT, LOG_FORMAT, STREAM_URL, SNAPSHOT_URL, PLACES, OCCUPATIONS

log = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=LOG_LEVEL, format=LOG_FORMAT, datefmt=LOG_DATE_FORMAT)

# Main method updating the list of job ads
def _get(url, params={}):
    log.info(f'Collecting ads from: {url} with params {params}')
    headers = {'Accept': 'application/json'}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    list_of_ads = json.loads(response.content.decode('utf8'))
    log.info(f"Got {len(list_of_ads)} ads from {url}. Params: {params}")
    return list_of_ads

# Uses the snapshot function in the API to download all active ads
def get_all_ads():
    return _get(SNAPSHOT_URL)

# Utilizes the stream function from JobStream API to update new job listings
def get_ads_since_time(timestamp):
    params = {'date': timestamp}
    if PLACES:
        params['location-concept-id'] = PLACES
    if OCCUPATIONS:
        params['occupation-concept-id'] = OCCUPATIONS
    return _get(STREAM_URL, params)
