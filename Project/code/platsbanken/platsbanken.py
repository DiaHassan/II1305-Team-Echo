import requests
import datetime
import logging
import json
import sys
from settings import LOG_LEVEL, LOG_DATE_FORMAT, LOG_FORMAT, DATE_FORMAT, STREAM_URL


# Logging
log = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=LOG_LEVEL, format=LOG_FORMAT, datefmt=LOG_DATE_FORMAT)


# Main function that retrieves all ads and outputs their data in a 2d list
def run():
   # Creates a list with all ads from a specific time to now
   all_ads = get_ads()

   # Creates a 2d list of ads containting sought parameters
   list = extract_data_all_ads(all_ads)
   #print(list[0])
   #print(list[500])
   #print(list[1000])
   flag = True
   i = 0
   while flag:
    if list[i][6] != []:
        break
    i += 1
    
   print(list[i])    

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


# Creates a list for one ad with correct parameters
def extract_data_ad(ad):
    employment_type = ad.get('working_hours_type', {}).get('label', ' ')
    duration = ad.get('duration', {}).get('label', ' ')
    publication_date = ad.get('publication_date', ' ')
    occupation = ad.get('occupation', {}).get('label', ' ')
    county = ad.get('workplace_address', {}).get('region', ' ')

    # Recieve all the experience requirements. 
    experience = []
    experience.append(["experience_required", ad.get('experience_required', ' ')])
    #########   FIXA I FRAMTIDEN    ############
    experience.append(["work_experience", ad.get('must_have', {}).get('work_experiences', ' ').get('label', ' ')])
    #############################################
    experience.append(["education", ad.get('education', ' ')])
    experience.append(["education_level", ad.get('education_level', ' ')])
    experience.append(["skills", ad.get('must_have', {}).get('skills', ' ')])
    experience.append(["language", ad.get('must_have', {}).get('language', ' ')])
    experience.append(["access_to_own_car", ad.get('access_to_own_car', ' ')])
    experience.append(["driving_license_required", ad.get('driving_license_required', ' ')])
    experience.append(["driving_license", ad.get('driving_license', ' ')])

    # seniority
    return ["platsbanken", employment_type, duration, publication_date, occupation, county, experience]
  

# Main script
if __name__ == '__main__':
    run()
