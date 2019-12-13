#!/usr/bin/env python
# coding: utf-8

# In[1]:


from datetime import datetime
import os


from netCDF4 import num2date
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
import matplotlib.colors as mcolors
from matplotlib.colors import LogNorm, Normalize
import matplotlib as mpl
from mpl_toolkits.axes_grid1 import make_axes_locatable, axes_size
from matplotlib.colors import LinearSegmentedColormap



from metpy.plots import add_metpy_logo


# CartoPy Map Plotting Libraires
import cartopy.crs as ccrs
import cartopy.feature as cfeature


# Numerical and Scientific Libraries


# Accessing Data from External Databases via XLM Catalog
from siphon.catalog import TDSCatalog
from mpl_toolkits.axes_grid1.inset_locator import inset_axes


# In[2]:


# Thanks to the crew over at Metpy for this handy little function
def find_time_var(var, time_basename='time'):
    for coord_name in var.coordinates.split():
        if coord_name.startswith(time_basename):
            return coord_name
    raise ValueError('No time variable found for ' + var.name)







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




# In[3]:


def Map_UpFlux_PV(i,im_save_path,MSLP=False):
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
    data = query_data.variables('Temperature_surface', 'Relative_humidity_entire_atmosphere_single_layer',
                'Wind_speed_gust_surface',"Pressure_potential_vorticity_surface",
               "MSLP_Eta_model_reduction_msl","Geopotential_height_isobaric",
               "Upward_Long-Wave_Radp_Flux_atmosphere_top_Mixed_intervals_Average")

# Finally attempt to access the data
    # Request data for the variables you want to use
    data = subset.get_data(query_data)
    #print(list(data.variables))

    # Pull out the lat and lon data
    lat = data.variables['lat'][:]
    lon = data.variables['lon'][:]

    # Get time into a datetime object
    time_var = data.variables[find_time_var(data.variables['Temperature_surface'])]
    time_var = num2date(time_var[:], time_var.units).tolist()
    #time_strings = [t.strftime('%m/%d %H:%M') for t in time_var]

    # Combine 1D latitude and longitudes into a 2D grid of locations
    lon_2d, lat_2d = np.meshgrid(lon, lat)

    mslp = data.variables["MSLP_Eta_model_reduction_msl"][:].squeeze()
    mslp = mslp.astype(int)
    mslp = (mslp/100).astype(int)
    print(type(mslp[0,0,]))
    
    UpFlux = data.variables["Upward_Long-Wave_Radp_Flux_atmosphere_top_Mixed_intervals_Average"][:].squeeze()
    #PV = data.variables["Pressure_potential_vorticity_surface"][:,1,:,:].squeeze()
    PV_Heights = data.variables["Pressure_potential_vorticity_surface"][:].squeeze()

    PV_1 = np.where(data.variables['potential_vorticity_surface'][:] == 1.9999999949504854E-6)[0][0]
    PV = PV_Heights[PV_1]
    
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
    time_var = data.variables[find_time_var(data.variables['Temperature_surface'])]
    time_final = num2date(time_var[:].squeeze(), time_var.units)
    print(str(time_final)[:4]+"_"+str(time_final)[5:7]+"_"+str(time_final)[8:10]+"_"+str(time_final)[11:13]+"Z")
    file_time = str(time_final)[:4]+"_"+str(time_final)[5:7]+"_"+str(time_final)[8:10]+"_"+str(time_final)[11:13]+"Z" 
    
# Plot Title
    plt.title('GFS: PV and Upward Radiative Flux',loc='left',fontsize=16)
    plt.title(' {0:%d %B %Y %H:%MZ}'.format(time_final),loc='right',fontsize=16)


                                        # Dew Points
#---------------------------------------------------------------------------------------------------
    c = ax.contourf(lon_2d, lat_2d, UpFlux, np.arange(90,360,5),
                   cmap="Greys",transform=datacrs)
    c3 = ax.contour(lon_2d, lat_2d, PV ,np.arange(10000,60000,5000),
                     cmap="jet",transform=datacrs,alpha=0.5)

    axins = inset_axes(ax,width="5%",  # width = 5% of parent_bbox width
                       height="100%",    
                       loc='lower right',
                       bbox_to_anchor=(.205, -0.015, 0.9, 1),
                      bbox_transform=ax.transAxes)
    cb = fig.colorbar(c, cax=axins, shrink=0.7)
    
    axins = inset_axes(ax,width="5%",  # width = 5% of parent_bbox width
                       height="100%",    
                       loc='lower left',
                       bbox_to_anchor=(-.105, -0.015, 0.9, 1),
                      bbox_transform=ax.transAxes)
    cb2 = fig.colorbar(c3, cax=axins, shrink=0.7)
    cb2.ax.yaxis.set_ticks_position('left')
    cb2.set_label("1.5 PVU Height")
    cb.set_label("Upward Longwave Flux")
    cb2.ax.yaxis.set_label_position('left')
    
        
    if MSLP != False:
        print("should be plotting MSLP...")
        c2 = ax.contour(lon_2d, lat_2d, mslp, np.arange(980,1030,4),
                        linestyles = 'dashed',colors="r",transform=datacrs)
        
        
        plt.clabel(c2, fmt = '%.0f', inline = True,colors='k')
   
    ax.set_extent(extent, datacrs)
    GFS_CAPE = im_save_path+"GFS/PV_UpFlux/"
    if not os.path.isdir(GFS_CAPE):
        os.makedirs(GFS_CAPE)
    fig.savefig(GFS_CAPE+"PV_UpFlux_"+file_time+".png",
            bbox_inches='tight',dpi=120)
    plt.close(fig)
    
    print('done.')


# In[ ]:




