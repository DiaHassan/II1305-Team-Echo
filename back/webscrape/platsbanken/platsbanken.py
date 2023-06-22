# Imports
from requests import get
from datetime import datetime, timedelta
from logging import INFO, getLogger, basicConfig
from json import loads

# Requirement finder
from sys import stdout, path
from os.path import dirname
path.append(dirname(dirname(__file__)))
from reqfinder import find_req, find_seniority, find_req_ai
from file_to_list import file_to_list

# Occupation ID
try:
    from .get_occupation_id import get_occupational_ids
except ImportError:
    from get_occupation_id import get_occupational_ids

# URL and format for settings
BASE_URL = 'https://jobstream.api.jobtechdev.se'
STREAM_URL = f"{BASE_URL}/stream"
DATE_FORMAT = "%Y-%m-%dT%H:%M:%S"

# Logging for settings
LOG_LEVEL = INFO  # Change INFO to DEBUG for verbose logging
LOG_FORMAT = '%(asctime)s  %(levelname)-8s %(message)s'
LOG_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

# Logging for termnial
log = getLogger(__name__)
basicConfig(stream=stdout, level=LOG_LEVEL, format=LOG_FORMAT, datefmt=LOG_DATE_FORMAT)

# Dictionary with all occupation names, in order
# of how they appear in the occupation_ids list in run().
# It is used to give job ads the same desired name
professions = file_to_list('professions.txt')
index_dict = {index: value for index, value in enumerate(professions)}

# Main function that retrieves all ads and outputs their data in a 2d list
def run() -> list:
    # Retrieves the 10 requested occupations and their ids 
    occupation_ids = get_occupational_ids()

    # Create an instance of the ads list variable
    all_ads = []

    # Adds every requested job to the list with the help of their occupation_ids
    # The get_ads func can take multiple ids at once, so every id for "ingenjör"
    # is inputed at the same time, same for the 9 other occupations
    for index, occupation in enumerate(occupation_ids):
        occupation_ads = get_ads(occupation, index)
        all_ads.extend(extract_data_all_ads(occupation_ads, index))

    # Removes ads with "null" as county
    valid_ads = remove_void_ads(all_ads)

    return valid_ads

# Retrieves all ads (with given ids) in full json format
def get_ads(ids: list, index: int) -> list:

    # Declare variables
    # OBS: date = amount of days to look back 
    # for gathering data, change 1 to desired days
    url = STREAM_URL
    date = datetime.now() - timedelta(30)  
    params = {
        'date': date.strftime(DATE_FORMAT),
        'occupation-concept-id': ids
        }

    # Writing log info to the terminal
    log.info(f'Collecting ads from: {index_dict[index]}')

    # Send GET request to JobStream API 
    headers = {'Accept': 'application/json'}
    response = get(url, headers=headers, params=params)
    response.raise_for_status()
    list_of_ads = loads(response.content.decode('utf8'))

    # Log and return
    log.info(f"----> Received {len(list_of_ads)}")
    return list_of_ads


# Removes ads with "null" value in given field
def remove_void_ads(ads: list) -> list:
    initial_length = len(ads)
    valid_ads = []
    for ad in ads:
        if ad[5] != 'null':
            valid_ads.append(ad)
    log.info(f"Removed {initial_length - len(valid_ads)} ads out of {initial_length}")
    return valid_ads


# Loads all ads into a list with appropiate parameters
def extract_data_all_ads(all_ads: list, index: int) -> list:
    list = []
    for ad in all_ads:
      list.append(extract_data_ad(ad, index)) 
    log.debug(f'Insert multiple ads: ({len(all_ads)} ads)')
    return list


# Takes first duration found
def extract_duration(duration: str) -> (str | int):
    duration = str(duration)
    if duration.lower() == 'tills vidare' or duration == 'tillsvidare':
        return '0'
    # Gives 'tillsvidare' the value 0
    for char in duration:
        if char.isnumeric():
          return char
    return 'null'

# Creates a list for one ad with correct parameters
def extract_data_ad(ad: list, index: int) -> list:
    # Extract all desired job descriptions
    employment_type = ad.get('working_hours_type', {}).get('label') or 'null'
    duration = extract_duration(ad.get('duration', {}).get('label')) or 'null'
    publication_date = ad.get('publication_date', "null") or 'null'
    occupation = index_dict[index]
    county = ad.get('workplace_address', {}).get('region') or 'null'
    date_extracted = datetime.today().strftime('%Y-%m-%d')
    description_list = ad.get('description', {}).get('text') or 'null'
    description = ''.join(description_list) if isinstance(description_list, list) else description_list
    prereq = find_req(description)
    years = find_seniority(description)

    if employment_type is not None:
        employment_type= employment_type.lower()
    if county is not None:
        county = county.lower()

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
            'null', 
            date_extracted
            ]


# Main script
if __name__ == '__main__':
    run()
