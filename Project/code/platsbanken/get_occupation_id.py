import codecs      #swedish alphabet
import requests
import json

def return_ids():
    url = "https://data.jobtechdev.se/taxonomy/yrkesben%C3%A4mningar.json"
    connection = requests.get(url)

    # Loads the JSON data into a Python dictionary
    data = json.loads(connection.text)
    tuples = data['data']['concepts']

    jobs = ["Ingenjör", "Utvecklare", "Läkare", "Sjuksköterska", "Lärare", "Operatör", "Tekniker", "Elektriker", "Projektledare", "Logistiker"]
    all_ids = []

    for job in jobs:
        ids = []
        for tuple in tuples:
            if all(word.lower() in tuple['preferred_label'].lower() for word in job.split()):
                ids.append(tuple['id'])
        if len(ids) > 0:
            all_ids.append(ids)

    return all_ids