import sys
import json
import logging
import requests
import datetime

from settings import LOG_LEVEL, LOG_DATE_FORMAT, LOG_FORMAT, DATE_FORMAT, STREAM_URL, PLACES, OCCUPATIONS

log = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=LOG_LEVEL, format=LOG_FORMAT, datefmt=LOG_DATE_FORMAT)

# Main method updating the list of job ads
def get_ads():
    url = STREAM_URL
    date = datetime.datetime.now() - datetime.timedelta(1)
    params = {'date': date.strftime(DATE_FORMAT)}
    if PLACES:
        params['location-concept-id'] = PLACES
    if OCCUPATIONS:
        params['occupation-concept-id'] = OCCUPATIONS

    log.info(f'Collecting ads from: {url} with params {params}')
    headers = {'Accept': 'application/json'}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    list_of_ads = json.loads(response.content.decode('utf8'))
    log.info(f"Got {len(list_of_ads)} ads from {url}. Params: {params}")

    return list_of_ads