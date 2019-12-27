# Different Model Variable Plots

#### These are from the MetPy and Unidata example Jupyter notebooks. As always a million thanks to the Devs for making these so easy and all the effort they put into their work.

The wonderful thing about these notebooks is the access to the THREDDS server and the almost endless amount of data available!

---

With the NCSS and Siphon package, there are several different ways of accessing the data, here are two that I use most often:

---

* Using the main web address of the product:

ex: GFS 20km CONUS

```Python
gfs = TDSCatalog('http://thredds-jetstream.unidata.ucar.edu/thredds/catalog/grib/'
                 'NCEP/GFS/CONUS_20km/catalog.xml')

dataset = list(gfs.datasets.values())[1]
#print(dataset.access_urls)

# Create NCSS object to access the NetcdfSubset
ncss = NCSS(dataset.access_urls['NetcdfSubset'])

# get current date and time
#now = forecast_times[0]
now = datetime(today_year,today_month,today_day,0,0)
# define time range you want the data for
start = now
print(start)
delt_t = 48
end = now + timedelta(hours=delt_t)

query = ncss.query()
query.time_range(start, end)
query.lonlat_box(north=60, south=20, east=310, west=230)
query.accept('netcdf4')
query.variables(precip_name).add_lonlat()


# Request data for the variables you want to use
data = ncss.get_data(query)
```

* Using a recurisve search from the top catalog to your desired product:

ex: National Blend of Models (NMB) CONUS Gridded Forecast

```Python
from siphon.catalog import TDSCatalog
top_cat = TDSCatalog('http://thredds.ucar.edu/thredds/catalog.xml')
ref_anl = top_cat.catalog_refs['Forecast Products and Analyses']
new_cat_anl = ref_anl.follow()
print(new_cat_anl)
>>>
Unidata THREDDS Data Server - NCEP models

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

model_anl = new_cat_anl.catalog_refs[13]
Prod = model_anl
print(Prod)
print("Product Catalog url:",model_anl.href)

>>>
National Model Blend CONUS Grids
Product Catalog url: https://thredds.ucar.edu/thredds/catalog/grib/NCEP/NBM/CONUS/catalog.xml

gfs_anl_cat = model_anl.follow()
ds_anl = gfs_anl_cat.datasets[1]
print("Variable Name:",ds_anl.name)
print("Path:",ds_anl.url_path)

>>>
Variable Name: Best National Model Blend CONUS Grids Time Series
Path: grib/NCEP/NBM/CONUS/Best
```
