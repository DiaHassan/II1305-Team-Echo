import sqlite3
from countyprof import profession_list
from sys import platform


def find_db_path(platform):
    match platform:
        case "linux":
            return "Project/db/echo.db"
        case "darwin":
            return "Project/db/echo.db"
        case _:
            return "Project\db\echo.db"

db_path = find_db_path(platform)

# [(a,b), (c,d)] --> [[a,b], [c,d]]
def list_of_tuples_to_2d_list(list_of_tuples):
    result = []
    for t in list_of_tuples:
       result.append(list(t)) 
    return result    


# [[(a,b)], [(c,d)]] --> [[a,b], [c,d]]
def list_of_list_tuple_to_2d_list(list_of_list_tuple):
    result = []
    for list_tuple in list_of_list_tuple:
       result.append(list(list_tuple.pop()))  
    return result     


# Merges list with key-value
# [[a, x], [b, y], [b,z]] --> [[a, x], [b, [y,z]]]
def merge_list(lst):
    # Group the elements by their first value
    groups = {}
    for elem in lst:
        key = elem[0]
        if key not in groups:
            groups[key] = []
        groups[key].append(elem[1:])

    # Combine the second and third values of each group into a list
    result = []
    for key, values in groups.items():
        combined = [key]
        for i in range(len(values[0])):
            combined.append([v[i] for v in values])
        result.append(combined)

    return result


# Connects to database and sends query
def send_query(query):
    with sqlite3.connect(db_path) as conn:
      cursor = conn.cursor()
      result = cursor.execute(query).fetchall()
      cursor.close()
    conn.close()
    result = list_of_tuples_to_2d_list(result)
    return result


# X-axis: all counties
# Y-axis: number of ads in variable profession 
def get_profession_in_counties(profession):
    query = 'SELECT jl.county, COUNT(j.id) as job_count \
            FROM job_listing jl \
            LEFT JOIN job j ON jl.job_id = j.id AND j.profession LIKE "%' + profession + '%" \
            WHERE county IS NOT "null" \
            GROUP BY jl.county'
    result = send_query(query)
    result.insert(0, profession)
    return result


# X-axis: all counties
# Y-axis: variable param of ads in variable profession
def get_param_per_county(profession, param): 
    query = 'SELECT j.county, j.' + param + ', COUNT(*) as count \
            FROM job_listing j \
            JOIN job p ON j.job_id = p.id \
            WHERE p.profession LIKE "%' + profession + '%" AND ' + param + ' IS NOT + "null"\
            GROUP BY j.county, j.' + param
    result = send_query(query)
    result = merge_list(result)
    result.insert(0, (profession, param))
    return result


# X-axis: all professions
# Y-axis: number of professions in variable county
def get_professions_in_county(county): 
    with sqlite3.connect(db_path) as conn:
        result = []
        cursor = conn.cursor()
        for profession in profession_list:
            query = 'SELECT "' + profession +  '" AS profession, COUNT(job_listing.id) as "sum" \
                    FROM job_listing INNER JOIN job ON job.id = job_listing.job_id \
                    WHERE county = "' + county + '" AND profession LIKE "%' + profession + '%"'
            result.append(cursor.execute(query).fetchall())
        cursor.close()
    conn.close()
    result = list_of_list_tuple_to_2d_list(result)
    result.insert(0, (county))
    return result


# One function to rule them all -E
def general_extraction(xaxis, yaxis, parameters):
    #xaxis is the attribute that we want ot show on the xaxis
    #yaxis is the attribute that we want ot show on the yaxis
    #parameters is an array where each attribute is an array with the structure 
    # ["attributename", [acceptablevalues("which counties we search or perhaps min value for attributes like years of experience")]]
    # SELECT yaxis, count(xaxis) from table WHERE conditions GROUP BY yaxis
    # WHERE 
    job_listing_parameters = ["source", "employment_type", "duration", "publication_date", "county", "years_of_experience", "seniority", "date_gathered"]
    outside_params = [""]
    #The string for parameters which are withing the argument list. 
    #for i in parameters:
     #   if i in


# Test
if __name__ == '__main__':
    #print(get_profession_in_counties('Städare'))
    print(get_param_per_county('Läkare', 'duration'))
    #print(get_professions_in_county('Stockholms län'))
