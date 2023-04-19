import sys
import logging
from settings import LOG_LEVEL, LOG_DATE_FORMAT, LOG_FORMAT


# Logging
log = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=LOG_LEVEL, format=LOG_FORMAT, datefmt=LOG_DATE_FORMAT)


# Loads all ads into a list with appropiate parameters
def load_all(all_ads):
    list = []
    for ad in all_ads:
      list.append(insert_one_ad(ad)) 
    log.debug(f'Insert multiple ads: ({len(all_ads)} ads)')
    print(list[0])
    print(list[500])
    print(list[1000])
    return list


# Creates a list for one ad with correct parameters
def insert_one_ad(ad):
    ad_id = ad['id']
    email = ad.get('application_details', {}).get('email', ' ')
    city = ad.get('workplace_address', {}).get('municipality', ' ')
    occupation = ad.get('occupation', {}).get('label', ' ')
    return [ad_id, email, city, occupation]

