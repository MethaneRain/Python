#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 22:19:49 2020

@author: Justin Richling
"""

class THREDDS_Radar:
    author = "Justin Richling"
    
    def __init__(self,author):
        self.author=author
        
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
    
#class Meteorologist:
#    education = "Atmospheric Science"#
#
#    def __init__(self,name,age,employer):
#        self.name = name
#        self.age = age
#        self.employer = employer

#    def description(self):
#        return f"Hi, my name is {self.name} and I'm {self.age} years old and work for {self.employer}!"