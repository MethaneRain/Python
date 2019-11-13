#!/usr/bin/env python
# coding: utf-8

# # Collection of GFS Forecast Maps from Thredds Server via NCSS and Siphon

# ## Justin Richling
# ## 11/15/18

# https://doi.org/10.6084/m9.figshare.5244637.v1

# In[1]:


# Random Library Imports
import subprocess,os,glob,re,webbrowser,io,sys,time

# Importing Datetime Libraries
from datetime import datetime, timedelta

# CartoPy Map Plotting Libraires
import cartopy.crs as ccrs
import cartopy.feature as cfeature
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
from metpy.plots import add_metpy_logo
from metpy.constants import g

# NetCDF Libraries
from netCDF4 import Dataset
from netCDF4 import num2date

# More Image Manipulation Options
from PIL import Image as PILImage
from IPython.display import Image

# Ipyhton Options
from IPython import get_ipython
from nbformat import current
from IPython.core.interactiveshell import InteractiveShell
from IPython.display import HTML, display, Image

# Matplotlib Plotting Libraries
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
import matplotlib.colors as mcolors
from matplotlib.colors import LogNorm, Normalize
import matplotlib as mpl
from mpl_toolkits.axes_grid1 import make_axes_locatable, axes_size
from matplotlib.colors import LinearSegmentedColormap

# Warnings
import warnings
warnings.filterwarnings('ignore')

#import ColorBar


# ## Helper Functions

# In[2]:


# Thanks to the crew over at Metpy for this handy little function
def find_time_var(var, time_basename='time'):
    for coord_name in var.coordinates.split():
        if coord_name.startswith(time_basename):
            return coord_name
    raise ValueError('No time variable found for ' + var.name)


# <h2>----------------------------------------------//---------------------------------------------------------</h2>

# ## Set the Map Projection

# In[3]:


# Set Projection of Data
datacrs = ccrs.PlateCarree()

# Set Projection of Plot
plotcrs = ccrs.LambertConformal(central_latitude=[30, 60], central_longitude=-100)

# Add Map Features
states_provinces = cfeature.NaturalEarthFeature(category='cultural',
    name='admin_1_states_provinces_lakes',scale='50m', facecolor='none')

country_borders = cfeature.NaturalEarthFeature(category='cultural',
    name='admin_0_countries',scale='50m', facecolor='none')

# Colorbar Axis Placement (under figure)
colorbar_axis = [0.183, 0.09, 0.659, 0.03] # [left, bottom, width, height]

# Lat/Lon Extents [lon0,lon1,lat0,lat1]
extent = [-130., -70, 20., 60.]


# <h2>----------------------------------------------//---------------------------------------------------------</h2>

# <h1><center>-- CAPE --</center></h1>

# In[ ]:
















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
        #ax.text(lon[mxy[i], mxx[i]], lat[mxy[i], mxx[i]], symbol, color=color, size=24,
        #        clip_on=True, horizontalalignment='center', verticalalignment='center',
        #        transform=transform)
        #ax.text(lon[mxy[i], mxx[i]], lat[mxy[i], mxx[i]],
        #        '\n' + str(np.int(data[mxy[i], mxx[i]])),
        #        color=color, size=12, clip_on=True, fontweight='bold',
        #        horizontalalignment='center', verticalalignment='top', transform=transform)
        
        AX.text(lon[mxx[i]], lat[mxy[i]], symbol, color=color, size=24,
                clip_on=True, horizontalalignment='center', verticalalignment='center',
                transform=transform)
        AX.text(lon[mxx[i]], lat[mxy[i]],
                '\n' + str(np.int(data[mxy[i], mxx[i]])),
                color=color, size=12, clip_on=True, fontweight='bold',
                horizontalalignment='center', verticalalignment='top', transform=transform)


# In[13]:


def Map_Cape(i,im_save_path):
    from siphon.catalog import TDSCatalog
    top_cat = TDSCatalog('http://thredds.ucar.edu/thredds/catalog.xml')
    ref = top_cat.catalog_refs['Forecast Model Data']
    new_cat = ref.follow()
    model = new_cat.catalog_refs[4]
    gfs_cat = model.follow()
    ds = gfs_cat.datasets[1]
    subset = ds.subset()
    query_data = subset.query()
    query_data.lonlat_box(west=-130, east=-50, south=10, north=60)

# Allow for NetCDF files
    query_data.accept('netcdf4')
    query_data.time(i)
    data = query_data.variables("Convective_available_potential_energy_surface",
                               "Pressure_reduced_to_MSL_msl","u-component_of_wind_height_above_ground",
                               "v-component_of_wind_height_above_ground")

# Finally attempt to access the data
    data = subset.get_data(query_data)
    
    cape = data.variables['Convective_available_potential_energy_surface'][:].squeeze()
    mslp = data.variables['Pressure_reduced_to_MSL_msl'][:] * units.Pa
    mslp.ito('hPa')
    mslp = gaussian_filter(mslp[0], sigma=3.0)
    u_wind = units('m/s') * data.variables['u-component_of_wind_height_above_ground'][:].squeeze()
    v_wind = units('m/s') * data.variables['v-component_of_wind_height_above_ground'][:].squeeze()
    u_wind.ito('kt')
    v_wind.ito('kt')
    lev_10m = np.where(data.variables['height_above_ground3'][:] == 10)[0][0]
    u_wind_10m = u_wind[lev_10m]
    v_wind_10m = v_wind[lev_10m]
    
    cape = np.ma.masked_where(cape < 50,cape)
    lat = data.variables['lat'][:]
    lon = data.variables['lon'][:]
# Create a figure object, title it, and do the plots.
    fig = plt.figure(figsize = (17.,11.))

    add_metpy_logo(fig, 30, 940, size='small')

# Add the map and set the extent
    ax = plt.subplot(1,1,1, projection=plotcrs)

# Add state boundaries to plot
    ax.add_feature(states_provinces, edgecolor='b', linewidth=1)

# Add country borders to plot
    ax.add_feature(country_borders, edgecolor='k', linewidth=1)

# Convert number of hours since the reference time into an actual date
    time_var = data.variables[find_time_var(data.variables['Convective_available_potential_energy_surface'])]
    time_final = num2date(time_var[:].squeeze(), time_var.units)
    print(str(time_final)[:4]+"_"+str(time_final)[5:7]+"_"+str(time_final)[8:10]+"_"+str(time_final)[11:13]+"Z")
    file_time = str(time_final)[:4]+"_"+str(time_final)[5:7]+"_"+str(time_final)[8:10]+"_"+str(time_final)[11:13]+"Z" 
    
# Plot Title
    plt.title('GFS: CAPE (J/Kg)',loc='left',fontsize=16)
    plt.title(' {0:%d %B %Y %H:%MZ}'.format(time_final),loc='right',fontsize=16)


                                        # Dew Points
#---------------------------------------------------------------------------------------------------
    levs = np.arange(50,5000,100)
    cs = ax.contourf(lon,lat,cape,levs,cmap="nipy_spectral",transform=datacrs)
#plt.clabel(cs, fontsize=10, inline=1, inline_spacing=10, fmt='%i',
#           rightside_up=True, use_clabeltext=True)

    cbaxes = fig.add_axes(colorbar_axis) # [left, bottom, width, height]

    cbar = plt.colorbar(cs, orientation='horizontal',cax=cbaxes)
    ax.set_extent(extent, datacrs)
    #ax.set_extent([-105, -98, 30, 50])
    
    
    kw_clabels = {'fontsize': 11, 'inline': True, 'inline_spacing': 5, 'fmt': '%i',
              'rightside_up': True, 'use_clabeltext': True}
    clevmslp = np.arange(800., 1120., 4)
    cs2 = ax.contour(lon, lat, mslp, clevmslp, colors='k', linewidths=1.25,
                 linestyles='solid', transform=datacrs)
    plt.clabel(cs2, **kw_clabels)

                                            # High and Low Symbols
#---------------------------------------------------------------------------------------------------
    plot_maxmin_points(ax,lon, lat, mslp, 'max', 50, symbol='H', color='b',  transform=datacrs)
    plot_maxmin_points(ax,lon, lat, mslp, 'min', 25, symbol='L', color='r', transform=datacrs)
    
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
    ax.barbs(lon, lat, u_wind_10m.magnitude, v_wind_10m.magnitude,
         length=6, regrid_shape=20, pivot='middle', transform=datacrs,barbcolor='k')
    
    
    GFS_CAPE = im_save_path+"GFS/CAPE/"
    if not os.path.isdir(GFS_CAPE):
        os.makedirs(GFS_CAPE)
    fig.savefig(GFS_CAPE+"CAPE_"+file_time+".png",
            bbox_inches='tight',dpi=120)
    plt.close(fig)
    
    print('done.')


# In[ ]:




