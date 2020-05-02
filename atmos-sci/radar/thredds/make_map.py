#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 22:26:03 2020

@author: Justin Richling
"""

def make_map(data,LatLonBox):  
    import cartopy.ccrs as crs
    import cartopy.feature as cfeature
    import cartopy.io.shapereader as shpreader
    import matplotlib.pyplot as plt
    
    proj = crs.LambertConformal(central_longitude=data.RadarLongitude,
                                       central_latitude=data.RadarLatitude)

    fig = plt.figure(figsize=(17,11))
    ax = plt.subplot(111,projection=proj)
    
    ax.coastlines('50m', 'black', linewidth=2, zorder=2)

    reader = shpreader.Reader('/Users/chowdahead/Downloads/countyl010g_shp_nt00964/countyl010g.shp')
    counties = list(reader.geometries())
    COUNTIES = cfeature.ShapelyFeature(counties,crs.PlateCarree())
    ax.add_feature(COUNTIES, facecolor='none',edgecolor='r')
    # Grab state borders
    state_borders = cfeature.NaturalEarthFeature(
                category='cultural', name='admin_1_states_provinces_lines',
                scale='50m', facecolor='none')
    ax.add_feature(state_borders, edgecolor='w', linewidth=1, zorder=3)
    ocean = cfeature.NaturalEarthFeature('physical', 'ocean', scale='50m',
                                                edgecolor='face',
                                                facecolor=cfeature.COLORS['water'])
    land = cfeature.NaturalEarthFeature('physical', 'land', scale='50m',
                                               edgecolor='face',
                                               facecolor="k")

    ax.add_feature(ocean, zorder=-1)
    ax.add_feature(land, zorder=-1)
    ax.set_facecolor('black')
    
    ax.set_extent(LatLonBox,cfeature.PlateCarree())
    
    return fig,ax,proj