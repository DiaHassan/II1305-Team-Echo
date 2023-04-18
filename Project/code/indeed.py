# All code explicit for webscraping Indeed.com

# LÄN and YRKE
# https://se.indeed.com/jobs?q=ingenjör&l=Stockholm&vjk=9f959c4e0166fe2d

# UTBILDNING
# <a class="yosegi-FilterPill-dropdownListItemLink" href="/jobb?q=civilingenj%C3%B6r&amp;l=Stockholm&amp;sc=0kf%3Aattr(HFDVW)%3B" rel="nofollow" tabindex="-1">Kandidatexamen (97)</a>

# DATUM
# <span class="date"><span class="visually-hidden">Posted</span>"Publicerad för 15 dagar sedan"</span>
# Comment: quotation on plain text?

# NEXT PAGE
# <a data-testid="pagination-page-3" rel="nofollow" aria-label="3" href="https://se.indeed.com/jobs?q=ingenj%C3%B6r&amp;l=Stockholm&amp;start=20&amp;pp=gQAeAAABh45grFkAAAACACfwogBGAQEBEAS1yU3WaQz46-2c2Xhs9PhZJM6xrKcwXv7jqPk_tMm1B3JQ08zgg5wYpf1fHbEBnQpc8ohDRhEvt0NjpaWs0VuQtAAA" class="css-1qt7hdn e8ju0x50">3</a>
# Comment: page and label incrementing


# Testing of HTML user agent
import requests
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}
r = requests.get('https://se.indeed.com/jobs?q=ingenjör&l=Stockholm&vjk=9f959c4e0166fe2d/', headers=HEADERS)
print(r.text)

