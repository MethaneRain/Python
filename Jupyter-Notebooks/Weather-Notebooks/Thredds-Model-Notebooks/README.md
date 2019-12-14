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

ex: NWS CONUS CONDUIT Gridded Frecast

```Python
from siphon.catalog import TDSCatalog
top_cat = TDSCatalog('http://thredds.ucar.edu/thredds/catalog.xml')
ref_anl = top_cat.catalog_refs['Forecast Products and Analyses']
new_cat_anl = ref_anl.follow()
model_anl = new_cat_anl.catalog_refs[1]
print("Product Catalog url:",model_anl.href)
gfs_anl_cat = model_anl.follow()
ds_anl = gfs_anl_cat.datasets[1]
print("Variable Name:",ds_anl.name)
print("Path:",ds_anl.url_path)

>>>
Product Catalog url: https://thredds.ucar.edu/thredds/catalog/grib/NCEP/NDFD/NWS/CONUS/CONDUIT/catalog.xml
Variable Name: Best National Weather Service CONUS Forecast Grids (CONDUIT) Time Series
Path: grib/NCEP/NDFD/NWS/CONUS/CONDUIT/Best
```
