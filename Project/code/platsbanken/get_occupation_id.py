from requests import get
from json import loads
from sys import path
from os.path import dirname
path.append(dirname(dirname(__file__)))
from file_to_list import file_to_list

def get_occupational_ids() -> list:
    url = "https://data.jobtechdev.se/taxonomy/yrkesben%C3%A4mningar.json"
    connection = get(url)

    # Loads the JSON data into a Python dictionary
    data = loads(connection.text)
    tuples = data['data']['concepts']

    jobs = file_to_list('professions.txt')
    all_ids = []

    for job in jobs:
        ids = []
        for tuple in tuples:
            if all(word.lower() in tuple['preferred_label'].lower() for word in job.split()):
                ids.append(tuple['id'])
        if len(ids) > 0:
            all_ids.append(ids)

    return all_ids