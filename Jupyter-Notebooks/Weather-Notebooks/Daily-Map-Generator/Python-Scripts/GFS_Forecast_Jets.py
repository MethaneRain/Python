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

# <h1><font><center>-- 250mb Heights and Jet Streaks --</center></font></h1>

# In[15]:


def Map_Jets(i,im_save_path):
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
    data = query_data.variables('Geopotential_height_isobaric',
               'Pressure_reduced_to_MSL_msl',
               'u-component_of_wind_isobaric',
               'v-component_of_wind_isobaric')

# Finally attempt to access the data
    data = subset.get_data(query_data)
    lat = data.variables['lat'][:].squeeze()
    lon = data.variables['lon'][:].squeeze()
    lev_250 = np.where(data.variables['isobaric4'][:] == 25000)[0][0]

    hght_250 = data.variables['Geopotential_height_isobaric'][0, lev_250, :, :]
    u_250 = data.variables['u-component_of_wind_isobaric'][0, lev_250, :, :]
    v_250 = data.variables['v-component_of_wind_isobaric'][0, lev_250, :, :]
    
# Create a figure object, title it, and do the plots.
    fig = plt.figure(figsize = (17.,11.))

    add_metpy_logo(fig, 30, 940, size='small')

# Add the map and set the extent
    ax6 = plt.subplot(1,1,1, projection=plotcrs)

# Add state boundaries to plot
    ax6.add_feature(states_provinces, edgecolor='b', linewidth=1)

# Add country borders to plot
    ax6.add_feature(country_borders, edgecolor='k', linewidth=1)

# Convert number of hours since the reference time into an actual date
    time_var = data.variables[find_time_var(data.variables['v-component_of_wind_isobaric'])]
    time_final = num2date(time_var[:].squeeze(), time_var.units)
    print(str(time_final)[:4]+"_"+str(time_final)[5:7]+"_"+str(time_final)[8:10]+"_"+str(time_final)[11:13]+"Z")
    file_time = str(time_final)[:4]+"_"+str(time_final)[5:7]+"_"+str(time_final)[8:10]+"_"+str(time_final)[11:13]+"Z" 
    
# Plot Title
    plt.title('GFS: 250mb Heights and Jet Streaks (m/s)',loc='left',fontsize=16)
    plt.title(' {0:%d %B %Y %H:%MZ}'.format(time_final),loc='right',fontsize=16)


                                        # Heights
#---------------------------------------------------------------------------------------------------

    MIN = hght_250.min()
    MAX = hght_250.max()

    #print hght_250.min(),hght_250.max()
    hght_250 = ndimage.gaussian_filter(hght_250, sigma=3, order=0) * units.meter

    clev250 = np.arange(MIN, MAX, 80)
    cs = ax6.contour(lon, lat, hght_250.m, clev250, colors='black', linewidths=2.0,
                linestyles='solid', transform=ccrs.PlateCarree())
#plt.clabel(cs, fontsize=10, inline=1, inline_spacing=10, fmt='%i',
#           rightside_up=True, use_clabeltext=True)

                                        # Winds
#---------------------------------------------------------------------------------------------------
#lon_slice = slice(None, None, 7)
#lat_slice = slice(None, None, 7)
#ax4.barbs(lon[lon_slice], lat[lat_slice],
#         u_250[lon_slice, lat_slice].magnitude,
#         v_250[lon_slice, lat_slice].magnitude,
#         transform=ccrs.PlateCarree(), zorder=2)

    wspd250 = mpcalc.get_wind_speed(u_250, v_250)
    clevsped250 = np.arange(50, 100, 1)
    cf = ax6.contourf(lon, lat, wspd250, clevsped250, cmap="gist_ncar", transform=ccrs.PlateCarree())
    #cbar = plt.colorbar(cf, cax=cax, orientation='horizontal', extend='max', extendrect=True,pad=0.2)
    cbaxes = fig.add_axes(colorbar_axis) 

    cbar = plt.colorbar(cf, orientation='horizontal',cax=cbaxes)

    ax6.set_extent(extent, datacrs)

    plt.close(fig)
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
    GFS_Jet = im_save_path+"GFS/Jets/"
    if not os.path.isdir(GFS_Jet):
        os.makedirs(GFS_Jet)
    fig.savefig(GFS_Jet+"250mb_Heights_Winds_"+file_time+".png",
            bbox_inches='tight',dpi=120)

    print('done.')

