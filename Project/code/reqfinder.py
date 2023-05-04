import re
import requests
import json

# Job ad test variable
job_ad = """
"""
# Sends large description of job ads to AI API,
# which returns skills and experience required based on text
# id, title, and description needs to be string
def find_req_ai(id, title, description):
    # URL of the API 
    url = 'https://jobad-enrichments-api.jobtechdev.se/enrichtextdocumentsbinary'
    
    # Set the headers for POST request 
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    # Set the payload for POST request
    # IMPROVEMENT FOR FUTURE: CAN SEND 100 ADS AT THE SAME TIME INSTEAD OF ONE
    payload = {
    "documents_input": [
        {
          "doc_id": id,
          "doc_headline": title,
          "doc_text": description
        }
        ],
        "add_occupation_concepts": True,
        "add_skill_concepts": True,
        "add_workplace_experience_concepts": True
    }

    # Make the HTTP POST request
    response = requests.post(url, headers=headers, json=payload)

    # Extracts all the 'concept_lablels' (the requirements) from the API response
    data = json.loads(response.text)
    labels = []
    for candidate in data:
        for competency in candidate['enriched_candidates']['competencies']:
            labels.append(competency['concept_label'])
        for trait in candidate['enriched_candidates']['traits']:
            labels.append(trait['concept_label'])
    
    #print(labels)
    return labels



# Define regular expressions for bachelor's, master's, and PhD degrees
def find_req(job_ad):
    # Keywords to be looked for in the text
    bachelors_regex = r"bachelor[\']?s degree"
    bachelors_regexa = r"bachelor[\’]?s degree"
    bachelors_regexm = r"bachelor[\’s]? or master’s degree"
    bachelors_regexma = r"bachelor[\']?s or master's degree"
    bachelors_regexml = r"bachelor or master's degree"
    masters_regex = r"master[\']?s degree"
    masters_regexa = r"master[\’]?s degree"
    phd_regex = r"phd|doctorate"
    degree_regex = r"degree"
    civ_regex = r"civilingenjör"
    civ_regexa = r"civilingenjörsexamen or Civilingenjörsexamen"
    eng_regex = r"högskoleingenjör"
    eng_regexa = r"högskoleingenjörsexamen or Högskoleingenjörsexamen"
    ut_regex = r"utbildning"
    rut_regex = r"relevant utbildning"
    aut_regex = r"akademisk utbildning"
    uut_regex = r"universitetsutbildning"
    u_ut_regex = r"universitets utbildning"
    uni_regex = r"university degree"
    hut_regex = r"högskoleutbildning"
    h_ut_regex = r"högskole utbildning"
    col_regex = r"college degree"

    # Words to replace the found key words
    regex_list = [(bachelors_regex,"kandidatexamen"),
                (bachelors_regexa,"kandidatexamen"),
                (bachelors_regexm,"kandidatexamen"),
                (bachelors_regexma,"kandidatexamen"),
                (bachelors_regexml,"kandidatexamen"),
                (masters_regex,"masterexamen"),
                (masters_regexa,"masterexamen"),
                (phd_regex,"doktorand"),
                (civ_regex,"ingenjör"),
                (civ_regexa,"ingenjör"),
                (eng_regex,"ingenjör"),
                (eng_regexa,"ingenjör"),
                (aut_regex,"akademiskt relevant utbildning"),
                (uni_regex,"högskoleutbildning"),
                (uut_regex,"högskoleutbildning"),
                (u_ut_regex,"högskoleutbildning"),
                (hut_regex,"högskoleutbildning"),
                (h_ut_regex,"högskoleutbildning"),
                (col_regex,"högskoleutbildning"),
                (degree_regex,"kräver relevant utbildning"),
                (ut_regex,"kräver relevant utbildning"),
                (rut_regex,"kräver relevant utbildning"),
                ]


    # Search for degrees using regex keywrods by first lowercasing the text
    for reg in regex_list:
        if re.search(reg[0], job_ad.lower()):
            tbr = [reg[1]]
            break
        else:
            tbr = []

    return tbr


# Define regular expressions for seniority
# First occurrence of string in job ad description matches
def find_seniority(job_ad):
    # Keywords to be looked for in the text
    year_one = r"ett års erfarenhet|1 års erfarenhet|one year of experience|1 year of experience"
    year_two = r"två års erfarenhet|2 års erfarenhet|two years of experience|2 years of experience"
    year_three = r"tre års erfarenhet|3 års erfarenhet|three years of experience|3 years of experience"
    year_four = r"fyra års erfarenhet|4 års erfarenhet|four years of experience|4 years of experience"
    year_five = r"fem års erfarenhet|5 års erfarenhet|five years of experience|5 years of experience"
    year_six = r"sex års erfarenhet|6 års erfarenhet|six years of experience|6 years of experience"
    year_seven = r"sju års erfarenhet|7 års erfarenhet|seven years of experience|7 years of experience"
    year_eight = r"åtta års erfarenhet|8 års erfarenhet|eight years of experience|8 years of experience"
    year_nine = r"nio års erfarenhet|9 års erfarenhete|nine years of experience|9 years of experience"
    year_ten = r"tio års erfarenhet|10 års erfarenhet|ten years of experience|10 years of experience"
    #year_fifteen = r"femton års erfarenhet|15 års erfarenhet"
    #year_twenty = r"tjugo års erfarenhet|20 års erfarenhet"
    year = r"några års erfarenhet|a few years of experience"
    year_several = r"flera års erfarenhet|several years of experience"
    year_par = r"ett par års erfarenhet|a couple of years of experience"
    year_work = r"Arbetslivserfarenhet|arbetslivserfarenhet|Arbetserfarenhet|arbetserfarenhet"

    # Words to replace the found key words
    regex_year = [(year_one, 1),
                (year_two, 2),
                (year_three, 3),
                (year_four, 4),
                (year_five, 5),
                (year_six, 6),
                (year_seven,7),
                (year_eight, 8),
                (year_nine, 9),
                (year_ten, 10),
                #(year_fifteen, 15),
                #(year_twenty, 20),
                (year, 2),
                (year_several, 5),
                (year_par, 2),
                (year_work, 2)
                ]

    # Search for seniority using regex keywords by first lowercasing the text
    for reg in regex_year:
        if re.search(reg[0], job_ad.lower()):
            tbr = reg[1]
            break
        else:
            tbr = None

    return tbr
