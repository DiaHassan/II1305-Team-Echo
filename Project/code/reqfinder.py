import re

# Job ad test variable
job_ad = """


"""

#högskoleutbildning
#civilingenjörsexamen

# Define regular expressions for bachelor's, master's, and PhD degrees
def find_req(job_ad):
    #Keywords to be looked for in the text
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
    eng_regex = r"högskoleingenjör"
    ut_regex = r"utbildning"
    rut_regex = r"relevant utbildning"
    aut_regex = r"akademisk utbildning"
    uut_regex = r"universitetsutbildning"
    u_ut_regex = r"universitets utbildning"
    uni_regex = r"university degree"

    #Words to replace the found key words
    regex_list = [(bachelors_regex,"Bachelor's degree"),
                (bachelors_regexa,"Bachelor's degree"),
                (bachelors_regexm,"Bachelor's degree"),
                (bachelors_regexma,"Bachelor's degree"),
                (bachelors_regexml,"Bachelor's degree"),
                (masters_regex,"Master's degree"),
                (masters_regexa,"Master's degree"),
                (phd_regex,"PhD"),
                (civ_regex,"Engineer"),
                (eng_regex,"Engineer"),
                (aut_regex,"Academic relevant degree"),
                (uni_regex,"University degree"),
                (uut_regex,"University degree"),
                (u_ut_regex,"University degree"),
                (degree_regex,"Requires a relevant degree"),
                (ut_regex,"Requires a relevant degree"),
                (rut_regex,"Requires a relevant degree"),
                ]


    # Search for degrees using regex keywrods by first lowercasing the text
    for reg in regex_list:
        if re.search(reg[0], job_ad.lower()):
            tbr = reg[1]
            break
        else:
            tbr= None

    return tbr


# Define regular expressions for seniority
def find_seniority(job_ad):
    #Keywords to be looked for in the text
    year_one = r"ett års erfarenhet | 1 års erfarenhet"
    year_two = r"två års erfarenhet | 2 års erfarenhet"
    year_three = r"tre års erfarenhet | 3 års erfarenhet"
    year_four = r"fyra års erfarenhet | 4 års erfarenhet"
    year_five = r"fem års erfarenhet | 5 års erfarenhet"
    year_six = r"sex års erfarenhet | 6 års erfarenhet"
    year_seven = r"sju års erfarenhet | 7 års erfarenhet"
    year_eight = r"åtta års erfarenhet | 8 års erfarenhet"
    year_nine = r"nio års erfarenhet | 9 års erfarenhet"
    year_ten = r"tio års erfarenhet | 10 års erfarenhet"
    year_fifteen = r"femton års erfarenhet | 15 års erfarenhet"
    year_twenty = r"tjugo års erfarenhet | 20 års erfarenhet"
    year = r"några års erfarenhet"

    # TODO: year_interval 4-5 years of experience?
    #       english text
    #       etc.
    
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
                (year_fifteen, 15),
                (year_twenty, 20),
                (year, 2)
                ]

    # Search for seniority using regex keywords by first lowercasing the text
    for reg in regex_year:
        if re.search(reg[0], job_ad.lower()):
            tbr = reg[1]
            break
        else:
            tbr = None

    return tbr
