#!/usr/bin/env python
# coding: utf-8

# Author: Justin Richling
# Date: 2020 May 16


print("This Notebook only plots: Base Reflectivity and Radial Velocity"+"\n"+
     "Many other products are available in the data!")

from datetime import datetime, timedelta
import time

import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.io.shapereader as shpreader

import matplotlib.pyplot as plt
from matplotlib import patheffects
from matplotlib.colors import LinearSegmentedColormap

import numpy as np

import metpy
from metpy.plots import ctables

import pandas as pd

from siphon.catalog import TDSCatalog
from siphon.cdmr import Dataset
from siphon.radarserver import get_radarserver_datasets, RadarServer

rad_vel = pd.read_csv("/Users/chowdahead/Documents/radial_velocity_cmap.csv")
rad_vel_colors = []
for i in range(0,256):
    rad_vel_colors.append((float(rad_vel["r"][i]),
                               float(rad_vel["g"][i]),
                               float(rad_vel["b"][i]),
                               float(rad_vel["a"][i])
                             ))
cmap_name="rad_vel"
rad_vel_cmap = LinearSegmentedColormap.from_list(
            cmap_name, rad_vel_colors)

refl = pd.read_csv("/Users/chowdahead/Documents/refl_cmap.csv")
refl_colors = []
for i in range(0,255):
    refl_colors.append((float(refl["r"][i]),
                               float(refl["g"][i]),
                               float(refl["b"][i]),
                               float(refl["a"][i])
                             ))
cmap_name="refl"
refl_cmap = LinearSegmentedColormap.from_list(
            cmap_name, refl_colors)

prod_dict = {"N0V":{"prod_name":"Velocity","dataset_name":"RadialVelocity_HI"},
             "N1P":{"prod_name":"Precip1hr","dataset_name":"Precip1hr"},
             "N0Q":{"prod_name":"Reflectivity","dataset_name":"BaseReflectivityDR"},
             "N0S":{"prod_name":"StormMeanVelocity","dataset_name":"StormMeanVelocity"},
             "N0C":{"prod_name":"CC","dataset_name":"CorrelationCoefficient"},
             "N0H":{"prod_name":"HydroClass","dataset_name":"HydrometeorClassification"},
    
}

available_product_list = ['DAA',
 'DHR',
 'DOD',
 'DPA',
 'DPR',
 'DSD',
 'DSP',
 'DTA',
 'DU3',
 'DU6',
 'DVL',
 'EET',
 'HHC',
 'N0C',
 'N0H',
 'N0K',
 'N0M',
 'N0Q',
 'N0R',
 'N0S',
 'N0U',
 'N0V',
 'N0X',
 'N0Z',
 'N1C',
 'N1H',
 'N1K',
 'N1M',
 'N1P',
 'N1Q',
 'N1S',
 'N1U',
 'N1X',
 'N2C',
 'N2H',
 'N2K',
 'N2M',
 'N2Q',
 'N2S',
 'N2U',
 'N2X',
 'N3C',
 'N3H',
 'N3K',
 'N3M',
 'N3Q',
 'N3S',
 'N3U',
 'N3X',
 'NAC',
 'NAH',
 'NAK',
 'NAM',
 'NAQ',
 'NAU',
 'NAX',
 'NBC',
 'NBH',
 'NBK',
 'NBM',
 'NBQ',
 'NBU',
 'NBX',
 'NCR',
 'NET',
 'NMD',
 'NST',
 'NTP',
 'NVL',
 'NVW',
 'OHA',
 'PTA']

def query_radar_data(station,product,start,
                     minute_delta=0,hour_delta=0,day_delta=0):
    
    """
    ---------------------
    Query the radar data
    ---------------------
    ** Must run this function first to query and grab data **
    
    Arguments
    ----------
    data_set: name of the the THREDDS Radar Dataset, ie NEXRAD Level III Radar from IDD
    station: coded station name, ie FTG for Denver
    start: dataset start time
    
    Time deltas for range of times for query (default none)
    minute_delta: 
    hour_delta:
    day_delta:
    
    Returns
    -------
    file_list:
    dataset: shortened name of chosen THREDDS dataset 
    LatLonBox: lat/lon extent around radar station
    
    """
    
    end = start+timedelta(days=day_delta, minutes=minute_delta, hours=hour_delta)
    
    print(f"query start time:{start}")
    print(f"query end time:{end}")
    rs = RadarServer('http://thredds-aws.unidata.ucar.edu/thredds/radarServer/nexrad/level2/S3/')
    query = rs.query()
    rs.validate_query(query)
    print(rs.stations[station])

    query.stations(station).time_range(start,end).variables(product)
    catalog = rs.get_catalog(query)
    file_station = str(catalog.datasets[0])
    file_station = file_station[0:4]
   
    file_list = list(catalog.datasets.values())
    for t in file_list: print(t)
    LatLonBox = [rs.stations[station].longitude-3,rs.stations[station].longitude+3,
                 rs.stations[station].latitude-2,rs.stations[station].latitude+2]
  
    return file_list,LatLonBox

def get_radar_data(file_list,index=0):
    
    """
    ---------------
    Grab radar data
    ---------------
    Produce the data and time strings for each index of the file_list
    
    Arguments
    ---------
    file_list: list of queried files (.nids)
    index: index value of file_list
    
    Returns
    -------
    data: full data object with data and metadata
    title_time: time of particular file formatted for the plot title
    file_time: time of particular file formatted for the saved filename
    
    """
    ds = file_list[index]
    data = Dataset(ds.access_urls['CdmRemote'])

    radar_time = ((data.time_coverage_start).replace('T',' ')).replace('Z','')
    date_time_obj = datetime.strptime(radar_time, '%Y-%m-%d %H:%M:%S')

    print('Date:', date_time_obj.date())
    print('Time:', date_time_obj.time())
    print('Date-time:', date_time_obj)
    title_time = "{0:%d %b %Y %H%MZ}".format(date_time_obj)
    file_time = "{0:%Y_%m_%d_%H%MZ}".format(date_time_obj)
    print(title_time,file_time)
    #print(data)
    return data, title_time, file_time

def get_prod_name(product):
    
    """
    -----------------
    Grab product name
    -----------------
    Gives name of product used for filename extension as well as 
    product name in THREDDS database for query call
    
    Arguments
    ---------
    product: abbreviated prodcut name ie N0V,N1P,etc
    
    Returns
    -------
    prod_name: product name for filename
    thredds_product: product name for THREDDS query
    """
    prod_name = prod_dict[product]["prod_name"]
    thredds_product = prod_dict[product]["dataset_name"]

    return prod_name,thredds_product

def get_radar_vars(data,prod_name):  
    """
    --------------------
    Grab radar variables
    --------------------
    
    Arguments
    ---------
    data: full data 
    dataset_name: THREDDS dataset product name
    
    Returns
    -------
    
    radar_data: radar values
    x,y: spatial coordiantes for plotting in imshow/pcolormesh since no 
        lat/lon data is available 
    """
    sweep = 0
    if prod_name == "Velocity":
        ref_var = data.variables['RadialVelocity_HI']
        rng = data.variables['distanceV_HI'][:]
        az = data.variables['azimuthV_HI'][sweep]
        
    if prod_name == "Reflectivity":
        ref_var = data.variables['Reflectivity_HI']
        rng = data.variables['distanceR_HI'][:]
        az = data.variables['azimuthR_HI'][sweep]
    
    ref_data = ref_var[sweep]
    az_rad = np.deg2rad(az)[:, None]
    x = rng * np.sin(az_rad)
    y = rng * np.cos(az_rad)
    
    return ref_var,ref_data,x,y

def raw_to_masked_float(ref_var, ref_data):
    # Values come back signed. If the _Unsigned attribute is set, we need to convert
    # from the range [-127, 128] to [0, 255].
    if ref_var._Unsigned:
        ref_data = ref_data & 255

    # Mask missing points
    ref_data = np.ma.array(ref_data, mask=ref_data==0)

    # Convert to float using the scale and offset
    return ref_data * ref_var.scale_factor + ref_var.add_offset

def get_product_cbar_args(prod_name,ax,cbar,outline_effect):
    if prod_name == "Reflectivity":
        ticks = np.arange(-20,80,10)
        Y = 23
    if prod_name == "Velocity":
        ticks = [-60,-45,-20,0,20,45,60]    
        Y = -11
        cbar.ax.text(-76, Y, "RF", ha='center', va='center',path_effects=outline_effect,color="w",fontsize=6) #RF
        
    for count,ele in enumerate(ticks,0): 
        cbar.ax.text(ele, Y, ticks[count], ha='center', va='center',path_effects=outline_effect,color="w",fontsize=6)

def make_text_time_right(ax,end,title_time,dataset,
                         color="w",
                       fontsize=12):  
    
    text_time = ax.text(.995, 0.01, 
            f"{dataset} (dbz)"+"\n"+title_time,
            horizontalalignment='right', transform=ax.transAxes,
            color=color, fontsize=fontsize, weight='bold',zorder=15)
    outline_effect = [patheffects.withStroke(linewidth=5, foreground='black')]
    text_time.set_path_effects(outline_effect)
    return text_time,ax

def make_text_time_left(ax,station, prod_name,product,
                        color="w",
                       fontsize=12):  
    
    text_time2 = ax.text(0.005, 0.01, 
                "Station: "+station+"\n"+prod_name+" ("+product+")",
                horizontalalignment='left', transform=ax.transAxes,
                color=color, fontsize=fontsize, weight='bold',zorder=15)
    outline_effect = [patheffects.withStroke(linewidth=5, foreground='black')]
    text_time2.set_path_effects(outline_effect)
    return text_time2,ax

def make_map(data,LatLonBox): 
    """
    -------------------
    Create map instance
    -------------------
    Initiate the map figure, axis, and projection
    
    Arguments
    ---------
    data: full data
    LatLonBox: lat/lon extent around radar station
    
    Returns
    -------
    fig: new figure
    ax: drawing axis
    proj: map/data projection
    """

    proj = ccrs.LambertConformal(central_longitude=data.StationLongitude,
                                       central_latitude=data.StationLatitude)

    fig = plt.figure(figsize=(17,11))
    ax = plt.subplot(111,projection=proj)
    
    ax.coastlines('50m', 'black', linewidth=2, zorder=2)

    reader = shpreader.Reader('/Users/chowdahead/Documents/shapefiles/countyl010g_shp_nt00964/countyl010g.shp')
    counties = list(reader.geometries())
    COUNTIES = cfeature.ShapelyFeature(counties,ccrs.PlateCarree())
    ax.add_feature(COUNTIES, facecolor='none',edgecolor='w')
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
    
    ax.set_extent(LatLonBox,ccrs.PlateCarree())
    
    return fig,ax,proj

def radar_plot(station,save_path,product,start,file_list,LatLonBox,
               save=True,show=False,index=0):
    
    """
    -------------------
    Plot radar data
    -------------------
    Take final arguments and plot the radar data
    
    Arguments
    ---------
    station: coded station name, ie FTG for Denver
    save_path: path for saved image
    product: abbreviated prodcut name ie N0V,N1P,etc
    start: datetime for start of data query
    file_list: list of queried files (.nids)
    dataset: shortened name of chosen THREDDS dataset
    LatLonBox: lat/lon extent around radar station
    index: file_list index number
    
    Returns
    -------
    fig: new figure
    ax: drawing axis
    proj: map/data projection
    """
    
    data, title_time, file_time = get_radar_data(file_list,index=0)
    
    prod_name,thredds_product = get_prod_name(product)
    
    ref_var,ref_data,x,y = get_radar_vars(data,prod_name)
    
    ref_data = raw_to_masked_float(ref_var, ref_data)
    
    
    if prod_name == "Velocity":
        cmap = rad_vel_cmap
        vmin=-80
        vmax=80
        
    if prod_name == "Reflectivity":
        cmap = refl_cmap
        vmin=-40
        vmax=84.5
        
    fig,ax,proj = make_map(data,LatLonBox)
    
    mesh = ax.pcolormesh(x,y,ref_data,cmap=cmap,vmin=vmin,vmax=vmax,transform=proj)
    #mesh = ax.pcolormesh(x,y,radar_data,cmap=ref_cmap, norm=ref_norm)
    
    cbar = plt.colorbar(mesh, orientation='horizontal')
    posn = ax.get_position()
    outline_effect = [patheffects.withStroke(linewidth=3, foreground='k')]
    cbar.ax.set_position([posn.x0+0.001, posn.y0-0.001,
                            (posn.x1-posn.x0)/2, posn.height])
    #params = {
    #          "xtick.color" : "k",
    #          "ytick.color" : "k",
    #          "font.size" : 10,
    #              }
    #plt.rcParams.update(params)
    
    cbar.set_ticks([])
    cbar.ax.set_xticklabels([])      
        
    get_product_cbar_args(prod_name,ax,cbar,outline_effect)
  
    make_text_time_right(ax,start,title_time,"Radar S3 NEXRAD Level II")
    make_text_time_left(ax,station, prod_name,product)
    
    if save == True:
        plt.savefig(f"{save_path+station}_RadarL2_{prod_name}thredds_{file_time}.png",bbox_inches="tight",dpi=200)
    #plt.savefig(save_path+station+"_RadarL3_"+prod_name+"_thredds_"+file_time+".png",bbox_inches="tight",dpi=200)
    #plt.close(fig)    
    if show == True:
        plt.show()                               

def example():
    """
    ------------
    Example plot
    ------------
    Plot reflectivity for Denver (KFTG) on May 16th, 2020
    
    Simply run example()
    """
    station = "KFTG"
    product = 'N0Q'
    start = datetime(2020,5,16,0,0)

    file_list,LatLonBox = query_radar_data(station,product,start,
                     minute_delta=30,hour_delta=0,day_delta=0)
    radar_plot(station,save_path,product,start,file_list,LatLonBox,save=False,show=True,index=0)

