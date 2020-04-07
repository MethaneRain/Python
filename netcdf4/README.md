## Using Python's NetCDF4 Package

```python
import netcdf4 as nc

ds = nc.Dataset("test.nc","w",format="NETCDF4")
```

Defining the axis size by name

---

```python
lons = np.arange(0,360,2.5) # This will give 144 longitudes, every 2.5 degrees
lats = np.arange(-90,92.5,2.5) # This will give 73 latitudes, every 2.5 degrees
```

Now the llength of the ats/lons can be used to create the dimension size

```python
# The first argument (lat/lon) will be the reference name used later 
# in the creation of the variables
ds.createDimension('lat', len(lats))
ds.createDimension('lon', len(lons))
```