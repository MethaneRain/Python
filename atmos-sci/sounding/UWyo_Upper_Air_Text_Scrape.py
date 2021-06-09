#!/usr/bin/env python
# coding: utf-8

import requests
from bs4 import BeautifulSoup
import urllib.request
from datetime import datetime
import os, sys

'''
Handy little script for grabbing the text data from the University of Wyoming Upper Air data

Url: http://weather.uwyo.edu/upperair/sounding.html

Author - Justin Richling 2020/03/27
-------------------------------------------------------------------------------------------

This has the option of grabbing one hour's worth (12 or 00Z) or a range of dates

System Arguments example:
-------------------------
$ python UWyo_Upper_Air_Text_Scrape.py year month (with leading 0), day (with leading 0),
    hour (with leading 0) 72469

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
#now = datetime.utcnow()
#now = datetime(2019,4,10,0,0)
#today_day = int('{0:%d}'.format(now))
#today_year = int('{0:%Y}'.format(now))
#today_month = int('{0:%m}'.format(now))
#init_hour = 12
init_hour = sys.argv[4]
#print(today_day,today_year,today_month)



text_type = "TEXT"
#station = 72469
station = sys.argv[5]
#year = now.year
year = sys.argv[1]
#month = '{:02d}'.format(now.month)
month = sys.argv[2]
#day0 = int('{:02d}'.format(now.day))-1
#day0 = 
#print(day0)
#day1 = int('{:02d}'.format(now.day))-1
day1 = sys.argv[3]
for arg in sys.argv:
    print(arg)
#url_1 = f"http://weather.uwyo.edu/cgi-bin/sounding?region=naconf&TYPE={text_type}%3ALIST&"
#url_2 = f"YEAR={year}&MONTH={month:02}&FROM={day1}{hour0:02}&TO={day1}{hour1:02}&STNM={station}"

print("{:02d}/{:02d}/{:4d}".format(int(month),int(day1),int(year)))

url_1 = "http://weather.uwyo.edu/cgi-bin/sounding?region=naconf&TYPE=TEXT%3ALIST&"
url_2 = "YEAR="+str(year)+"&MONTH="+str(month)+"&FROM="+str(day1)+str(init_hour)+"&TO="+str(day1)+str(init_hour)+"&STNM="+str(station)

url = url_1+url_2
print(url)
response = urllib.request.urlopen(url)
html = response.read()

# Check if the response went through
print("If response check is 200, we're good to proceed")
response_check = requests.get(url)
print(response_check)
#day0 = '{:02d}'.format(now.day)
#day0 = 
#print(day0)
#day1 = '{:02d}'.format(now.day)
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

    base = "./"
    date_string = str(year)+"_"+str(month)+"_"+str(day1)+"_"+str(init_hour)+"Z_"+str(station)
    print(date_string)
    loc = base+date_string+"_upperair.txt"

    if not os.path.isdir(base):
        os.makedirs(base)

    file1 = open(loc,"w")
    print("Saved file going to:",loc)
    #file1.write(table_title[0]+"\n") # could exclude these if desired
    #file1.write(table_station[0]) # could exclude these if desired
    file1.write(table)
    #file1.write(table_data[0]) # could exclude these if desired

    # Finally, close the file and we're done!
    file1.close()

    file2 = open(base+date_string+"_upperair_indicies.txt","w")
    file2.write(table_title[0]+"\n") # could exclude these if desired
    file2.write(table_station[0]) # could exclude these if desired
    #file1.write(table)
    file2.write(table_data[0]) # could exclude these if desired

    # Finally, close the file and we're done!
    file2.close()


    print("Files successfully created!")
except:
    print("Bad gateway, file not created :(")
    
#os.system("chmod +x UWyo_UpperAir_striplines.sh")
os.system("./UWyo_UpperAir_striplines.sh " +str(year)+"_"+str(month)+"_"+str(day1)+"_"+str(init_hour)+"Z_"+str(station))
