#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Random Library Imports
import os,glob,io,sys,time

# Importing Datetime Libraries
from datetime import datetime, timedelta

from netCDF4 import num2date

# CartoPy Map Plotting Libraires
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.io.shapereader as shpreader
from pyproj import Proj 

# Numerical and Scientific Libraries
import numpy as np
import scipy.ndimage as ndimage
from scipy.ndimage import gaussian_filter

# Accessing Data from External Databases via XLM Catalog
from siphon.ncss import NCSS
from siphon.catalog import TDSCatalog

# MetPy Libraries
import metpy
import metpy.calc as mpcalc
from metpy.units import masked_array, units
from metpy.plots import ctables
mycmap = ctables.registry.get_colortable("NWSReflectivity")
from metpy.plots import add_metpy_logo

# Matplotlib Plotting Libraries
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
import matplotlib.colors as mcolors
from matplotlib.colors import LogNorm, Normalize
import matplotlib as mpl
from mpl_toolkits.axes_grid1 import make_axes_locatable, axes_size
from matplotlib.colors import LinearSegmentedColormap

# PV widgits imports
import ipywidgets as widgets


# In[2]:


# Thanks to the crew over at Metpy for this handy little function
def find_time_var(var, time_basename='time'):
    for coord_name in var.coordinates.split():
        if coord_name.startswith(time_basename):
            return coord_name
    raise ValueError('No time variable found for ' + var.name)


# In[3]:


# MetPy Function
def plot_maxmin_points(AX,lon, lat, data, extrema, nsize, symbol, color='k',
                       plotValue=True, transform=None):
    """
    This function will find and plot relative maximum and minimum for a 2D grid. The function
    can be used to plot an H for maximum values (e.g., High pressure) and an L for minimum
    values (e.g., low pressue). It is best to used filetered data to obtain  a synoptic scale
    max/min value. The symbol text can be set to a string value and optionally the color of the
    symbol and any plotted value can be set with the parameter color
    lon = plotting longitude values (2D)
    lat = plotting latitude values (2D)
    data = 2D data that you wish to plot the max/min symbol placement
    extrema = Either a value of max for Maximum Values or min for Minimum Values
    nsize = Size of the grid box to filter the max and min values to plot a reasonable number
    symbol = String to be placed at location of max/min value
    color = String matplotlib colorname to plot the symbol (and numerica value, if plotted)
    plot_value = Boolean (True/False) of whether to plot the numeric value of max/min point
    The max/min symbol will be plotted on the current axes within the bounding frame
    (e.g., clip_on=True)
    """
    from scipy.ndimage.filters import maximum_filter, minimum_filter

    if (extrema == 'max'):
        data_ext = maximum_filter(data, nsize, mode='nearest')
    elif (extrema == 'min'):
        data_ext = minimum_filter(data, nsize, mode='nearest')
    else:
        raise ValueError('Value for hilo must be either max or min')

    mxy, mxx = np.where(data_ext == data)
    #print mxy,mxx

    for i in range(len(mxy)):
        ax.text(lon[mxy[i], mxx[i]], lat[mxy[i], mxx[i]], symbol, color=color, size=24,
                clip_on=True, horizontalalignment='center', verticalalignment='center',
                transform=transform)
        ax.text(lon[mxy[i], mxx[i]], lat[mxy[i], mxx[i]],
                '\n' + str(np.int(data[mxy[i], mxx[i]])),
                color=color, size=12, clip_on=True, fontweight='bold',
                horizontalalignment='center', verticalalignment='top', transform=transform)
        
        #AX.text(lon[mxx[i]], lat[mxy[i]], symbol, color=color, size=24,
        #        clip_on=True, horizontalalignment='center', verticalalignment='center',
        #        transform=transform)
        #AX.text(lon[mxx[i]], lat[mxy[i]],
        #        '\n' + str(np.int(data[mxy[i], mxx[i]])),
        #        color=color, size=12, clip_on=True, fontweight='bold',
        #        horizontalalignment='center', verticalalignment='top', transform=transform)


# In[4]:


# Set Projection of Data
datacrs = ccrs.PlateCarree()
#datacrs= ccrs.LambertConformal()

# Set Projection of Plot
plotcrs = ccrs.LambertConformal(central_latitude=[30, 60], central_longitude=-100)
#plotcrs = ccrs.PlateCarree()
# Add Map Features
states_provinces = cfeature.NaturalEarthFeature(category='cultural',
    name='admin_1_states_provinces_lakes',scale='50m', facecolor='none')

country_borders = cfeature.NaturalEarthFeature(category='cultural',
    name='admin_0_countries',scale='50m', facecolor='none')

# Colorbar Axis Placement (under figure)
colorbar_axis = [0.183, 0.09, 0.659, 0.03] # [left, bottom, width, height]

# Lat/Lon Extents [lon0,lon1,lat0,lat1]
extent = [-130., -70, 20., 60.]


# In[17]:






now = datetime.utcnow()
#now = datetime(2019,3,5,18,0)
today_day = int('{0:%d}'.format(now))
today_month = int('{0:%m}'.format(now))
today_year = int('{0:%Y}'.format(now))
print(today_month,today_day,today_year)

forecast_times = []

for i in range(4,8):
    forecast_times.append(datetime(today_year,today_month,today_day,i*3,0))
for i in range(0,5):
    forecast_times.append(datetime(today_year,today_month,today_day+1,i*3,0))
#for i in range(0,8):
#    forecast_times.append(datetime(today_year,today_month,today_day+1,i*3,0))
#for i in range(0,8):
#    forecast_times.append(datetime(today_year,today_month,today_day+2,i*3,0))
#for i in range(0,8):
#    forecast_times.append(datetime(today_year,today_month,today_day+3,i*3,0))
forecast_times

# Set a path to save the plots with string format for the date to set the month and day 
im_save_path = "/path/to/saved/files/"
im_save_path ="/Users/chowdahead/Desktop/Weather_Blog/"+str(today_year)+'/{0:%m_%d}'.format(now)+"/"
print(im_save_path)

# Check to see if the folder already exists, if not create it
if not os.path.isdir(im_save_path):
    os.makedirs(im_save_path)












for i in forecast_times:
    
    from siphon.catalog import TDSCatalog
    top_cat = TDSCatalog('http://thredds.ucar.edu/thredds/catalog.xml')
    ref = top_cat.catalog_refs['Forecast Model Data']
    new_cat = ref.follow()
    model = new_cat.catalog_refs[32]
    gfs_cat = model.follow()
    ds = gfs_cat.datasets[1]
    
    subset = ds.subset()
    query_data = subset.query()
    query_data.lonlat_box(west=-130, east=-50, south=10, north=60)

        # Allow for NetCDF files
    query_data.accept('netcdf4')
    query_data.time(i)
    data = query_data.variables("Potential_temperature_height_above_ground",
                                'MSLP_MAPS_System_Reduction_msl').add_lonlat()
    #print(data.variables["Precipitation_rate_surface"].)
        # Finally attempt to access the data
    data = subset.get_data(query_data)
    RADAR = data.variables["Potential_temperature_height_above_ground"][:].squeeze()
    # Grab MSLP and smooth, use MetPy Units module for conversion
    EMSL = data.variables['MSLP_MAPS_System_Reduction_msl'][:] * units.Pa
    EMSL.ito('hPa')
    mslp = gaussian_filter(EMSL[0], sigma=3.0)
    
    #RADAR = RADAR*39.3701
    #RADAR = np.ma.masked_where(RADAR < 0.1,RADAR)
    lat = data.variables['lat'][:].squeeze()
    lon = data.variables['lon'][:].squeeze()

    time_var = data.variables[find_time_var(data.variables['Potential_temperature_height_above_ground'])]

    # Convert number of hours since the reference time into an actual date
    time_final = num2date(time_var[:].squeeze(), time_var.units)
    print(str(time_final)[:4]+"_"+str(time_final)[5:7]+"_"+str(time_final)[8:10]+"_"+str(time_final)[11:13]+"Z")
    file_time = str(time_final)[:4]+"_"+str(time_final)[5:7]+"_"+str(time_final)[8:10]+"_"+str(time_final)[11:13]+"Z"


    
    # Create new figure
    fig = plt.figure(figsize=(17., 11.))

    add_metpy_logo(fig, 30, 1000, size='small')

    # Add the map and set the extent
    ax = plt.subplot(111, projection=plotcrs)
    #Set the lat and lon boundaries
    ax.set_extent(extent, datacrs)
    
    
    #reader = shpreader.Reader('countyl010g_shp_nt00964/countyl010g.shp')

    #counties = list(reader.geometries())

    #COUNTIES = cfeature.ShapelyFeature(counties,datacrs) #, plotcrs

   
    #ax.add_feature(cfeature.LAND.with_scale('50m'))
    #ax.add_feature(cfeature.OCEAN.with_scale('50m'))
    #ax.add_feature(cfeature.LAKES.with_scale('50m'))
    #ax.add_feature(COUNTIES, facecolor='none', edgecolor='gray')
    
    # Add state boundaries to plot
    ax.add_feature(states_provinces, edgecolor='blue', linewidth=1)

    # Add country borders to plot
    ax.add_feature(country_borders, edgecolor='black', linewidth=1)

    # Labeling Denver with a star
    ax.scatter(-104.9903, 39.7392, marker='*', c="grey",transform=datacrs,s=150)
    transform = datacrs._as_mpl_transform(ax)
    #ax.annotate('Denver', xy=(-104.9903, 39.1392), xycoords=transform,size=13) #,fontproperties=()

    # Plot Title
    plt.title('2m Potential Temperature',loc='left',fontsize=16)
    plt.title(' {0:%d %B %Y %H:%MZ}'.format(time_final),loc='right',fontsize=16)
    #RADAR_levs = np.arange(0,2,.05)
    
    lev = np.arange(240,320,5)
    cs = ax.contour(lon,lat, RADAR,lev,cmap="nipy_spectral",transform=datacrs)
    cbar = plt.colorbar(cs, orientation='vertical',pad=0.005,aspect=50)

                                            # MSLP
#---------------------------------------------------------------------------------------------------
    clevmslp = np.arange(800., 1120., 4)
    cs2 = ax.contour(lon, lat, mslp, clevmslp, colors='k', linewidths=1.25,
                 linestyles='solid', transform=datacrs)
    #plt.clabel(cs2, **kw_clabels)

                                            # High and Low Symbols
#---------------------------------------------------------------------------------------------------
    plot_maxmin_points(ax,lon, lat, mslp, 'max', 50, symbol='H', color='b',  transform=datacrs)
    plot_maxmin_points(ax,lon, lat, mslp, 'min', 25, symbol='L', color='r', transform=datacrs)
    

    RAP_theta = im_save_path+"RAP/Theta/"
    if not os.path.isdir(RAP_theta):
        os.makedirs(RAP_theta)
    fig.savefig(RAP_theta+"Theta"+file_time+".png",
            bbox_inches='tight',dpi=120)
    
    
    plt.close(fig)
    print('next.')
print("All done.")

# In[ ]:




