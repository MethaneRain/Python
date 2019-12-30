# Different Model Variable Plots

#### These are from the MetPy and Unidata example Jupyter notebooks. As always a million thanks to the Devs for making these so easy and all the effort they put into their work.

The wonderful thing about these notebooks is the access to the THREDDS server and the almost endless amount of data available!

---

With the NCSS and Siphon package, there are several different ways of accessing the data, here are two that I use most often:

---

<h3> Using the main web address of the product:</h3>

ex: GFS 20km CONUS

If you want to specify the initialization hour GRIB file:
* in this case I'm grabbing the 00Z init hour of current day's catalog

```Python
from datetime import datetime, timedelta
now = datetime.utcnow()
today_year = now.year
today_hour = now.month
today_day = now.day
init_hour = '0000'

vort_name = "Absolute_vorticity_isobaric"
hgt_name = "Geopotential_height_isobaric"
mslp_name = "MSLP_Eta_model_reduction_msl"

# Request the GFS data from the thredds server
gfs = TDSCatalog(f'http://thredds-jetstream.unidata.ucar.edu/thredds/catalog/grib/NCEP/GFS/CONUS_20km/GFS_CONUS_20km_{today_year}{today_month}{today_day}_{init_hour}.grib2/catalog.xml')

print(list(gfs.datasets)[0])

>>>
GFS_CONUS_20km_20191230_0000.grib2
```

```Python
dataset = list(gfs.datasets.values())[0]

# Create NCSS object to access the NetcdfSubset
ncss = NCSS(dataset.access_urls['NetcdfSubset'])

# get current date and time
now = datetime(today_year,today_month,today_day,init_hour,0)
# define time range you want the data for
start = now
print(start)

>>>
2019-12-30 00:00:00
```

```Python
delta_t = 48
end = now + timedelta(hours=delta_t)

query = ncss.query()
query.time_range(start, end)
Lat = query.lonlat_box(north=60, south=20, east=310, west=230)
query.accept('netcdf4')
query.variables(vort_name,hgt_name,mslp_name).add_lonlat(True)


# Request data for the variables you want to use
data = ncss.get_data(query)
```

Or grabbing the desired date range from the Best catalog entry ():

```Python
gfs = TDSCatalog('http://thredds-jetstream.unidata.ucar.edu/thredds/catalog/grib/'
                 'NCEP/GFS/CONUS_20km/catalog.xml')

dataset = list(gfs.datasets.values())[1]
#print(dataset.access_urls)

# Create NCSS object to access the NetcdfSubset
ncss = NCSS(dataset.access_urls['NetcdfSubset'])

# get current date and time
now = datetime(today_year,today_month,today_day,0,0)
# define time range you want the data for
start = now
print(start)
delta_t = 48
end = now + timedelta(hours=delta_t)

query = ncss.query()
query.time_range(start, end)
query.lonlat_box(north=60, south=20, east=310, west=230)
query.accept('netcdf4')
query.variables(precip_name).add_lonlat()


# Request data for the variables you want to use
data = ncss.get_data(query)
```

---

<h3> Using a recurisve search from the top catalog to your desired product:</h3>

ex: National Blend of Models (NMB) CONUS Gridded Forecast

```Python
from siphon.catalog import TDSCatalog
top_cat = TDSCatalog('http://thredds.ucar.edu/thredds/catalog.xml')
ref_anl = top_cat.catalog_refs['Forecast Products and Analyses']
new_cat_anl = ref_anl.follow()
print(new_cat_anl)

>>>
Unidata THREDDS Data Server - NCEP models
```

```Python
j = 0
for i in new_cat_anl.catalog_refs:
    print(f'Index {j}: {i}')
    j += 1
    
>>>
Index 0: National Weather Service CONUS Forecast Grids (NOAAPORT)
Index 1: National Weather Service CONUS Forecast Grids (CONDUIT)
Index 2: Storm Prediction Center CONUS Forecast Grids
Index 3: Climate Prediction Center CONUS Forecast Grids
Index 4: Real Time Mesoscale Analysis 2.5 km
Index 5: Real Time Mesoscale Analysis GUAM 2.5 km
Index 6: MRMS Base Reflectivity
Index 7: MRMS Model-derived fields
Index 8: MRMS NLDN Analysis
Index 9: MRMS Precipitation Analysis
Index 10: MRMS Radar Analysis
Index 11: MRMS Low-Level Rotation Tracks
Index 12: MRMS Mid-Level Rotation Tracks
Index 13: National Model Blend CONUS Grids
Index 14: National Model Blend Oceanic Grids
Index 15: National Model Blend Alaska Grids
Index 16: National Model Blend Hawaii Grids
Index 17: National Model Blend Puerto Rico Grids
```

```Python
model_anl = new_cat_anl.catalog_refs[13]
Prod = model_anl
print(Prod)
print("Product Catalog url:",model_anl.href)

>>>
National Model Blend CONUS Grids
Product Catalog url: https://thredds.ucar.edu/thredds/catalog/grib/NCEP/NBM/CONUS/catalog.xml
```

```Python
gfs_anl_cat = model_anl.follow()
ds_anl = gfs_anl_cat.datasets[1]
print("Variable Name:",ds_anl.name)
print("Path:",ds_anl.url_path)

>>>
Variable Name: Best National Model Blend CONUS Grids Time Series
Path: grib/NCEP/NBM/CONUS/Best
```
