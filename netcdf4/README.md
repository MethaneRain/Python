## Using Python's NetCDF4 Package

```python
import netcdf4 as nc

ds = nc.Dataset("test.nc","w",format="NETCDF4")
```

### Creating a new ```nc``` file
---

#### Defining the axis size by name

```python
lons = np.arange(0,360,2.5) # This will give 144 longitudes, every 2.5 degrees
lats = np.arange(-90,92.5,2.5) # This will give 73 latitudes, every 2.5 degrees
```

Now the length of the lats/lons can be used to create the dimension size

```python
# The first argument (lat/lon) will be the reference name used later in the creation of the variables
ds.createDimension('lat', len(lats))
ds.createDimension('lon', len(lons))
```

#### Creating the variable axes

The netcdf4 method ```createVariable``` takes necessary arguments:
* Name - first arg
* Data Type - second arg
* Dimension Name - third arg (must match the name given in the ```createDimension``` call above)

Various pieces of metadata can be assigned as well such as:
* standard_name
* long_name
* units
* axis
* group
* etc

```python
# create latitude axis
lat = ncout.createVariable('lats', dtype('double').char, ('lat'))
lat.standard_name = 'latitude'
lat.long_name = 'latitude'
lat.units = 'degrees_north'
lat.axis = 'Y'

# create longitude axis
lon = ncout.createVariable('lons', dtype('double').char, ('lon'))
lon.standard_name = 'longitude'
lon.long_name = 'longitude'
lon.units = 'degrees_east'
lon.axis = 'X'

# create (made-up) pressure axis
press = ncout.createVariable('pres', dtype('double').char, ('lat', 'lon'))
press.standard_name = 'pressure'
press.long_name = 'Made-Up Pressure'
press.units = 'hPa'
```

In the variable creation above there will be lat and lon variables that are 1d each and a press variable that will be 2d (73,144)