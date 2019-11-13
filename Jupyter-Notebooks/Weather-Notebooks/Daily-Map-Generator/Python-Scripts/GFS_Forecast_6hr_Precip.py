#!/usr/bin/env python
# coding: utf-8

# # NDFD Forecast Maps from Thredds Server via NCSS and Siphon
# # 6-Hour Precip Accumulation
# ### National Digital Forecast Database

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


# In[ ]:


# Set the font 
font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 18,
        }


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

# <h1><font><center>-- 6-Hour Precipitation Accumulation --</center></font></h1>
# 
# * Starting at??

# In[7]:


def Map_6hrPrecip(i,im_save_path):
    

    
    
    
    from siphon.catalog import TDSCatalog
    top_cat = TDSCatalog('http://thredds.ucar.edu/thredds/catalog.xml')
    ref_anl = top_cat.catalog_refs['Forecast Products and Analyses']
    new_cat_anl = ref_anl.follow()
    model_anl = new_cat_anl.catalog_refs[1]
    gfs_anl_cat = model_anl.follow()
    ds_anl = gfs_anl_cat.datasets[1]
    
    subset = ds_anl.subset()
    query_data = subset.query()
    query_data.lonlat_box(west=-130, east=-50, south=10, north=60)

        # Allow for NetCDF files
    query_data.accept('netcdf4')
    query_data.time(i)
    data = query_data.variables("Total_precipitation_surface_6_Hour_Accumulation").add_lonlat()

        # Finally attempt to access the data
    data = subset.get_data(query_data)
    dew = data.variables['Total_precipitation_surface_6_Hour_Accumulation'][:].squeeze()
    dew = np.ma.masked_where(dew < 2.,dew)

    lat = data.variables['lat'][:].squeeze()
    lon = data.variables['lon'][:].squeeze()
            #lats = data.variables['lat'][:]
            #lons = data.variables['lon'][:]
    time_var = data.variables[find_time_var(data.variables['Total_precipitation_surface_6_Hour_Accumulation'])]

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

        # Add state boundaries to plot
    ax.add_feature(states_provinces, edgecolor='blue', linewidth=1)

        # Add country borders to plot
    ax.add_feature(country_borders, edgecolor='black', linewidth=1)

    # Plot Title
    plt.title('6-hr Precip Accumulation ($kg/m^{2}$)',loc='left',fontdict=font)
    plt.title(' {0:%d %B %Y %H:%MZ}'.format(time_final),loc='right',fontdict=font)

    cs = ax.contourf(lon,lat,dew,40, cmap="jet",transform=datacrs)#norm=Normalize(-1, 80)
    cbaxes = fig.add_axes(colorbar_axis) # [left, bottom, width, height]
    cbar = plt.colorbar(cs, orientation='horizontal',cax=cbaxes)
    #cbar.set_label(r'$s^-1$')

    #plt.show()
    plt.close(fig)
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    PV_Jet = im_save_path+"GFS/Precip_6/"
    if not os.path.isdir(PV_Jet):
        os.makedirs(PV_Jet)
    fig.savefig(PV_Jet+"Precip_Accum"+file_time+".png",
                bbox_inches='tight',dpi=120)
    
    print('done.')


# In[ ]:




