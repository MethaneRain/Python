## Using Python's NetCDF4 Package

```python
import netcdf4 as nc
import numpy as np

ds = nc.Dataset("test.nc","w",format="NETCDF4")
```

### Creating a new ```nc``` file
---

#### Defining the axis size by name

```python
lon_vals = np.arange(0,360,2.5) # This will give 144 longitudes, every 2.5 degrees
lat_vals = np.arange(-90,92.5,2.5) # This will give 73 latitudes, every 2.5 degrees
```

Now the length of the lats/lons can be used to create the dimension size

```python
# The first argument (lat/lon) will be the reference name used later in the creation of the variables
ds.createDimension('lat', len(lat_vals))
ds.createDimension('lon', len(lon_vals))
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
lat = ds.createVariable('lats', dtype('double').char, ('lat'))
lat.standard_name = 'latitude'
lat.long_name = 'latitude'
lat.units = 'degrees_north'
lat.axis = 'Y'

# create longitude axis
lon = ds.createVariable('lons', dtype('double').char, ('lon'))
lon.standard_name = 'longitude'
lon.long_name = 'longitude'
lon.units = 'degrees_east'
lon.axis = 'X'

# create (made-up) pressure axis
press = ds.createVariable('pres', dtype('double').char, ('lat', 'lon'))
press.standard_name = 'pressure'
press.long_name = 'Made-Up Pressure'
press.units = 'hPa'
```
We can arbitrarily assign values to the pressure array. It must be 2d since it will take a value at every lat/lon pairing. One way to accomplish this quickly is to use ```numpy.arange()```:

```python
pres_vals = np.arange(73*144).reshape(73,144)
pres_vals.shape

>>>
(73, 144)
```

This will just make a set of numbers from 0 to 73*144 and fill them accordingly 

In the variable creation above there will be lat and lon variables that are 1d each and a press variable that will be 2d (73,144)

#### Assigning the values to the new variables

The only thing left to do is just assign the varibales lat, lon, and press to their values:

```python
lon[:] = lon_vals
lat[:] = lat_vals
press[:] = pres_vals
```