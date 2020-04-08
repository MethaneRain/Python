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
new_ds = nc.Dataset("test.nc","r")

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
    
fig=plt.figure(figsize=(20,20))
      
ax = fig.add_subplot(1, 1, 1, projection=plotcrs) 
   
ax.coastlines('10m', color='black',alpha=0.5)
ax.add_feature(state_boundaries, edgecolor='black',alpha=0.5)
ax.add_feature(cfeature.LAKES,alpha=0.5)
ax.set_extent(extent, datacrs)
    
levels = np.arange(6000,8500,25)
    
hgt_contourfill=ax.contourf(Lon,Lat,press,levels, 
                    cmap=plt.cm.jet,transform=datacrs,alpha=0.6)

cb = plt.colorbar(hgt_contourfill,pad=0.02, shrink=0.45) # cax = cbaxes
cb.ax.tick_params(labelsize=15)
cb.ax.set_title('$hPa$', fontsize=15,horizontalalignment='center',y=1.01,x=.5)

    
ax.scatter(-104.9903, 39.7392, marker='*', c="k",transform=datacrs,s=205)

transform = datacrs._as_mpl_transform(ax)

ax.annotate('Denver', xy=(-106, 38.8), xycoords=transform,color="k")

   
plt.title('Made-Up Pressures',fontsize=30)
    
plt.savefig("test_press.png",bbox_inches="tight")      

plt.show()