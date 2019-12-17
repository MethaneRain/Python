## My first attempt at web scraping!!

### I really wanted to be able to directly download a file (and also get certain data from the file) from the website via Python.

## For example, I wanted to get the most current weather model data initialization hour of the most current data file in the THREDDS sever.

~~~Python

import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = "http://thredds.ucar.edu/thredds/catalog/grib/NCEP/GFS/Global_0p25deg/latest.html"
response = requests.get(url)

response
>>> <Response [200]>

soup = BeautifulSoup(response.text, "html.parser")
soup.findAll('a')
>>> [<a href="latest.html?dataset=grib/NCEP/GFS/Global_0p25deg/GFS_Global_0p25deg_20191010_1200.grib2"><tt>GFS_Global_0p25deg_20191010_1200.grib2</tt></a>,
 <a href="/thredds/catalog.html">THREDDS Data Server</a>,
 <a href="http://www.unidata.ucar.edu/">Unidata</a>,
 <a href="/thredds/serverInfo.html"> Info </a>,
 <a href="http://www.unidata.ucar.edu/software/thredds/current/tds/reference/index.html"> Documentation</a>]

one_a_tag = soup.findAll('a')[0]
link = one_a_tag['href']
link
>>> 'latest.html?dataset=grib/NCEP/GFS/Global_0p25deg/GFS_Global_0p25deg_20191010_1200.grib2'


---

Gathering SPC's storm report ```csv``` files

* Filtered Tornado Reports:

```Python
import requests

print('Beginning file download with requests')

url = "https://www.spc.noaa.gov/climo/reports/today_torn.csv"
r = requests.get(url)

with open('torn_rpts.csv', 'wb') as f:
    f.write(r.content)
```
