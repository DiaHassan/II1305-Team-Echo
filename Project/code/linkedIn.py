# All code explicit for webscraping LinkedIn.com

import requests

print("before")
url = "https://www.linkedin.com/jobs/search/?currentJobId=3560018027&geoId=104853962&keywords=engineer&location=Stockholm%20County%2C%20Sweden&refresh=true"
response = requests.get(url)
 
print(response.content)
print("after")