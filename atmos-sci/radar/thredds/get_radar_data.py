#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 23:24:10 2020

@author: Justin Richling
"""

def get_radar_data(rs,station,product,dataset_name,start,end):
    import numpy as np
    query = rs.query()
    query.stations(station).time_range(start,end).variables(product)
    print(end)
    filetime = "{0:%Y_%m_%d_%H%MZ}".format(end)
    query_cat = rs.get_catalog(query)
    data = query_cat.datasets[0].remote_access()
    

    range_data = data.variables['gate'][:]
    azimuth_data = data.variables['azimuth'][:]
    radar_data = data.variables[dataset_name][:]

    x = range_data*np.sin(np.deg2rad(azimuth_data))[:,None]
    y = range_data*np.cos(np.deg2rad(azimuth_data))[:,None]
    
    return data,range_data,azimuth_data,radar_data,x,y,filetime