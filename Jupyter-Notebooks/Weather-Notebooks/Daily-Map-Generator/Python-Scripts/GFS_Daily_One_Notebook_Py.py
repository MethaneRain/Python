#!/usr/bin/env python
# coding: utf-8

# Importing Datetime Libraries
from datetime import datetime, timedelta
import os

now = datetime.utcnow()
#now = datetime(2019,9,5,18,0)
today_day = int('{0:%d}'.format(now))
today_month = int('{0:%m}'.format(now))
today_year = int('{0:%Y}'.format(now))
print(today_month,today_day,today_year)

forecast_times = []

for i in range(4,8):
    forecast_times.append(datetime(today_year,today_month,today_day,i*3,0))
for i in range(0,5):
    forecast_times.append(datetime(today_year,today_month,today_day+1,i*3,0))


# Set a path to save the plots with string format for the date to set the month and day
im_save_path = "/path/to/saved/files/"+str(today_year)+'/{0:%m_%d}'.format(now)+"/"
#im_save_path ="/Users/chowdahead/Desktop/Weather_Blog/"+str(today_year)+'/{0:%m_%d}'.format(now)+"/"
print(im_save_path)

# Check to see if the folder already exists, if not create it
if not os.path.isdir(im_save_path):
    os.makedirs(im_save_path)
# Uncomment if you want to automatically change to the map folder
#os.chdir(im_save_path)

import GFS_Forecast_1000_and_500mb as GFS_1000_500
import GFS_Forecast_500mb_Vorticity as GFS_Vort
import GFS_Forecast_HILO as GFS_HiLo
import GFS_Forecast_Jets as GFS_Jets
import GFS_Forecast_Surface as Surf
import GFS_Forecast_CAPE as CAPE
import GFS_Forecast_6hr_Precip as Prcip
import GFS_Forecast_PV_Jets as PVJets
import GFS_Forecast_4_Panel_Isen as Isen4

for i in forecast_times:
    GFS_1000_500.Map_1000_500(i,im_save_path)
    GFS_Vort.Map_500_Vort(i,im_save_path)
    GFS_HiLo.Map_HiLo(i,im_save_path)
    GFS_Jets.Map_Jets(i,im_save_path)
    Surf.Map_Sfc(i,im_save_path)
    CAPE.Map_Cape(i,im_save_path)
    Prcip.Map_6hrPrecip(i,im_save_path)
    PVJets.Map_PVJet(i,im_save_path)
    #Theta.Map_Theta(forecast_times[0],im_save_path)
    #Isen4.Map_Isen4(forecast_times[0],im_save_path)
