# Documentation

## Necessary installations:  
In order to run the code, the following libraries and programs will be needed:  
 - Selenium (Python library)
 - BeautifulSoup (Python library)
 - pandas (Python library)
 - DB Browser (SQLite)


## [main.py](https://github.com/DiaHassan/II1305-Team-Echo/blob/main/Project/code/main.py)
This program retrieves a list of all the webscraped data from the websites selected and forwards the data to the database to be inserted.


## [/ledigajobb](https://github.com/DiaHassan/II1305-Team-Echo/tree/main/Project/code/ledigajobb)
The file in the ```ledigajobb``` folder is used to web scrape job listing data from Ledigajobb. This folder consists of ```ledigajobb.py```.  

### ledigajobb.py
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
**get_prerequiered(respone)**:  
*Returns the pre-requirements from the HTML response.*  
**get_work_details(response)**:  
*Returns employment type, duration and seniority from the HTML response.*  
**find_lan(lan_nb)**:  
todo


## [/linkedIn](https://github.com/DiaHassan/II1305-Team-Echo/tree/main/Project/code/linkedIn)
All files in the ```linkedIn``` folder are used to web scrape job listing data from LinkedIn. This folder consists of ```linkedIn.py``` and ```getGeoId.py```.  
To extract data from LinkedIn, the following code will return all data in a list:
```python
linkedInData = linkedIn.run()
```  
Similar code is already included in ```main.py```.

### linkedIn.py
The "main" file that has all the data extracting functions. This file is dependent on the output produced by ```getGeoId.py```.

#### Functions
**linkedin_scraper(job, municipality, page_number)**:  
*Scrapes all ads on the page, with* ```job``` *and* ```municipality``` *specified.*  

**run()**:  
*Automates the* ```linkedin_scraper``` *function to scrape a list of jobs and municipalities.*  

### getGeoId.py
This script collects the GeoID's of a list of locations. This script is not run by ```main.py```, but if a new list of Geo ID's for different locations is desired, you can change the locations in the ```municipalities``` list:  
```python
municipalities = ["Upplands Väsby, Stockholm", "Österåker, Stockholm"]
```
The above code will let ```getGeoId.py``` search for the Geo ID's of Upplands Väsby and Österåker, provided if both have Geo ID's on LinkedIn. The Geo ID's and the name of the locations will be returned in ```geo_ids.txt```. This text file will then be used in ```linkedIn.py```'s run() function.


## [/platsbanken](https://github.com/DiaHassan/II1305-Team-Echo/tree/main/Project/code/platsbanken)
The program within the file connects to platsbanken API and retrieves all the information in ads from the last 30 days. It then extracts the relevant data and converts it into a format suitable for the database before sending it. This folder consists of ```platsbanken.py```.  

### platsbanken.py
Extracts data from Platsbanken's API. There are several functions in this file.

#### Functions

**get_ads()**:  
*Retrieves all ads from the API in full.*  
[todo]

**extract_data_ad()**:
*Extracts neccesary data from an ad using json and returns it in a array*


## [reqfinder.py](https://github.com/DiaHassan/II1305-Team-Echo/tree/main/Project/code/reqfinder.py)
Reads a string and finds the first recognizable pre-condition for a job application and returns it.
