#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 23:29:28 2020

@author: Justin Richling
"""

def query_data(cat_prod='NEXRAD Level III Radar from IDD'):
    
    '''
    Catalog Products:
    ------------------
    * 'NEXRAD Level II Radar for Case Study CCS039'
    * 'NEXRAD Level II Radar from IDD'
    * 'NEXRAD Level III Radar for Case Study CCS039'
    * 'NEXRAD Level III Radar from IDD'
    * 'TDWR Level III Radar from IDD'
    '''
    
    from siphon.radarserver import get_radarserver_datasets, RadarServer
    
    ds = get_radarserver_datasets('http://thredds.ucar.edu/thredds/')
    print(list(ds))
    url = ds[cat_prod].follow().catalog_url
    rs = RadarServer(url)
    
    
    return rs