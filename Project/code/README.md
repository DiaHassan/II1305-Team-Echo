# Documentation

## Necessary installations:  
In order to run the code, the following libraries and programs will be needed:  
 - Selenium (Python library)
 - BeautifulSoup (Python library)
 - pandas (Python library)
 - DB Browser (SQLite)


## [/ledigajobb](https://github.com/DiaHassan/II1305-Team-Echo/tree/main/Project/code/ledigajobb)
The file in the ```ledigajobb``` folder is used to web scrape job listing data from Ledigajobb.  

### [ledigajobb.py](https://github.com/DiaHassan/II1305-Team-Echo/blob/main/Project/code/ledigajobb/ledigajobb.py)
Extracts data from Ledigajobb. This file contains several functions.

#### Functions
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

#### Functions
**linkedin_scraper(job, municipality, page_number)**:  
*Establishes a connection to a page with* ```job``` *and* ```municipality``` *specified. Incrementing* ```page_number``` *and calling itself to load more ads.*

**extract_html(ad, job)**:
*Extracts some data through HTML for a specific ```ad```.*

**extract_ad_page_html(key)**:
*Gets the rest of the data by connecting to the ad-page of a specific ad with the help of it's* ```key```*, then extracting data through HTML.*

**format(emp_type, ad_date, location, seniority)**:
*Makes format changes for* ```emp_type```*, *```ad_date```*, *```location```*, *```seniority``` *such that it matches the other scrapers format.*

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

#### Functions
**run()**:  
*Retrieves all ads and outputs their data in a 2D list.*  

**get_ads()**:  
*Retrieves all ads from the API in full.*  

**extract_data_all_ads(all_ads)**:  
*Extracts the relevant data from all ads into a list.*  

**extract_duration(duration)**:  
*Extracts the job's duration from the listing.*  

**extract_data_ad()**:  
*Extracts neccesary data from an ad using json and returns it in an array*  


## [job_info.py](https://github.com/DiaHassan/II1305-Team-Echo/blob/main/Project/code/job_info.py)  
All of the occupations and counties we are web scraping for.


## [reqfinder.py](https://github.com/DiaHassan/II1305-Team-Echo/tree/main/Project/code/reqfinder.py)
Reads a string and finds the first recognizable pre-condition for a job application and returns it.  


## [webscrape.py](https://github.com/DiaHassan/II1305-Team-Echo/blob/main/Project/code/webscrape.py)
This program retrieves a list of all the webscraped data from the websites selected and forwards the data to the database to be inserted.  
