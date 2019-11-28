# Access GFS data from gribs file types
<p align="center">
  <img src="https://www.earthsystemcog.org/site_media/logos/gfs4c.png" width="30%">
</p>


## This can be very helpful as a lot of model data and other weather data are in this file type
---
I had to create a separate ```env``` for working with ```pygrib```, my libraries weren't playing nicely otherwise.

In the terminal:

$ conda create -n test-pygrib python=3.7

You must install all your Python libraries again since this is a blank slate environment

$ conda activate test-pygrib

---
GFS Analysis and Forecast:
* Some days are missing...

* Roughly 10 days behind current date

* https://www.ncdc.noaa.gov/data-access/model-data/model-datasets/global-forcast-system-gfs

---

```grbs``` will be the new instance of the data and file and

```grb``` will be the lines of the file read in

```python
grbs = pygrib.open("gfs_4_20191110_0000_012.grb2")
grb = grbs.read()
```
There are so many variables, we can just print out a couple to see the data in raw form

```python
grb[0:10]
>>>
[1:Cloud mixing ratio:kg kg**-1 (instant):regular_ll:hybrid:level 1:fcst time 3 hrs:from 201911150000,
 2:Ice water mixing ratio:kg kg**-1 (instant):regular_ll:hybrid:level 1:fcst time 3 hrs:from 201911150000,
 3:Rain mixing ratio:kg kg**-1 (instant):regular_ll:hybrid:level 1:fcst time 3 hrs:from 201911150000,
 4:Snow mixing ratio:kg kg**-1 (instant):regular_ll:hybrid:level 1:fcst time 3 hrs:from 201911150000,
 5:Graupel (snow pellets):kg kg**-1 (instant):regular_ll:hybrid:level 1:fcst time 3 hrs:from 201911150000,
 6:Maximum/Composite radar reflectivity:dB (instant):regular_ll:atmosphere:level 0 -:fcst time 3 hrs:from 201911150000,
 7:Visibility:m (instant):regular_ll:surface:level 0:fcst time 3 hrs:from 201911150000,
 8:U component of wind:m s**-1 (instant):regular_ll:unknown:level 0:fcst time 3 hrs:from 201911150000,
 9:V component of wind:m s**-1 (instant):regular_ll:unknown:level 0:fcst time 3 hrs:from 201911150000,
 10:Ventilation Rate:m**2 s**-1 (instant):regular_ll:unknown:level 0:fcst time 3 hrs:from 201911150000]
>>>
```




---

There are several ways to access data, lets take a look a some:
---

#### Simplest Method

pygrib's ```.select(kwargs)``` is a sudo search function. If you know the exact long name of the variable in the dataset, you can call the ```name``` function.

ex:
```Python
grbs.select(name="MSLP")

>>>
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-20-ec68fde650b7> in <module>
----> 1 grbs.select(name="MSLP")

pygrib.pyx in pygrib.open.select()

ValueError: no matches found
>>>
```

But knowing the GFS Forecast 1/2 or Full degrees grib files:
```Python
grbs.select(name="MSLP (Eta model reduction)")

>>>
[419:MSLP (Eta model reduction):Pa (instant):regular_ll:meanSea:level 0:fcst time 3 hrs:from 201911150000]
>>>
```

```Python
type(grbs.select(name="MSLP (Eta model reduction)"))
>>>
list
>>>
```

So the select function will return a list based off the kwargs

The level can also be a kwarg to search by:

ex. ```Absolute vorticity:s**-1 (instant):regular_ll:isobaricInhPa:level 50000 Pa```

!! The ```grbs.select(level)``` kwarg is by hPa,  but the variable info has it in Pa !!
```Python
grbs.select(name="Absolute vorticity",level=500)[0] # [0]to grab it out of the returned list
>>>
230:Absolute vorticity:s**-1 (instant):regular_ll:isobaricInhPa:level 50000 Pa:fcst time 3 hrs:from 201911150000
>>>
```



---

Now that we can grab variables we can grab specific values, lats, and lons based off kwargs and/or heights.

The lat/lons can be taken from the data as 2d arrays each
```Python
hgt_500 = grbs.select(name="Geopotential Height",level=500)[0]
lat, lon = hgt_500.latlons()
lat, lon
>>>
(array([[ 90. ,  90. ,  90. , ...,  90. ,  90. ,  90. ],
        [ 89.5,  89.5,  89.5, ...,  89.5,  89.5,  89.5],
        [ 89. ,  89. ,  89. , ...,  89. ,  89. ,  89. ],
        ...,
        [-89. , -89. , -89. , ..., -89. , -89. , -89. ],
        [-89.5, -89.5, -89.5, ..., -89.5, -89.5, -89.5],
        [-90. , -90. , -90. , ..., -90. , -90. , -90. ]]),
 array([[  0. ,   0.5,   1. , ..., 358.5, 359. , 359.5],
        [  0. ,   0.5,   1. , ..., 358.5, 359. , 359.5],
        [  0. ,   0.5,   1. , ..., 358.5, 359. , 359.5],
        ...,
        [  0. ,   0.5,   1. , ..., 358.5, 359. , 359.5],
        [  0. ,   0.5,   1. , ..., 358.5, 359. , 359.5],
        [  0. ,   0.5,   1. , ..., 358.5, 359. , 359.5]]))
>>>
```

For each variable there are 3 arrays with values, lat, lon:
 ```Python
hgt_500.data()
 >>>
 (array([[5035.2534, 5035.2534, 5035.2534, ..., 5035.2534, 5035.2534,
          5035.2534],
         [5033.2935, 5033.2334, 5033.174 , ..., 5033.4937, 5033.4336,
          5033.3535],
         [5033.7935, 5033.694 , 5033.5737, ..., 5034.154 , 5034.0337,
          5033.9136],
         ...,
         [5046.4136, 5046.5137, 5046.614 , ..., 5046.0938, 5046.214 ,
          5046.3135],
         [5057.194 , 5057.2734, 5057.3135, ..., 5057.0537, 5057.114 ,
          5057.154 ],
         [5065.7734, 5065.7734, 5065.7734, ..., 5065.7734, 5065.7734,
          5065.7734]], dtype=float32),
  array([[ 90. ,  90. ,  90. , ...,  90. ,  90. ,  90. ],
         [ 89.5,  89.5,  89.5, ...,  89.5,  89.5,  89.5],
         [ 89. ,  89. ,  89. , ...,  89. ,  89. ,  89. ],
         ...,
         [-89. , -89. , -89. , ..., -89. , -89. , -89. ],
         [-89.5, -89.5, -89.5, ..., -89.5, -89.5, -89.5],
         [-90. , -90. , -90. , ..., -90. , -90. , -90. ]]),
  array([[  0. ,   0.5,   1. , ..., 358.5, 359. , 359.5],
         [  0. ,   0.5,   1. , ..., 358.5, 359. , 359.5],
         [  0. ,   0.5,   1. , ..., 358.5, 359. , 359.5],
         ...,
         [  0. ,   0.5,   1. , ..., 358.5, 359. , 359.5],
         [  0. ,   0.5,   1. , ..., 358.5, 359. , 359.5],
         [  0. ,   0.5,   1. , ..., 358.5, 359. , 359.5]]))
 >>>
 ```

The actual values can be pulled for each lat/lon pair. This means the data is in a 2d array as well.
The values can be extracted by running ```grbs.select()[0].data()[0]```

```Python
hgt_500.data()[0]
>>>
array([[5035.2534, 5035.2534, 5035.2534, ..., 5035.2534, 5035.2534,
         5035.2534],
        [5033.2935, 5033.2334, 5033.174 , ..., 5033.4937, 5033.4336,
         5033.3535],
        [5033.7935, 5033.694 , 5033.5737, ..., 5034.154 , 5034.0337,
         5033.9136],
        ...,
        [5046.4136, 5046.5137, 5046.614 , ..., 5046.0938, 5046.214 ,
         5046.3135],
        [5057.194 , 5057.2734, 5057.3135, ..., 5057.0537, 5057.114 ,
         5057.154 ],
        [5065.7734, 5065.7734, 5065.7734, ..., 5065.7734, 5065.7734,
         5065.7734]], dtype=float32)
>>>
```
Pygrib also allows for spatial subsetting with ```lat1, lat2, lon1, lon2``` calls
```Python
hgt_500 = grbs.select(name="Geopotential Height",level=500)[0].data(lat1=20,lat2=70,lon1=220,lon2=320)
```


---
Plot
---
![500mb Heights and Vorticity w/ MSLP](https://raw.githubusercontent.com/MethaneRain/Python-Jupyter/master/Jupyter-Notebooks/Gribs-Examples/GFS_4_mslp_500_hgts_vort_20191115_0600Z_F030.png)
