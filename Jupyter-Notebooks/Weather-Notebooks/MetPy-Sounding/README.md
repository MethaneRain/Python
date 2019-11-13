# My small take on the MetPy basic sounding skew-T Plots
## I've created a dictionary with the station names and station ID.

    StationsList = ["Wallops Island, VA","Upton, NY","Chatham, MA","Albany, NY","Sterling, VA","Gray, ME",\
    "Buffalo, NY","Pittsburgh, PA","Wilmington, OH","White Lake, MI","Blacksburg, VA","Greensboro, NC",\
    "Newport, NC","Charleston, SC","Jacksonville, FL","Tampa Bay, FL","Miami, FL","Tallahassee, FL",\
    "Shelby Cnty. Airport, AL","Peachtree City, GA","Nashville, TN","Gaylord, MI","Green Bay, WI","Davenport, IA",\
    "Lincoln, IL","Springfield, MO","Little Rock, AR","Jackson Thomas, MS","Slidell Muni., LA","Lake Charles, LA",\
    "Shreveport, LA","Norman, OK","Dodge City, KS","Topeka, KS","Omaha, NE","Chanhassen, MN","International Falls, MN",\
    "Aberdeen, SD","Bismarck, ND","Rapid City, SD","North Platte, NE","Amarillo, TX","Midland, TX","Del Rio, TX",\
    "Corpus Christi, TX","Brownsville, TX","Ft. Worth, TX","Santa Teresa, NM","Albuquerque, NM","Denver, CO","Grand Juncion, CO",\
    "Riverton, WY","Glasgow, MT","Great Falls, MT","Salt Lake City, UT","Flagstaff, AZ","Tuscon, AZ","Yuma Prarie Grnds, AZ","Las Vegas, NV",\
    "Elko, NV","Boise, ID","Spokane, WA","Quillayute, WA","Salem, OR","Medford, OR","Reno, NV",\
    "Oakland, CA","Vandenberg Air Force Base, CA","San Diego, CA"]

    StationNumList = [72402,72501,74494,72518,72403,74389,72528,72520,72426,72632,72318,72317,72305,72208,72206,72210,\
    72202,72214,72230,72215,72327,72635,72645,74455,74560,72440,72340,72235,72233,72240,72248,72357,72451,72456,\
    72558,72649,72747,72659,72764,72662,72562,72363,72265,72261,72251,72250,72249,72364,72365,72469,72476,72672,\
    72768,72776,72572,72376,72274,74004,72388,72582,72681,72786,72797,72694,72597,72489,72493,72393,72293]

    StationFinal = dict(zip(StationsList,StationNumList))

## I've also made a mapping function to expedite plotting different stations with the opotions to turn on/off CAPE and CIN plotting.
```ruby
        # Mapperz(data_date,station,filename date,image_save_path,CIN_CAPE=None)
        Mapperz(dateCurrent,"DNR",date,im_save_path,False)
```
![](https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/MetPy-Sounding/Sample-Maps/Resized_Sounding_DNR_2019031612.png)
```ruby
        Mapperz(dateCurrent,"DNR",date,im_save_path,True)
```        
![](https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/MetPy-Sounding/Sample-Maps/Resized_Sounding_DNR_2019031612_CIN.png)
