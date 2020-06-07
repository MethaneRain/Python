#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 00:52:49 2020

@author: Justin Richling

University of Wyoming and MetPy Soundings (non Siphon)
"""

class UWyoSound:
    """
    University of Wyoming
    """
    
    def __init__(self):
        '''
        Default values
        
        * date -> current date
        * launch hour -> 12Z
        * image save path -> cwd

        '''
        from datetime import datetime
        now = datetime.utcnow()
        #self.day0 = int('{0:%d}'.format(now))
        #self.day1 = int('{0:%d}'.format(now))
        #self.year = int('{0:%Y}'.format(now))
        #self.month = int('{0:%m}'.format(now))
        
        self.day0 = '{:02}'.format(now.day)
        self.day1 = '{:02}'.format(now.day)
        self.year = '{:4}'.format(now.year)
        self.month = '{:02}'.format(now.month)
        print(self.day0,self.year,self.month)
        
        # initialization hour for model forecast
        self.launch_hour = 12
        
        # current working drive for saved images
        self.im_save_path = "./"
        
        self.station_num = 72469
        self.station_name = "DNR"
        
    def scrape_text(self):
        import requests
        from bs4 import BeautifulSoup
        import urllib.request
        import os
        #if day1 == None:
        #    day1 = day0
        text_type = "TEXT"
        url_1 = f"http://weather.uwyo.edu/cgi-bin/sounding?region=naconf&TYPE={text_type}%3ALIST&"
        url_2 = "YEAR="+str(self.year)+"&MONTH="+str(int(self.month))+"&FROM="+str(int(self.day0))+"12&TO="+str(int(self.day1))+"12&STNM="+str(self.station_num)
        
        url = url_1+url_2
        print("Requested url:\n---------------------------------------------------\n",url,"\n---------------------------------------------------")
        print("\nCheck the response:")
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
        
            #base = "/Users/chowdahead/Desktop/Weather_Blog/"+str(year)+"/"+str(month)+"_"+str(day0)+"/"
            base = "/Users/chowdahead/Jupyter/"
            date_string = str(self.year)+"_"+str(self.month)+"_"+str(self.day1)+"_"+str(self.launch_hour)+"Z_"+str(self.station_num)
            loc = base+date_string+"_upperair.txt"
            print("file location:",base)
        
            if not os.path.isdir(base):
                os.makedirs(base)
            print("\nnext step, write the file...\n")
            try:
                file1 = open(loc,"w")
                print("File successfully created!")
            except:
                print("File not created...")
            print("\nSaved file name:",date_string+"_upperair.txt")
            file1.write(table_title[0]+"\n") # could exclude these if desired
            file1.write(table_station[0]) # could exclude these if desired
            file1.write(table)
            file1.write(table_data[0]) # could exclude these if desired
        
            # Finally, close the file and we're done!
            file1.close()
            print("\nAll good!!")
        except:
            print("\nBad gateway, file not created :(")
        #print(loc)
                
            
                
                