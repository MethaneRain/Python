#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 22:14:51 2020

@author: Justin Richling
"""


from metpy.plots import ctables
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

import make_vel_cmap
rad_vel_cmap = make_vel_cmap.make_vel_cmap()
#reflec_norm, reflec_cmap = ctables.registry.get_with_steps('NWSReflectivity', 5, 5)
reflec_norm, reflec_cmap = ctables.registry.get_with_steps('NWSStormClearReflectivity',-20., 0.5)

station = "FTG"
save_path = "/Users/chowdahead/Desktop/"
product = "N0Q"
Year = 2020
Month = 4
Day = 22
Hour = 22
Minute = 0
start = datetime(Year,Month,Day,Hour,Minute)
end = datetime(Year,Month,Day,Hour,Minute)

import get_prod_name
prod_name,dataset_name = get_prod_name.get_prod_name(product,None)

import query_radar
rs = query_radar.query_data()

import get_radar_data
data,range_data,azimuth_data,radar_data,x,y,filetime,LatLonBox = get_radar_data.get_radar_data(rs,station,product,dataset_name,start,end)

print(filetime)

import make_map
fig,ax,proj = make_map.make_map(data,LatLonBox)

mesh = ax.contourf(x,y,radar_data,np.arange(-90,90,5),cmap=reflec_cmap,norm=reflec_norm)
    #mesh = ax.pcolormesh(x,y,radar_data,cmap=ref_cmap, norm=ref_norm)
    
cbar = plt.colorbar(mesh, orientation='vertical',pad=0.005,aspect=50)
    #cbar = plt.colorbar(mesh, ticks=[steps],pad=0.005,aspect=50)
    #cbar.ax.set_yticklabels(['-110',"-90","-70","-50","-30", "-10",'0', 
    #                         "10", "30", "50", "70", "90",'110'])  # vertically oriented colorbar

import make_fig_titles
make_fig_titles.make_text_time_right(ax,end)
make_fig_titles.make_text_time_left(ax,station, prod_name,product)
    
plt.savefig(save_path+station+"_RadarL3_"+prod_name+"_thredds_"+filetime+".png",bbox_inches="tight")