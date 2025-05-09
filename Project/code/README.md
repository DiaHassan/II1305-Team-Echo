# Documentation

## [/ledigajobb](https://github.com/DiaHassan/II1305-Team-Echo/tree/main/Project/code/ledigajobb)
The file in the ```ledigajobb``` folder is used to web scrape job listing data from Ledigajobb.  

### [ledigajobb.py](https://github.com/DiaHassan/II1305-Team-Echo/blob/main/Project/code/ledigajobb/ledigajobb.py)
Extracts data from Ledigajobb. This file contains several functions.

#### ***FUNCTIONS***
**get_code(url)**:  
*Sends an HTTP GET request to the specified* ```url``` *and returns the HTML (*```response```*) if possible.*  

**get_jobs(response)**:  
*Finds all job listings on the page.*  

**get_job_links(job_listings)**:  
*Uses* ```job_listings``` *received from* **get_jobs** *and returns those listings' job links.*  

**get_next_page(response)**:  
*Finds the link to the next page. Returns False if no link is found.*  

**create_search_link(lan, work, page)**:  
*Creates a URL based on* ```lan``` *(county)*, ```work``` *(occupation) and a specific* ```page```*.*  

**replace_after(my_string, to_replace, replacement)**:  
*Replaces the index of the link to get to the next page.*  

**join_url(base_url, section)**:  
*Appends the base URL with the path to the job ad and returns a link directly to the job ad.*  

**get_date(response)**:  
*Extracts the date from the HTML response.*  

**get_prerequiered(response)**:  
*Returns the pre-requirements from the HTML response.*  

**get_work_details(response)**:  
*Returns employment type, duration and seniority from the HTML response.*  

**find_lan(lan_nb)**:  
*Finds the next municipality in* ```lan_list```*.*  

**run()**:  
*Returns* ```get_all```*.*  

**scrape_ad(job_link, lan, work)**:  
*Returns all relevant information of a job listing in a list using the above functions.*  

**get_all()**:  
*Gets all information specified in* ```yrke_list``` *(occupation list) and* ```lan_list``` *(county list) using the above functions.*


## [/linkedIn](https://github.com/DiaHassan/II1305-Team-Echo/tree/main/Project/code/linkedIn)  
All files in the ```linkedIn``` folder are used to web scrape job listing data from LinkedIn.  

### [linkedIn.py](https://github.com/DiaHassan/II1305-Team-Echo/blob/main/Project/code/linkedIn/linkedIn.py)  
The "main" file that has all the data extracting functions. This file is dependent on the output produced by ```getGeoId.py```. 
Uses BeautifulSoup to analyze HTML elements.

#### ***FUNCTIONS***
**linkedin_scraper(job, municipality, page_number)**:  
*Establishes a connection to a page with* ```job``` *and* ```municipality``` *specified. Incrementing* ```page_number``` *and calling itself to load more ads.*

**extract_html(ad, job)**:  
*Extracts some data through HTML for a specific* ```ad```*.*

**extract_ad_page_html(key)**:  
*Gets the rest of the data by connecting to the ad-page of a specific ad with the help of it's* ```key``` *, then extracting data through HTML.*

**format(emp_type, ad_date, location, seniority)**:  
*Makes format changes for* ```emp_type``` *, * ```ad_date``` *, * ```location``` *, * ```seniority``` *such that it matches the other scrapers format.*

**get_professions()**:  
*Gets a list of the wanted proffessions*

**run()**:  
*Automates the* ```linkedin_scraper``` *function to scrape a list of jobs and municipalities.*

### [getGeoId.py](https://github.com/DiaHassan/II1305-Team-Echo/blob/main/Project/code/linkedIn/getGeoId.py)  
This script collects the GeoID's of a list of locations. This script is not run by ```main.py```, but if a new list of Geo ID's for different locations is desired, you can change the locations in the ```municipalities``` list:  
```python
municipalities = ["Upplands Väsby, Stockholm", "Österåker, Stockholm"]
```
The above code will let ```getGeoId.py``` search for the Geo ID's of Upplands Väsby and Österåker, provided if both have Geo ID's on LinkedIn. The Geo ID's and the name of the locations will be returned in ```geo_ids.txt```. This text file will then be used in ```linkedIn.py```'s run() function.


## [/platsbanken](https://github.com/DiaHassan/II1305-Team-Echo/tree/main/Project/code/platsbanken)
The program within the file connects to platsbanken API and retrieves all the information in ads from the last 30 days. It then extracts the relevant data and converts it into a format suitable for the database before sending it.  


### [platsbanken.py](https://github.com/DiaHassan/II1305-Team-Echo/blob/main/Project/code/platsbanken/platsbanken.py)
Extracts data from Platsbanken's API.

#### ***FUNCTIONS***
**run()**:  
*Retrieves all ads from given job ids and outputs their data in a 2D list.*

It achives this in a quite simple structure:
 1. Job ID:s are retrieved from the 10 occupations with occupation_ids
 2. Job ads are retrieved from given ID:s with occupation_ads
 3. Relevant Job ads data extracted from extract_data_all_ads
 4. Void ads are removed with remove_void_ads
 5. Return all ads left 


**get_ads(ids, index)**:  
*Retrieves all ads from a single occupation from the API in full.*

Input:
- Ids: List of all ids under a single occupation
- Index: Integer from the for-loop in run(), used for logging and easier readability in terminal.

Output:
- Returns a list of gathered ads with ALL information available.

**extract_data_all_ads(all_ads)**:  
*Extracts the relevant data from all ads into a list.*  

Input: 
- List of all ads in in FULL format gathered from get_ads()
Output: 
- List of all ads with RELEVANT data.

**extract_data_ad(ad, index)**:  
*Extracts neccesary data from an ad and returns it in a list*

Input: 
- ad: List of a single ad with ALL informaton available
- index: Integer from for-loop in run(), represents which job TITLE is being worked on

Output:
- List of a single ad and its relevant data

**extract_duration(duration)**:  
*Extracts the job's duration from the listing.*  

**remove_void_ads(ads)**:
*Iterates through each ad and removes it if county is null*


## [reqfinder.py](https://github.com/DiaHassan/II1305-Team-Echo/tree/main/Project/code/reqfinder.py)
Reads a string and finds the first recognizable pre-condition for a job application and returns it.  

## [file_to_list](https://github.com/DiaHassan/II1305-Team-Echo/blob/main/Project/code/file_to_list.py)
Only has one function which has the same name, for importing: 
- [professions.txt](https://github.com/DiaHassan/II1305-Team-Echo/blob/main/Project/professions.txt)
- [counties.txt](https://github.com/DiaHassan/II1305-Team-Echo/blob/main/Project/counties.txt)

## [webscrape.py](https://github.com/DiaHassan/II1305-Team-Echo/blob/main/Project/code/webscrape.py)
This program retrieves a list of all the webscraped data from the websites selected and forwards the data to the database to be inserted.  
