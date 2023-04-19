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
            tbr= "Not specified"

    return tbr

print("vvvvvvv\n")
print(find_req(job_ad))
print("\n^^^^^^^")