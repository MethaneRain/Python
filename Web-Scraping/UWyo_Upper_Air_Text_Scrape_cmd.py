#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import requests
from bs4 import BeautifulSoup
import urllib.request
import os,sys

'''
Handy little script for grabbing the text data from the University of Wyoming Upper Air data

Url: http://weather.uwyo.edu/upperair/sounding.html

Author - Justin Richling 2020/03/27
-------------------------------------------------------------------------------------------

This has the option of grabbing one hour's worth (12 or 00Z) or a range of dates

System Arguments example:
-------------------------
$ python UWyo_Upper_Air_Text_Scrape.py year month (with leading 0), day (with leading 0),
    hour (with leading 0)

** If setting a range of dates/times, the command line args must go as follows:
    - year, month (includeing 0 if before Oct.), day start (including 0 if before the 10th),
      hour start (including 0 if 00Z), day end (including 0 if before the 10th),
      hour end (including 0 if 00Z)

Args:
-----
text_type - raw, unmerged or text (see website)
station - coded station number (ie Denver is 72469)
year
month
day0 - start of the range of dates 
hour0 - start of the range of hours (must be 00 or 12Z)
day1 - (optional) end of range of dates
hour1 - (optional) end of range of hours (must be 00 or 12Z)

Method:
-------
Use BeautifulSoup to grab data from the URL and parse the text from different html tags

* The actual data values to plot a sounding are wrapped in the first <pre> tag
* The station data and calculated indicies are wraped in the second <pre> tag
* The University of Wyoming title is in wrapped in the <title> tag
* The station number, short name and actual name along with the date are wrapped in <h2> tag

'''
text_type = "TEXT"
station = 72469
year = sys.argv[1] #2020
month = sys.argv[2] #3
day0 = sys.argv[3] #27
hour0 = sys.argv[4] #12
# optional args
#if sys.argv
print(len(sys.argv[:]))
if len(sys.argv[:]) == 5:
    day1 = sys.argv[3]
    hour1 = sys.argv[4]
else:
    day1 = sys.argv[5]
    hour1 = sys.argv[6]

#url_1 = f"http://weather.uwyo.edu/cgi-bin/sounding?region=naconf&TYPE={text_type}%3ALIST&"
#url_2 = f"YEAR={year}&MONTH={month:02}&FROM={day1}{hour0:02}&TO={day1}{hour1:02}&STNM={station}"

url_1 = "http://weather.uwyo.edu/cgi-bin/sounding?region=naconf&TYPE="+text_type+"%3ALIST&"
url_2 = "YEAR="+str(year)+"&MONTH="+str(month)+"&FROM="+str(day1)+str(hour0)+"&TO="+str(day1)+str(hour1)+"&STNM="+str(station)

url = url_1+url_2
print(url)
response = urllib.request.urlopen(url)
html = response.read()

# Check if the response went through
print("If response check is 200, we're good to proceed")
response_check = requests.get(url)
print(response_check)

try:
    soup = BeautifulSoup(html, "html.parser")

    # Grab the first <pre></pre> data which is the actual table of values
    table = soup.find("pre").find(text=True)

    # Extract the Station and Indices Values
    table_data = [x.extract() for x in soup.find_all('pre')[1]]

    # Extract the Station and Indices Values
    table_title = [x.extract() for x in soup.find('title')]

    # Extract the Station and Indices Values
    table_station = [x.extract() for x in soup.find('h2')]

    # Create new text file and write the data
    #base = f"/Users/chowdahead/Desktop/Weather_Blog/{year}/{month:02}_{day0:02}/"
    #loc = base+f"{year}_{month :02}_{day0}_{hour0}_{station}_upperair.txt"
    
    base = "/Users/chowdahead/Desktop/Weather_Blog/"+str(year)+"/"+str(month)+"_"+str(day0)+"/"
    loc = base+str(year)+"_"+str(month)+"_"+str(day0)+"_"+str(hour0)+"_"+str(station)+"_upperair.txt"
    
    if not os.path.isdir(base):
        os.makedirs(base)
    
    file1 = open(loc,"w") 
    print("Saved file going to:",loc)
    file1.write(table_title[0]+"\n") # could exclude these if desired
    file1.write(table_station[0]) # could exclude these if desired
    file1.write(table)
    file1.write(table_data[0]) # could exclude these if desired

    # Finally, close the file and we're done!
    file1.close()
    print("File successfully created!")
except:
    print("Bad gateway, file not created :(")

