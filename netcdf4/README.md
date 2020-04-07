## Using Python's NetCDF4 Package

```python
import netcdf4 as nc

ds = nc.Dataset("test.nc","w",format="NETCDF4")
```

Defining the axis size by name
---

```python
ds.createDimension('lat', )
ds.createDimension('lon', )
```