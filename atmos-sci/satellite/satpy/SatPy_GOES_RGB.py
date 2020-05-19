#!/usr/bin/env python
# coding: utf-8

# Author: Justin Richling
# Date: 2020 May 19

import os
from satpy import Scene, DatasetID
import glob
from satpy.multiscene import MultiScene
from satpy.writers import get_enhanced_image

import matplotlib.pyplot as plt
from matplotlib import patheffects

import cartopy.crs as ccrs
import cartopy.feature as cfeature

from datetime import datetime
from siphon.catalog import TDSCatalog


from satpy import available_readers
available_readers()


def get_current_julian(Year,Month,Day,now=False):
    # Set the date you want to convert
    dt = datetime(Year,Month,Day)
    if now == True:
        dt = datetime.utcnow()

    # Start of year for reference
    d0 = datetime(Year, 1, 1)

    # Find the difference and add one to get the day number of the calander year
    delta = dt - d0
    Julian_Day = delta.days+1
    if Julian_Day < 100:
        Julian_Day = "0"+str(Julian_Day)
        if int(Julian_Day) < 10:
            Julian_Day = "0"+str(Julian_Day)

    Year = str('{0:%Y}'.format(dt))
    Month = str('{0:%m}'.format(dt))
    Day = str('{0:%d}'.format(dt))

    #'{0:%Y}'.format(dt)+"-"+'{0:%m}'.format(dt)+"-"+'{0:%d}'.format(dt)+"-"+'{0:%H}'.format(dt)
    print(f"date: {Year}-{Month}={Day}")

    # Julian day (Day)
    print(f"Julian number: {Julian_Day}")
    return Year,Month,Day,Julian_Day


Year,Month,Day,Julian_Day = get_current_julian(2020,1,10,now=True)
Year,Month,Day,
Julian_Day = 139


GOES_sample_path = f"/Users/chowdahead/Downloads/WX_Data/GOES_Data/"
GOES_sample_path

os.chdir(GOES_sample_path)

def make_movie():
    all_filenames = [glob.glob(fn.replace('C01', 'C0[123]*')[:len(GOES_sample_path) + 50] + '*.nc') for fn in sorted(glob.glob(os.path.join(GOES_sample_path, 'OR*-Rad*C01*.nc')))]
    print(all_filenames)
    scenes = [Scene(reader='abi_l1b', filenames=filenames) for filenames in all_filenames]
    print("Number of Scenes: ", len(scenes))
    
    mscn = MultiScene(scenes)
    mscn.load(['true_color'])
    
    new_mscn = mscn.resample(resampler='native')
    new_mscn.save_animation(GOES_sample_path+'/{name}_{start_time:%Y%m%d_%H%M%S}.mp4', fps=5)



filenames = glob.glob(GOES_sample_path+"*.nc")
filenames

product = "true_color"

scn = Scene(reader='abi_l1b', filenames=filenames)
print(scn.all_composite_names())
scn.load([product])

new_scn = scn.resample(scn.min_area(), resampler='native')   
new_scn.show(product)

def GOES_RGB(product,filenames,extent=None,projection=None):
    
    scn = Scene(reader='abi_l1b', filenames=filenames)
    print(scn.all_composite_names())
    scn.load([product])

    
    new_scn = scn.resample(resampler='native') #scn.min_area(),

    
    #var = get_enhanced_image(scn[product]).data
    var = get_enhanced_image(new_scn[product]).data
    # Get true color data to use later and reorder the dimensions so matplotlib can use the image
    # Sadly, this operation is not lazy (bad performance) in xarray at the time of writing
    var = var.transpose('y', 'x', 'bands')
    
    fig = plt.figure(figsize=(20, 10), dpi=200)
    abi_crs = var.attrs['area'].to_cartopy_crs()
    if projection == None:
        proj=abi_crs
    if projection == "lambert":
        proj = ccrs.LambertConformal()
    if projection == "plate":
        proj = ccrs.PlateCarree()
        
    
    ax = fig.add_subplot(1, 1, 1, projection=proj)

    ax.add_feature(cfeature.COASTLINE.with_scale('10m'), edgecolor='w')
    ax.add_feature(cfeature.STATES.with_scale('10m'), edgecolor='w')
    if extent !=None:
        ax.set_extent(extent, crs=ccrs.PlateCarree())
    else:
        ax.set_extent([-130,-70,20,55], crs=ccrs.PlateCarree())

    ax.imshow(var.data, extent=(var.x[0], var.x[-1], var.y[-1], var.y[0]), origin='upper',
             transform=abi_crs)
    
    #title = scn[product].orbital_slot
    #title2 = f"{scn[product].standard_name.capitalize()}-{scn[product].mode}"
    #title_time = "{0:%d-%B-%Y %H%MZ}".format(scn[product].start_time)
    
    title = new_scn[product].orbital_slot
    title2 = new_scn[product].standard_name.capitalize()+"-"+new_scn[product].mode
    title_time = "{0:%d-%B-%Y %H%MZ}".format(new_scn[product].start_time)
    
    text_time = ax.text(.995, 0.01, 
            title_time,
            horizontalalignment='right', transform=ax.transAxes,
            color='white', fontsize=20, weight='bold')

    text_time2 = ax.text(0.005, 0.01, 
            title+"\n"+title2,
            horizontalalignment='left', transform=ax.transAxes,
            color='white', fontsize=20, weight='bold')

    outline_effect = [patheffects.withStroke(linewidth=5, foreground='black')]
    text_time.set_path_effects(outline_effect)
    text_time2.set_path_effects(outline_effect)

    plt.savefig(f"GOES_rgb_{product}.png",bbox_inches="tight")


GOES_RGB("airmass",filenames,extent=[-120,-70,20,55])

