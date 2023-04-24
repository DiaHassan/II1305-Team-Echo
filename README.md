# II1305 Project in Information and Communication Technology


## About The Project
<!-- Bakgrund -->
TODO

### Built With
- python
- sql

### Dependencies
Python libraries used:
- requests
- beautifulsoup4
- pandas
- selenium

### Documentation
#### [Project/code/main.py](https://github.com/DiaHassan/II1305-Team-Echo/blob/main/Project/code/main.py)
The program retrieves a list of all the webscraped data from the websites selected and forwards the data to the database to be inserted.

#### [Project/code/platsbanken/platsbanken.py](https://github.com/DiaHassan/II1305-Team-Echo/blob/main/Project/code/platsbanken/platsbanken.py)
The program within the file connects to platsbanken API and retrieves all the information in ads from the last 30 days, it then extracts the relevant data and converts it into a format suitable for the database before sending it.

#### [Project/code/ledigajobb/ledigajobb.py](https://github.com/DiaHassan/II1305-Team-Echo/blob/main/Project/code/ledigajobb/ledigajobb.py)
Todo
<!-- Info here -->

#### [Project/code/linkedIn/](https://github.com/DiaHassan/II1305-Team-Echo/blob/main/Project/code/linkedIn)  
All files in the ```linkedIn``` folder are used to web scrape job listing data from LinkedIn. This folder consists of ```linkedIn.py``` and ```getGeoId.py```.  
To just extract data from LinkedIn, the following code will return all data in a list:
```python
linkedInData = linkedIn.run()
```  
Similar code is already included in ```main.py```.
##### [linkedIn.py](https://github.com/DiaHassan/II1305-Team-Echo/blob/main/Project/code/linkedIn/linkedIn.py)
The "main" file that has all the data extracting functions. This file is dependent on the output produced by ```getGeoId.py```.
###### Functions
**linkedin_scraper(job, municipality, page_number)**:  
*Scrapes all ads on the page, with* ```job``` *and* ```municipality``` *specified.*  
**run()**:  
*Automates the* ```linkedin_scraper``` *function to scrape a list of jobs and municipalities.*  
##### [getGeoId.py](https://github.com/DiaHassan/II1305-Team-Echo/blob/main/Project/code/linkedIn/getGeoId.py)
This script collects the GeoID's of a list of locations. This script is not run by ```main.py```, but if a new list of Geo ID's for different locations is desired, you can change the locations in the ```municipalities``` list:  
```python
municipalities = ["Upplands Väsby, Stockholm", "Österåker, Stockholm"]
```
The above code will let ```getGeoId.py``` search for the Geo ID's of Upplands Väsby and Österåker, provided if both have Geo ID's on LinkedIn. The Geo ID's and the name of the locations will be returned in ```geo_ids.txt```.




## Usage
- Project/code/main.py to webscrape and store the data in echo.db 


## Website
Todo
<!-- Länk till expo -->


## Team Echo
 - [Edwin Ahlstrand](https://github.com/EdwinAhl)
 - [Roy Liu](https://github.com/ruisnake)
 - [Albin Durfors](https://github.com/DrakenDurfors)
 - [Axel Lindqvist](https://github.com/ProgrammingCookies)
 - [Klara Fält](https://github.com/kflt)
 - [Zak Ora](https://github.com/ZakOra1)
<!--[Ditt namn här](länk till din Github-profil)-->
