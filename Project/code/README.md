# Documentation
## Necessary installations:  
In order to run the code, the following libraries and programs will be needed:  
 - Selenium (Python library)
 - BeautifulSoup (Python library)
 - pandas (Python library)
 - DB Browser (SQLite)

## [/linkedIn](https://github.com/DiaHassan/II1305-Team-Echo/tree/main/Project/code/linkedIn)
All files in the ```linkedIn``` folder are used to web scrape job listing data from LinkedIn. This folder consists of ```linkedIn.py``` and ```getGeoId.py```.  
To just extract data from LinkedIn, the following code will return all data in a list:
```python
linkedInData = linkedIn.run()
```  
Similar code is already included in ```main.py```.
### linkedIn.py
The "main" file that has all the data extracting functions. This file is dependent on the output produced by ```getGeoId.py```.
#### Functions
**linkedin_scraper(job, municipality, page_number)**  
*Scrapes all ads on the page, with* ```job``` *and* ```municipality``` *specified.*  
**run()**  
*Automates the* ```linkedin_scraper``` *function to scrape a list of jobs and municipalities.*  
### getGeoId.py
This script collects the GeoID's of a list of locations.
