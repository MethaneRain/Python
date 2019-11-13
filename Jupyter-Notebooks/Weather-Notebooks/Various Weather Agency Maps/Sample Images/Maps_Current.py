#!/usr/bin/env python
# coding: utf-8

# # Daily Maps from Websites

# ## Justin Richling
# ## 09/20/18

# 
# # Saved Images from Various Weather Websites
# 
# 
# Search through different weather websites and retreive the current images
# 
# There are several handy maps that we can grab here:
# * Weather Warnings
# * Convection Percentages (Summer)
# * 24-Hr Snowfall Accumulations (Winter)
# * Multi Day Forecasts (Fronts and Precip Types)
# * Radar (CONUS and Colorado)
# * Duane Tower in Boulder Meteogram
# 

# ## Imports

# In[1]:


# Random Library Imports
import os,glob,webbrowser

import urllib.request
from urllib.request import urlopen

# Importing Datetime Libraries
from datetime import datetime, timedelta

# More Image Manipulation Options
from PIL import Image as PILImage

# Matplotlib Plotting Libraries
import matplotlib.pyplot as plt


# ## Figuring out where you want the files...

# ### Generic Image Capture from Website
# #### Arguments:
# * page - web address for saved image
# * FileEnd - What you want the end of the file to be named; specific to each map
# * loc - Location where you want the samed image to be placed
# * AxisTitle - What the image axis title would be - Currently not doing anything...

# In[8]:


def CurrentMap(page,FileEnd,loc):
    '''
    Parameters
    ------------    
    page: string
        website address for the image to be saved from 
    
    FileEnd: string
        desired saved image name
    
    loc: string
        location on computer for image to be saved to
    
    Returns
    ------------
    Filename: string
        complete name for file saved to computer
    '''
    
    print(page)
    now = datetime.now()
     # Your code where you can use urlopen
    with urlopen(page) as url:
        my_picture = url.read()
    
# open file for binary write and save picture
# picture_page[-4:] extracts extension eg. .gif
# (most image file extensions have three letters, otherwise modify)
    #Filename = str(Year)+"_"+str(Month)+\
    #"_"+str(Day)+"_"+str(Hour)+"_"+str(Minute)+"_"+FileEnd 
    Filename = '{0:%Y_%m_%d_%H_%M_}'.format(now)+FileEnd
    
    # fout will create and write to a new image file
    fout = open(loc+"/"+Filename, "wb")
    fout.write(my_picture)
    fout.close()
# test to see if it saved correctly
    #webbrowser.open(Filename)  
    
    #except urllib2.HTTPError, err:
    #    if err.code == 404:
    #        logging.exception("No Data from website")
    #        pass
    #    else:
    #        raise

    
    #file = StringIO(urllib.urlopen(page).read())
    
    

    urllib.request.urlretrieve(page, "local-filename.jpg")
    img = PILImage.open("local-filename.jpg")
    
    

    fig, ax = plt.subplots(figsize=(15, 8))
    #ax.set_title(AxisTitle+" "'{0:%Y %m %d %H}'.format(now))
    ax.imshow(img, interpolation='nearest')
    #plt.show()
    plt.close()
    print(Filename)


# In[ ]:


# Pull the current time
now = datetime.now() 

YeaR = now.strftime('%y')


# # Pull Images from Weather Websites
# ---------------------------------------------
# ### Credit to NOAA, NCAR, CU Boulder, WPC, SPC, NOHRSC
# 

# In[4]:


#########################################################################
# SPC Advacned Sounding - CONUS
#########################################################################
#https://www.spc.noaa.gov/exper/soundings/19022312_OBS/
Sounding_page="https://www.spc.noaa.gov/exper/soundings/"+YeaR+'{0:%m%d}'.format(now)+"12_OBS/DNR.gif" 
Sounding_FileEnd="SPC_Sounding.png"  
Sounding_AxisTitle="Surface Analysis (North America): "
Sounding = [Sounding_page,Sounding_FileEnd,Sounding_AxisTitle]


#########################################################################
# WPC Surface Anaylsis - North America
#########################################################################
SurfAnalNA_page="http://www.wpc.ncep.noaa.gov/sfc/90fwbg.gif" 
SurfAnalNA_FileEnd="Current_Surf_Analy_NorthAmerica.png"  
SurfAnalNA_AxisTitle="Surface Analysis (North America): "
SurfAnalNA = [SurfAnalNA_page,SurfAnalNA_FileEnd,SurfAnalNA_AxisTitle]


#########################################################################
# WPC Surface Anaylsis - CONUS
#########################################################################
SurfAnal_page="http://www.wpc.ncep.noaa.gov/sfc/namussfcwbg.gif" 
SurfAnal_FileEnd="Current_Surf_Analy.png"  
SurfAnal_AxisTitle="Surface Analysis: "
SurfAnal = [SurfAnal_page,SurfAnal_FileEnd,SurfAnal_AxisTitle]


#########################################################################
# WPC Surface Anaylsis - CONUS Simple
#########################################################################
SurfAnalSimple_page="http://www.wpc.ncep.noaa.gov/sfc/usfntsfc12wbg.gif"
SurfAnalSimple_FileEnd="Current_Surf_Analy_SIMPLE.png"  
SurfAnalSimple_AxisTitle="Surface Analysis (Simple): "
SurfAnalSimple = [SurfAnalSimple_page,SurfAnalSimple_FileEnd,SurfAnalSimple_AxisTitle]


#########################################################################
# US Warnings
#########################################################################
USWarnings_page="http://forecast.weather.gov/wwamap/png/US.png"
USWarnings_FileEnd="US_Warnings.png"
USWarnings_AxisTitle="US Warnings and Watches: "
USWarnings = [USWarnings_page,USWarnings_FileEnd,USWarnings_AxisTitle]


#########################################################################
# WPC Forecast - Day 1
#########################################################################
SrfcForecast1_page="http://www.wpc.ncep.noaa.gov/noaa/noaad1.gif"
SrfcForecast1_FileEnd="SrfcForecast_Day1.png"
SrfcForecast1_AxisTitle="Surface Forecast Day 1: "
SrfcForecast1 = [SrfcForecast1_page,SrfcForecast1_FileEnd,SrfcForecast1_AxisTitle]


#########################################################################
# WPC Forecast - Day 2
#########################################################################
SrfcForecast2_page="http://www.wpc.ncep.noaa.gov/noaa/noaad2.gif"
SrfcForecast2_FileEnd="SrfcForecast_Day2.png"
SrfcForecast2_AxisTitle="Surface Forecast Day 2: "
SrfcForecast2 = [SrfcForecast2_page,SrfcForecast2_FileEnd,SrfcForecast2_AxisTitle]


#########################################################################
# WPC Forecast - Day 3
#########################################################################
SrfcForecast3_page="http://www.wpc.ncep.noaa.gov/noaa/noaad3.gif"
SrfcForecast3_FileEnd="SrfcForecast_Day3.png"
SrfcForecast3_AxisTitle="Surface Forecast Day 3: "
SrfcForecast3 = [SrfcForecast3_page,SrfcForecast3_FileEnd,SrfcForecast3_AxisTitle]


#########################################################################
# WPC Fronts and Weather - Day 1
#########################################################################
WPCFrontsandWeather_page="http://www.wpc.ncep.noaa.gov/basicwx/92fndfd.gif"
WPCFrontsandWeather_FileEnd="WPCFrontsandWeather_Day1.png"
WPCFrontsandWeather_AxisTitle="Fronts and Weather Type Forecast Day 1: "
WPCFrontsandWeather = [WPCFrontsandWeather_page,WPCFrontsandWeather_FileEnd,WPCFrontsandWeather_AxisTitle]


#########################################################################
# WPC Fronts and Weather - Day 2
#########################################################################
WPCFrontsandWeather2_page="http://www.wpc.ncep.noaa.gov/basicwx/94fndfd.gif"
WPCFrontsandWeather2_FileEnd="WPCFrontsandWeather_Day2.png"
WPCFrontsandWeather2_AxisTitle="Fronts and Weather Type Forecast Day 2: "
WPCFrontsandWeather2 = [WPCFrontsandWeather2_page,WPCFrontsandWeather2_FileEnd,WPCFrontsandWeather2_AxisTitle]


#########################################################################
# WPC Fronts and Weather - Day 3
#########################################################################
WPCFrontsandWeather3_page="http://www.wpc.ncep.noaa.gov/basicwx/96fndfd.gif"
WPCFrontsandWeather3_FileEnd="WPCFrontsandWeather_Day3.png"
WPCFrontsandWeather3_AxisTitle="Fronts and Weather Type Forecast Day 3: "
WPCFrontsandWeather3 = [WPCFrontsandWeather3_page,WPCFrontsandWeather3_FileEnd,WPCFrontsandWeather3_AxisTitle]


#########################################################################
# WPC Fronts and Weather - Day 4
#########################################################################
WPCFrontsandWeather4_page="http://www.wpc.ncep.noaa.gov/basicwx/98fndfd.gif"
WPCFrontsandWeather4_FileEnd="WPCFrontsandWeather_Day4.png"
WPCFrontsandWeather4_AxisTitle="Fronts and Weather Type Forecast Day 4: "
WPCFrontsandWeather4 = [WPCFrontsandWeather4_page,WPCFrontsandWeather4_FileEnd,WPCFrontsandWeather4_AxisTitle]


#########################################################################
# Duane Tower, CU Boulder Meteograms
#########################################################################
Duane_page="http://foehn.colorado.edu/weather/atoc1/wxobs"        +'{0:%Y%m%d}'.format(now)+".png"
Duane_FileEnd="Current_Duane_Meteo.png" 
Duane_AxisTitle="Duane Meteorgram: "
Duane = [Duane_page,Duane_FileEnd,Duane_AxisTitle]


#########################################################################
# NOHRSC 24hr Snowfall Accumulation
#########################################################################
Snow24Hr_page="http://www.nohrsc.noaa.gov/snowfall_v2/data/"+'{0:%Y%m}'.format(now)+"/sfav2_CONUS_24h_"+'{0:%Y%m%d}'.format(now)+"12.png"
Snow24Hr_FileEnd="24hr Snow.png" 
Snow24Hr_AxisTitle="24 Hour Snow Accumulation: "
Snow24Hr = [Snow24Hr_page,Snow24Hr_FileEnd,Snow24Hr_AxisTitle]


#########################################################################
# CONUS Radar
#########################################################################
USRadar_page="http://radar.weather.gov/Conus/RadarImg/latest.gif"
USRadar_FileEnd="Current_US_Radar_LARGE.png" 
USRadar_AxisTitle="Current Radar: "
USRadar = [USRadar_page,USRadar_FileEnd,USRadar_AxisTitle]


#########################################################################
# Colorado Radar
#########################################################################
CORockRadar_page="http://radar.weather.gov/Conus/RadarImg/northrockies.gif" 
CORockRadar_FileEnd="Current_Rockies_Radar.png" 
CORockRadar_AxisTitle="Current Rockies Radar: "
CORockRadar = [CORockRadar_page,CORockRadar_FileEnd,CORockRadar_AxisTitle]


#########################################################################
# Convection Outlook - Day 1
#########################################################################
ConvDay1_page="http://www.spc.noaa.gov/products/outlook/day1otlk_1300_prt.gif"
ConvDay1_FileEnd="ConvDay1.png"
ConvDay1_AxisTitle="Convective Outlook Day 1: "
ConvDay1 = [ConvDay1_page,ConvDay1_FileEnd,ConvDay1_AxisTitle]


#########################################################################
# Tornado Outlook - Day 1
#########################################################################
ConvDay1_Torn_page="http://www.spc.noaa.gov/products/outlook/day1probotlk_1300_torn_prt.gif"
ConvDay1_Torn_FileEnd="ConvDay1_Tornado.png"
ConvDay1_Torn_AxisTitle="Convective Outlook Tornado Day 1: "
ConvDay1_Torn = [ConvDay1_Torn_page,ConvDay1_Torn_FileEnd,ConvDay1_Torn_AxisTitle]


#########################################################################
# Wind Outlook - Day 1
#########################################################################
ConvDay1_Wind_page="http://www.spc.noaa.gov/products/outlook/day1probotlk_1300_wind_prt.gif"
ConvDay1_Wind_FileEnd="ConvDay1_Wind.png"
ConvDay1_Wind_AxisTitle="Convective Outlook Wind Day 1: "
ConvDay1_Wind = [ConvDay1_Wind_page,ConvDay1_Wind_FileEnd,ConvDay1_Wind_AxisTitle]


#########################################################################
# Hail Outlook - Day 1
#########################################################################
ConvDay1_Hail_page="http://www.spc.noaa.gov/products/outlook/day1probotlk_1300_hail_prt.gif"
ConvDay1_Hail_FileEnd="ConvDay1_Hail.png"
ConvDay1_Hail_AxisTitle="Convective Outlook Hail Day 1: "
ConvDay1_Hail = [ConvDay1_Hail_page,ConvDay1_Hail_FileEnd,ConvDay1_Hail_AxisTitle]

ConvDay1_List = [ConvDay1,ConvDay1_Torn,ConvDay1_Wind,ConvDay1_Hail]


#########################################################################
# Convection Outlook, any - Day 2
#########################################################################
#https://www.spc.noaa.gov/products/outlook/day2otlk_1730.gif
ConvDay2_page="http://www.spc.noaa.gov/products/outlook/day2otlk_1730.gif"
ConvDay2_FileEnd="ConvDay2.png"
ConvDay2_AxisTitle="Convective Outlook Day 2: "
ConvDay2 = [ConvDay2_page,ConvDay2_FileEnd,ConvDay2_AxisTitle]

ConvDay2_any_page="http://www.spc.noaa.gov/products/outlook/day2probotlk_1730_any.gif"
ConvDay2_any_FileEnd="ConvDay2_AnyPercentage.png"
ConvDay2_any_AxisTitle="Convective Outlook Any Percentage Day 2: "
ConvDay2_any = [ConvDay2_any_page,ConvDay2_any_FileEnd,ConvDay2_any_AxisTitle]

ConvDay2_List = [ConvDay2,ConvDay2_any]


#########################################################################
# Snow Water Equivalent
#########################################################################
SnowWater_page="http://www.nohrsc.noaa.gov/snow_model/"+        "images/full/National/nsm_swe/"+'{0:%Y%m}'.format(now)+        "/nsm_swe_"+'{0:%Y%m%d}'.format(now)+"05_National.jpg"
SnowWater_FileEnd="Snow_Water_Eq.png" 
SnowWater_AxisTitle="Snow Water Equivalent: "
SnowWater = [SnowWater_page,SnowWater_FileEnd,SnowWater_AxisTitle]


#########################################################################
# 24 Hour Snow Accumulation
#########################################################################
#Snow24Hr_page="http://www.nohrsc.noaa.gov/snowfall_v2/data/"+\
#        str(Year)+str(Month)+"/sfav2_CONUS_24h_"+str(Year)+str(Month)+str(Day)+"12.png"
new_now = datetime.now() - timedelta(days=1)
Snow24Hr_page="http://www.nohrsc.noaa.gov/snowfall_v2/data/"+'{0:%Y%m}'.format(now)+"/sfav2_CONUS_24h_"+'{0:%Y%m}'.format(now)+'{0:%d}'.format(new_now)+"12.png"
Snow24Hr_FileEnd="24hr_Snow.png" 
Snow24Hr_AxisTitle="24 Hour Snow Accumulation: "
Snow24Hr = [Snow24Hr_page,Snow24Hr_FileEnd,Snow24Hr_AxisTitle]

#########################################################################
# RAP Surface Plots
#########################################################################
"http://weather.rap.ucar.edu/surface/displaySfc.php?region=den&endDate=20190326&endTime=-1&duration=0"
#SnowWater_page="http://www.nohrsc.noaa.gov/snow_model/"+\
#        "images/full/National/nsm_swe/"+'{0:%Y%m}'.format(now)+\
#        "/nsm_swe_"+'{0:%Y%m%d}'.format(now)+"05_National.jpg"
#SnowWater_FileEnd="Snow_Water_Eq.png" 
#SnowWater_AxisTitle="Snow Water Equivalent: "
#SnowWater = [SnowWater_page,SnowWater_FileEnd,SnowWater_AxisTitle]



# Making a final list of all the differnt lists that contain webpage, image name, and title
currentList = [SurfAnal,SurfAnalNA,SurfAnalSimple,WPCFrontsandWeather,WPCFrontsandWeather2,WPCFrontsandWeather3,WPCFrontsandWeather4,USRadar,CORockRadar,USWarnings,SrfcForecast1,SrfcForecast2,SrfcForecast3,Duane,ConvDay1,ConvDay1_Torn,ConvDay1_Wind,ConvDay1_Hail,ConvDay2,ConvDay2_any,SnowWater,Sounding] #ConvDay2_any ,Snow24Hr

# Same as above, just a shorter list for winter - exclude the convection maps
winterlist = [SurfAnal,SurfAnalNA,SurfAnalSimple,WPCFrontsandWeather,WPCFrontsandWeather2,WPCFrontsandWeather3,WPCFrontsandWeather4,USRadar,CORockRadar,USWarnings,SrfcForecast1,SrfcForecast2,SrfcForecast3,Duane,SnowWater,Sounding]

