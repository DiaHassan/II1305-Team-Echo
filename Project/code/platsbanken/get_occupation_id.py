import requests
import json
from os import path
from sys import platform

# Retrieves list of all professions to webscrape
def get_professions():
    s = '/' if (platform == 'linux' or platform =='darwin') else '\\'
    file = path.dirname(path.dirname(path.dirname(__file__))) + s + 'professions.txt'
    return open(file, encoding='utf-8').read().splitlines()

def get_occupational_ids():
    url = "https://data.jobtechdev.se/taxonomy/yrkesben%C3%A4mningar.json"
    connection = requests.get(url)

    # Loads the JSON data into a Python dictionary
    data = json.loads(connection.text)
    tuples = data['data']['concepts']

    jobs = get_professions()
    all_ids = []

    for job in jobs:
        ids = []
        for tuple in tuples:
            if all(word.lower() in tuple['preferred_label'].lower() for word in job.split()):
                ids.append(tuple['id'])
        if len(ids) > 0:
            all_ids.append(ids)

    return all_ids