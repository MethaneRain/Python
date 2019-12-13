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

# <h1><font style="font-size:32px"><center>-- Plotting all of the GFS forecast hours for the current day --</center></font></h1>

# In[ ]:





# In[ ]:





# In[ ]:





# In[8]:


def Map_Isen4(i,im_save_path):
    # Create a figure object, title it, and do the plots.
    fig = plt.figure(figsize = (25,18))
    fig.subplots_adjust(hspace=0.06)
    fig.subplots_adjust(wspace=0.08)

    extent = [-130., -70, 20., 60.]


    from siphon.catalog import TDSCatalog
    top_cat = TDSCatalog('http://thredds.ucar.edu/thredds/catalog.xml')
    ref = top_cat.catalog_refs['Forecast Model Data']
    new_cat = ref.follow()
    model = new_cat.catalog_refs[4]
    gfs_cat = model.follow()
    ds = gfs_cat.datasets[1]

    ref_anl = top_cat.catalog_refs['Forecast Products and Analyses']
    new_cat_anl = ref_anl.follow()
    model_anl = new_cat_anl.catalog_refs[1]
    gfs_anl_cat = model_anl.follow()
    ds_anl = gfs_anl_cat.datasets[1]



    subset = ds.subset()
    query_data = subset.query()
    query_data.lonlat_box(west=-130, east=-50, south=10, north=60)

        # Allow for NetCDF files
    query_data.accept('netcdf4')
    query_data.time(i)
    data = query_data.variables('Temperature_isobaric', 'Geopotential_height_isobaric',
                    'u-component_of_wind_isobaric', 'v-component_of_wind_isobaric',
                    'Relative_humidity_isobaric','Absolute_vorticity_isobaric')

        # Finally attempt to access the data
    data = subset.get_data(query_data)
    ##############################################################################################################
                                            # 6-Hour Precipitation Accumulation
    ##############################################################################################################
    subset_anl = ds_anl.subset()
    query_data_anl = subset_anl.query()
    query_data_anl.lonlat_box(west=-130, east=-50, south=10, north=60)

        # Allow for NetCDF files
    query_data_anl.accept('netcdf4')
    query_data_anl.time(i)
    data_anl = query_data_anl.variables("Total_precipitation_surface_6_Hour_Accumulation").add_lonlat()

        # Finally attempt to access the data
    data_anl = subset_anl.get_data(query_data_anl)
    dew = data_anl.variables['Total_precipitation_surface_6_Hour_Accumulation'][:].squeeze()
    dew = np.ma.masked_where(dew < 2.,dew)

    lat = data_anl.variables['lat'][:].squeeze()
    lon = data_anl.variables['lon'][:].squeeze()
            #lats = data.variables['lat'][:]
            #lons = data.variables['lon'][:]
    time_var_anl = data_anl.variables[find_time_var(data_anl.variables['Total_precipitation_surface_6_Hour_Accumulation'])]

        # Convert number of hours since the reference time into an actual date
    time_final_anl = num2date(time_var_anl[:].squeeze(), time_var_anl.units)
    print(str(time_final_anl)[:4]+"_"+str(time_final_anl)[5:7]+"_"+str(time_final_anl)[8:10]+"_"+str(time_final_anl)[11:13]+"Z")
    file_time_anl = str(time_final_anl)[:4]+"_"+str(time_final_anl)[5:7]+"_"+str(time_final_anl)[8:10]+"_"+str(time_final_anl)[11]

    # Add the map and set the extent
    ax1 = plt.subplot(2,2,4, projection=plotcrs)

    # Add state boundaries to plot
    ax1.add_feature(states_provinces, edgecolor='k', linewidth=1)

    # Add country borders to plot
    ax1.add_feature(country_borders, edgecolor='black', linewidth=1)

        #Set the lat and lon boundaries
    ax1.set_extent(extent, datacrs)

    # Plot Title
    plt.title('GFS: 6-Hr Precip Accumulation',loc='left',fontsize=16)
    #plt.title(' {0:%d %B %Y %H:%MZ}'.format(time_final_anl),loc='right',fontsize=16)

    #radar = np.ma.masked_where(radar < 0.,radar)
    #cmap = colortables.get_colortable('NWSReflectivity')
    cs = ax1.contourf(lon,lat,dew,40, cmap="jet",transform=datacrs)#norm=Normalize(-1, 80)
    #cs = plt.pcolor(lon,lat, radar, cmap=cmap, norm=Normalize(-25, 75))
    #cbar = plt.colorbar(cs, orientation='vertical',pad=0.005,aspect=50)
    ##############################################################################################################
                                            # Isentropic Heights and Winds
    ##############################################################################################################

    # Add the map and set the extent
    ax2 = plt.subplot(2,2,1, projection=plotcrs)

    # Add state boundaries to plot
    ax2.add_feature(states_provinces, edgecolor='k', linewidth=1)

    # Add country borders to plot
    ax2.add_feature(country_borders, edgecolor='black', linewidth=1)


    lat = data.variables['lat'][:]
    lon = data.variables['lon'][:]
    press = data.variables['isobaric'][:] * units.Pa
    temperature = data.variables['Temperature_isobaric'][0] * units.kelvin
    rh = data.variables['Relative_humidity_isobaric'][0] * units.percent
    height = data.variables['Geopotential_height_isobaric'][0] * units.meter
    u = data.variables['u-component_of_wind_isobaric'][0] * units('m/s')
    v = data.variables['v-component_of_wind_isobaric'][0] * units('m/s')
        #vort =  data.variables['Absolute_vorticity_isobaric'][0] * units('1/s')  
    TEMP = 295
    isen_level = np.array([TEMP]) * units.kelvin
    isen_press, isen_u, isen_v = mpcalc.isentropic_interpolation(isen_level, press,
                temperature, u, v)
    # Need to squeeze() out the size-1 dimension for the isentropic level
    isen_press = isen_press.squeeze()
    isen_u = isen_u.squeeze()
    isen_v = isen_v.squeeze()
        #isen_vort = isen_vort.squeeze()

    # Needed to make numpy broadcasting work between 1D pressure and other 3D arrays
    pressure_for_calc = press[:, None, None]

    # Calculate mixing ratio using something from mpcalc
    mixing = mpcalc.mixing_ratio_from_relative_humidity(rh, temperature, pressure_for_calc)

    # Take the return and convert manually to units of 'dimenionless'
    mixing.ito('dimensionless')

    # Interpolate all the data
    isen_level = np.array([295]) * units.kelvin
    ret = mpcalc.isentropic_interpolation(isen_level, press, temperature, mixing, u, v)
    isen_press, isen_mixing, isen_u, isen_v = ret

    # Squeeze the returned arrays
    isen_press = isen_press.squeeze()
    isen_mixing = isen_mixing.squeeze()
    isen_u = isen_u.squeeze()
    isen_v = isen_v.squeeze()

    # 
    # Convert number of hours since the reference time into an actual date
    time_var = data.variables[find_time_var(data.variables['Geopotential_height_isobaric'])]
    time_final = num2date(time_var[:].squeeze(), time_var.units)
    print(str(time_final)[:4]+"_"+str(time_final)[5:7]+"_"+str(time_final)[8:10]+"_"+str(time_final)[11:13]+"Z")
    file_time = str(time_final)[:4]+"_"+str(time_final)[5:7]+"_"+str(time_final)[8:10]+"_"+str(time_final)[11:13]+"Z"    

    # Plot Title
    plt.title('GFS: {}K Isentropic Pressure and Winds (m/s)'.format(TEMP),loc='left',fontsize=16)
    #plt.title(' {0:%d %B %Y %H:%MZ}'.format(time_final),loc='right',fontsize=16)

                                                # Isentropic Pressure
    #---------------------------------------------------------------------------------------------------
    # Contour the pressure values for the isentropic level. We keep the handle
    # for the contour so that we can have matplotlib label the contours

    levels = np.arange(300, 1000, 10)
    cntr = ax2.contour(lon, lat, isen_press, transform=datacrs,
                     cmap='rainbow',levels=levels,linewidths=2) #ccrs.PlateCarree()
    #ax.clabel(cntr, fmt='%.0f',colors='black')

    #cbaxes = fig.add_axes(colorbar_axis)
    #cbar = plt.colorbar(cntr, orientation='horizontal',cax=cbaxes)

                                                # Isentropic Winds
    #---------------------------------------------------------------------------------------------------
    # Set up slices to subset the wind barbs--the slices below are the same as `::5`
    # We put these here so that it's easy to change and keep all of the ones below matched
    # up.

    lon_slice = slice(None, None, 11)
    lat_slice = slice(None, None, 11)
    ax2.barbs(lon[lon_slice], lat[lat_slice],
             isen_u[lon_slice, lat_slice],
             isen_v[lon_slice, lat_slice],
             #isen_u[lon_slice, lat_slice].to('knots').magnitude,
             #isen_v[lon_slice, lat_slice].to('knots').magnitude,
             transform=ccrs.PlateCarree(), zorder=2) # barbcolor="" optional call

    ax2.set_extent(extent, datacrs)

        #plt.show()



    ##############################################################################################################
                                            # Isentropic Pressure, Winds and Mixing Ratio
    ##############################################################################################################
    # Add the map and set the extent
    ax3 = plt.subplot(2,2,2, projection=plotcrs)

    # Add state boundaries to plot
    ax3.add_feature(states_provinces, edgecolor='k', linewidth=1)

    # Add country borders to plot
    ax3.add_feature(country_borders, edgecolor='black', linewidth=1)




    # Plot Title
    plt.title('GFS: {}K Isentrope Pressure, Winds (m/s) and Mixing Ratio'.format(TEMP),loc='left',fontsize=16)
    #plt.title(' {0:%d %B %Y %H:%MZ}'.format(time_final),loc='right',fontsize=16)

                                                # Isentropic Pressure
    #---------------------------------------------------------------------------------------------------
    levels = np.arange(300, 1000, 20)
    cntr = ax3.contour(lon, lat, isen_press, transform=datacrs,
                      colors='k', levels=levels,linewidths=2.0,alpha=0.5)#colors='black'cmap='rainbow'
    ax3.clabel(cntr, fmt='%.0f')

                                                # Isentropic Winds
    #---------------------------------------------------------------------------------------------------

    lon_slice = slice(None, None, 14)
    lat_slice = slice(None, None, 14)
    ax3.barbs(lon[lon_slice], lat[lat_slice],
             isen_u[lon_slice, lat_slice],
             isen_v[lon_slice, lat_slice],
             #isen_u[lon_slice, lat_slice].to('knots').magnitude,
             #isen_v[lon_slice, lat_slice].to('knots').magnitude,
             transform=ccrs.PlateCarree(), zorder=10,barbcolor='r')


                                               # Isentropic Mixing Ratio
    #---------------------------------------------------------------------------------------------------
    # Contourf the mixing ratio values
    mixing_levels = [0.001, 0.002, 0.004, 0.006, 0.010, 0.012, 0.014, 0.016, 0.020]
    cntr2 = ax3.contourf(lon, lat, isen_mixing, transform=datacrs,
                levels=mixing_levels, cmap='YlGn')

    ax3.set_extent(extent, datacrs)

    #cbaxes = fig.add_axes(colorbar_axis) # [left, bottom, width, height]
    #cbar = plt.colorbar(cntr2, orientation='horizontal',cax=cbaxes)




    ########################################################################################################

    ##############################################################################################################
                                            # Isentropic Pressure, Winds and Omega
    ##############################################################################################################
    # Add the map and set the extent
    ax4 = plt.subplot(2,2,3, projection=plotcrs)

    #isen_press.units, isen_u.units, isen_v.units
    dx, dy = mpcalc.lat_lon_grid_spacing(lon, lat)
    dy = -dy

    # Filter and re-attach units
    isen_press = gaussian_filter(isen_press.squeeze(), sigma=2.0) * units.hPa
    isen_u = gaussian_filter(isen_u.squeeze(), sigma=2.0) * units('m/s')
    isen_v = gaussian_filter(isen_v.squeeze(), sigma=2.0) * units('m/s')

    #isen_press = isen_press.squeeze() * units.hPa
    #isen_u = isen_u.squeeze() * units('m/s')
    #isen_v = isen_v.squeeze() * units('m/s')
    lift = -mpcalc.advection(isen_press, [isen_u, isen_v], [dx, dy], dim_order='yx')

    add_metpy_logo(fig, 30, 940, size='small')


    # Add state boundaries to plot
    ax4.add_feature(states_provinces, edgecolor='k', linewidth=1)

    # Add country borders to plot
    ax4.add_feature(country_borders, edgecolor='black', linewidth=1)

    # Plot Title
    plt.title('GFS: {}K Isentropic Pressure and Omega'.format(TEMP),loc='left',fontsize=16)
    #plt.title(' {0:%d %B %Y %H:%MZ}'.format(time_final),loc='right',fontsize=16)

                                                # Isentropic Pressure
    #---------------------------------------------------------------------------------------------------
    levels = np.arange(300, 1000, 50)
    cntr = ax4.contour(lon, lat, isen_press, transform=ccrs.PlateCarree(), colors='black', levels=levels,linewidths=2.0)
    #cntr = ax4.contour(lon, lat, isen_press, transform=ccrs.PlateCarree(), cmap='rainbow', levels=levels,linewidths=2.0)
    ax4.clabel(cntr, fmt='%.0f')


                                                # Isentropic Winds
    #---------------------------------------------------------------------------------------------------

    lon_slice = slice(None, None, 7)
    lat_slice = slice(None, None, 7)
        #ax.barbs(lon[lon_slice], lat[lat_slice],
        #     isen_u[lon_slice, lat_slice],
        #     isen_v[lon_slice, lat_slice],
        #     #isen_u[lon_slice, lat_slice].to('knots').magnitude,
        #     #isen_v[lon_slice, lat_slice].to('knots').magnitude,
         #    transform=ccrs.PlateCarree(), zorder=4)


                                                # Omega
    #---------------------------------------------------------------------------------------------------

    levels = np.arange(-10, 10,2)
    cs = ax4.contourf(lon, lat, lift.to('microbar/s'), levels=levels, cmap='RdBu',
                     transform=ccrs.PlateCarree())#, extend='both') .to('microbar/s')
    #cbaxes = fig.add_axes(colorbar_axis) 
    #cbar = plt.colorbar(cs, orientation='horizontal',cax=cbaxes)

    ax4.set_extent(extent, datacrs)



    fig.suptitle(' {0:%d %B %Y %H:%MZ}'.format(time_final),fontsize=35,x=0.8,y=0.94)
    add_metpy_logo(fig, 50, 1970, size='large')

    plt.close(fig)

    PV_Jet = im_save_path+"GFS/Isen/"
    if not os.path.isdir(PV_Jet):
        os.makedirs(PV_Jet)
    fig.savefig(PV_Jet+"4_Panel_Isentropic"+file_time+".png",
                    bbox_inches='tight',dpi=120)
    print("done")


# In[ ]:




