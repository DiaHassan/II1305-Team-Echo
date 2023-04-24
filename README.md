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
- requests

### Documentation
#### [Project/code/main.py](https://github.com/DiaHassan/II1305-Team-Echo/blob/main/Project/code/main.py)
The program retrieves a list of all the webscraped data from the websites selected and forwards the data to the database to be inserted.

#### [Project/code/platsbanken/platsbanken.py](https://github.com/DiaHassan/II1305-Team-Echo/blob/main/Project/code/platsbanken/platsbanken.py)
The program within the file connects to platsbanken API and retrieves all the information in ads from the last 30 days, it then extracts the relevant data and converts it into a format suitable for the database before sending it.

#### [Project/code/ledigajobb/ledigajobb.py](https://github.com/DiaHassan/II1305-Team-Echo/blob/main/Project/code/ledigajobb/ledigajobb.py)
Todo
<!-- Info here -->

#### [Project/code/linkedIn/linkedIn.py](https://github.com/DiaHassan/II1305-Team-Echo/blob/main/Project/code/linkedIn/linkedIn.py)
In the folder there's a file, ```GetGeoids.py```, that uses selenium to search Linkedid for all their municipalities and extracts their geo id and puts them in a text file.
This text file is then used in ```linkedIn.py``` to be able to search for jobs in every municipality in Sweden. The program then extract the html file for each job ad and extracts the data that is needed and converts it into a format suitable for the database before sending it.  
  
```GetGeoids.py```: uses Selenium to search and extract all GeoID's of the specified locations in the ```cities``` list into a ```geo_ids.txt```.  
```linkedIn.py```: makes use of ```geo_ids.txt``` and a list of different occupations to search through all of the relevant [todo]




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
