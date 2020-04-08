#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 00:11:32 2020

@author: chowdahead
"""

                            # Test new netcdf file
#-----------------------------------------------------------------------------#
import netCDF4 as nc
import numpy as np
new_ds = nc.Dataset("test.nc")

print(list(new_ds.variables))

# Build our backgroud map and plotting control
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# Needed for plot stuff
import matplotlib.pyplot as plt

# Set pur lat/lon box for plotting 
#extent = [-125,-70,20,50]
extent = [-125,-70,25,48]

# Set projection of data
datacrs = ccrs.PlateCarree()

# Set projection of map
plotcrs = ccrs.LambertConformal()

# Add Map Features
country_borders = cfeature.NaturalEarthFeature(category='cultural',
    name='admin_0_countries',scale='50m', facecolor='none')

state_boundaries = cfeature.NaturalEarthFeature(category='cultural',
        name='admin_1_states_provinces_lakes', scale='50m', facecolor='none')

press = new_ds.variables['pres'][:]
Lon = new_ds.variables['lons'][:]
Lat = new_ds.variables['lats'][:]
