#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 23:37:11 2020

@author: Justin Richling
"""

def get_prod_name(product,prod_list=None):
    
    '''
    Method to check the names associated with a particular radar product
    '''
    
    if prod_list == None:
        Prod_list = {"N0V":{"prod_name":"Velocity","dataset_name":"RadialVelocity"},
                 "N1P":{"prod_name":"Precip1hr","dataset_name":"Precip1hr"},
                 "N0Q":{"prod_name":"Reflectivity","dataset_name":"BaseReflectivityDR"},
                 "N0S":{"prod_name":"StormMeanVelocity","dataset_name":"StormMeanVelocity"},
                 "N0C":{"prod_name":"CC","dataset_name":"CorrelationCoefficient"},
                 "N0H":{"prod_name":"HydroClass","dataset_name":"HydrometeorClassification"},
        
        }
    else:
        prod_list=prod_list
        
    prod_name = Prod_list[product]["prod_name"]
    dataset_name = Prod_list[product]["dataset_name"]
    print("product name:",prod_name,"name for variable in dataset:",dataset_name)
    return prod_name,dataset_name

