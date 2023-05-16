# II1305 Project in Information and Communication Technology

## Websites
- [Dashboard](https://stmecho-ad215.web.app/)
- [Expo](https://teamechokth.wixsite.com/team-echo---expo-sit)

## About The Project
Our project was made externaly for Future Place Leadership as a dashboard collecting data of job listings in Sweden. The data is collected from three websites which are LinkedIn, Platsbanken and LedigaJobb. Lastly, the information extracted from the ads is: employement type, duration, publication date, profession, county, job requirements, years of experience and seniority.

### Built With
- python
- sqlite
- javascript and react
- html and css

### Dependencies
Python packages used:
[requirements.txt](https://github.com/DiaHassan/II1305-Team-Echo/blob/main/requirements.txt)

To install all dependencies using pip, run: ```pip install -r requirements.txt```

## Usage
First, install all of the Python dependencies by running the command above (in the **Dependencies** section) in the terminal. Also, make sure you have [DB Browser](https://sqlitebrowser.org/dl/) and [Node.js](https://nodejs.org/en/download/current) (Current Version) downloaded.  
### Webscraping
In order for the webscraping to work, the files in [/Project/code](https://github.com/DiaHassan/II1305-Team-Echo/tree/main/Project/code) and [/Project/db](https://github.com/DiaHassan/II1305-Team-Echo/tree/main/Project/db) should be run from the root directory. An example of running [```webscrape.py```](https://github.com/DiaHassan/II1305-Team-Echo/blob/main/Project/code/webscrape.py) from root directory, provided if the root directory is named "Root":  
```
C:\Users\example\Desktop\Root> python Project/code/webscrape.py
```
By running ```webscrape.py```, the program will scrape the data from the specified websites and create a database file called ```echo.db```. Estimated scraping times: ~1 min for Platsbanken, ~15 min for LedigaJobb and ~4.5 h for LinkedIn.  
### Starting the Servers
You will first need to start the database server. To run the database server, write
```
C:\Users\example\Desktop\Root> python Project/db/data_handler.py
```
and the terminal will host the server.
To get the website running, open a new terminal and change directory to the ```dashboard``` folder. There, if this is the first time your machine is running this code, run the command
```
C:\Users\example\Desktop\Root\Project\dashboard> npm install --force
```
After the installations are complete, run
```
C:\Users\example\Desktop\Root\Project\dashboard> npm start
```
and the website will be opened in your browser.

## Documentation
- [Code](https://github.com/DiaHassan/II1305-Team-Echo/blob/main/Project/code/README.md)
- [Dashboard](https://github.com/DiaHassan/II1305-Team-Echo/blob/main/Project/dashboard/README.md)
- [Database](https://github.com/DiaHassan/II1305-Team-Echo/blob/main/Project/db/README.md)

## Team Echo
 - [Hassan Dia](https://github.com/DiaHassan)              | Product Owner/Developer
 - [Tina Basta](https://github.com/tibasta)                | SCRUM Master/Developer
 - [Edwin Ahlstrand](https://github.com/EdwinAhl)          | Developer
 - [Roy Liu](https://github.com/ruisnake)                  | Developer
 - [Albin Durfors](https://github.com/DrakenDurfors)       | Developer
 - [Axel Lindqvist](https://github.com/ProgrammingCookies) | Developer
 - [Klara Fält](https://github.com/kflt)                   | Developer
 - [Zak Ora](https://github.com/ZakOra1)                   | Developer
 - [Samuel Sendek](https://github.com/CooperUSA)           | Developer
