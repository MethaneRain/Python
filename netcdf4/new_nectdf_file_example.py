#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 23:55:33 2020

@author: chowdahead
"""
import netCDF4 as nc
import numpy as np
from numpy import dtype

ds = nc.Dataset("test.nc","w",format="NETCDF4")

lon_vals = np.arange(0,360,2.5) # This will give 144 longitudes, every 2.5 degrees
lat_vals = np.arange(-90,92.5,2.5) # This will give 73 latitudes, every 2.5 degrees

ds.createDimension('lat', len(lat_vals))
ds.createDimension('lon', len(lon_vals))

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

pres_vals = np.arange(73*144).reshape(73,144)
print(pres_vals.shape)

lon[:] = lon_vals
lat[:] = lat_vals
press[:] = pres_vals

ds.close()







