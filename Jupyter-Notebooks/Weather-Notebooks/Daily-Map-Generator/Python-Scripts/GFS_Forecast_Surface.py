#!/usr/bin/env python
# coding: utf-8

# # Collection of GFS Forecast Maps from Thredds Server via NCSS and Siphon

# ## Justin Richling
# ## 11/15/18

# https://doi.org/10.6084/m9.figshare.5244637.v1

# In[1]:


# Random Library Imports
import subprocess,os,glob,tempfile,re,webbrowser,io,sys,types,time

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

# <h1><font><center>-- MSLP, Surface Winds and Temps --</center></font></h1>

# In[8]:


def Map_Sfc(i,im_save_path):
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
    data = query_data.variables("Pressure_reduced_to_MSL_msl",
               'Apparent_temperature_height_above_ground',
                'u-component_of_wind_height_above_ground',
               'v-component_of_wind_height_above_ground')

# Finally attempt to access the data
    data = subset.get_data(query_data)
    #for i in data.variables.keys(): print "Variables:",i,"\n"
    
    # Pull out variables you want to use
    mslp = data.variables['Pressure_reduced_to_MSL_msl'][:].squeeze()
    temp = units.K * data.variables['Apparent_temperature_height_above_ground'][:].squeeze()
    u_wind = units('m/s') * data.variables['u-component_of_wind_height_above_ground'][:].squeeze()
    v_wind = units('m/s') * data.variables['v-component_of_wind_height_above_ground'][:].squeeze()
    lat = data.variables['lat'][:].squeeze()
    lon = data.variables['lon'][:].squeeze()
    lats = data.variables['lat'][:]
    lons = data.variables['lon'][:]
    time_var = data.variables[find_time_var(data.variables['Pressure_reduced_to_MSL_msl'])]

# Convert winds to knots
    u_wind.ito('kt')
    v_wind.ito('kt')

# Convert number of hours since the reference time into an actual date
    time_final = num2date(time_var[:].squeeze(), time_var.units)
    print(str(time_final)[:4]+"_"+str(time_final)[5:7]+"_"+str(time_final)[8:10]+"_"+str(time_final)[11:13]+"Z")
    file_time = str(time_final)[:4]+"_"+str(time_final)[5:7]+"_"+str(time_final)[8:10]+"_"+str(time_final)[11:13]+"Z"

    lev_10m = np.where(data.variables['height_above_ground3'][:] == 10)[0][0]
    u_wind_10m = u_wind[lev_10m]
    v_wind_10m = v_wind[lev_10m]

# Combine 1D latitude and longitudes into a 2D grid of locations
    lon_2d, lat_2d = np.meshgrid(lon, lat)
    
# Smooth MSLP a little
# Be sure to only put in a 2D lat/lon or Y/X array for smoothing
    smooth_mslp = ndimage.gaussian_filter(mslp, sigma=3, order=0) * units.Pa
    smooth_mslp.ito('hPa')

    
    
    # Create new figure
    fig = plt.figure(figsize=(17., 11.))

    add_metpy_logo(fig, 30, 940, size='small')

# Add the map and set the extent
    ax = plt.subplot(111, projection=plotcrs)

#Set the lat and lon boundaries
    ax.set_extent(extent, datacrs)

# Add state boundaries to plot
    ax.add_feature(states_provinces, edgecolor='blue', linewidth=1)

# Add country borders to plot
    ax.add_feature(country_borders, edgecolor='black', linewidth=1)

# Plot Title
    plt.title('GFS: MSLP (hPa), 2m Temperature (F), Wind Barbs (kt)', fontsize=16,loc='left')
    plt.title(' {0:%d %B %Y %H:%MZ}'.format(time_final), fontsize=16,loc='right')

                                            # MSLP
#---------------------------------------------------------------------------------------------------
#clev_mslp = np.arange(0, 1200, 3)

#cs = ax.contour(lon_2d, lat_2d, smooth_mslp, clev_mslp, colors='k', linewidths=3,
#    linestyles='solid', transform=datacrs) # cmap='rainbow

#plt.clabel(cs, fontsize=10, inline=1, inline_spacing=10, fmt='%i',
#           rightside_up=True, use_clabeltext=True,colors='k')

# Plot Absolute Vorticity
#clev_abVort = np.arange(Max,Min,0.00001)
#abVort = ax.contourf(lon_2d, lat_2d, abs_vort[5,:,:],transform=datacrs,cmap='BrBG')
#cbaxes = fig.add_axes([0.92, 0.233, 0.03, 0.54]) # [left, bottom, width, height]
#cbar = plt.colorbar(abVort, orientation='vertical',cax=cbaxes)
#plt.colorbar(cs2, orientation='vertical', fraction=0.0311, pad=0.02)


                                            # 2m Temperatures
#---------------------------------------------------------------------------------------------------
# Plot 2m Temperature Contours
    clevtemp = np.arange(-30, 90, 2)

# Uncomment for contours instead of contour fill (below)
#cs2 = ax.contour(lon_2d, lat_2d, temp.to(units('degF')), clevtemp,
#                 cmap='gist_rainbow_r', linewidths=1.25,
#                 transform=datacrs)  #linestyles='dotted'

    cs2 = ax.contourf(lon_2d, lat_2d, temp.to(units('degF')),40,
                 transform=datacrs,cmap='gist_rainbow_r')

    cbaxes = fig.add_axes(colorbar_axis) # [left, bottom, width, height]

    cbar = plt.colorbar(cs2, orientation='horizontal',cax=cbaxes)

#plt.clabel(cs2, fontsize=10, inline=1, inline_spacing=10, fmt='%i',
#           rightside_up=True, use_clabeltext=True)

                                            # 10m Winds
#---------------------------------------------------------------------------------------------------
    ax.barbs(lon_2d, lat_2d, u_wind_10m.magnitude, v_wind_10m.magnitude,
         length=6, regrid_shape=20, pivot='middle', transform=datacrs,barbcolor='k')

    #plt.show()
    plt.close(fig)
    Surf = im_save_path+"GFS/MSLP_Temps/"
    if not os.path.isdir(Surf):
        os.makedirs(Surf)
    outfile=Surf+"MSLP_Temps_Winds_"+file_time+".png"
    fig.savefig(outfile,bbox_inches='tight',dpi=120)
    
    print("done.")


# <h2>----------------------------------------------//---------------------------------------------------------</h2>
