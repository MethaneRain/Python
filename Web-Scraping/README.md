## My first attempt at web scraping!!

### I really wanted to be able to directly download a file (and also get certain data from the file) from the website via Python.

#### For example, I wanted to get the most current weather model data initialization hour of the most current data file in the THREDDS sever.

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
>>> [<a href="latest.html?dataset=grib/NCEP/GFS/Global_0p25deg/GFS_Global_0p25deg_20200129_1200.grib2"><tt>GFS_Global_0p25deg_20191010_1200.grib2</tt></a>,
 <a href="/thredds/catalog.html">THREDDS Data Server</a>,
 <a href="http://www.unidata.ucar.edu/">Unidata</a>,
 <a href="/thredds/serverInfo.html"> Info </a>,
 <a href="http://www.unidata.ucar.edu/software/thredds/current/tds/reference/index.html"> Documentation</a>]

one_a_tag = soup.findAll('a')[0]
link = one_a_tag['href']
link
>>> 'latest.html?dataset=grib/NCEP/GFS/Global_0p25deg/GFS_Global_0p25deg_20200129_1200.grib2'

URL = url+link
URL
>>>
'http://thredds.ucar.edu/thredds/catalog/grib/NCEP/GFS/Global_0p25deg/latest.htmllatest.html?dataset=grib/NCEP/GFS/Global_0p25deg/GFS_Global_0p25deg_20200129_1200.grib2'

! curl -O '{URL}'

ls *.grib2
>>>

GFS_Global_0p25deg_20200129_1200.grib2
~~~


Grabbing text from University of Wyoming Upper Air

Since UWyo radiosonde data is only text (no file to download) the approach is slightly different than actuall scraping a file like ```csv``` or ```grib``` file.

The stations and date options can be found at: http://weather.uwyo.edu/upperair/sounding.html

The url will lead to just text and can be altered by station which is a number used for the city/station. The other url arguments are: year, month, starting day, ending day, starting hour and ending hour with hour only being eith 00 or 12Z. 

Note, the option ofr TYOE could be raw, unmergerd or list text.

Sample url for March 27th, 2020 12Z for Denver (station num 72469):
http://weather.uwyo.edu/cgi-bin/sounding?region=naconf&TYPE=TEXT%3ALIST&YEAR=2020&MONTH=03&FROM=2712&TO=2712&STNM=72469


---

Gathering SPC's storm report ```csv``` files

* Filtered Tornado Reports:

~~~Python
import requests

print('Beginning file download with requests')

url = "https://www.spc.noaa.gov/climo/reports/today_torn.csv"
r = requests.get(url)

with open('torn_rpts.csv', 'wb') as f:
    f.write(r.content)
~~~
