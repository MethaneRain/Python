#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 22:14:51 2020

@author: Justin Richling
"""


from metpy.plots import ctables

#reflec_norm, reflec_cmap = ctables.registry.get_with_steps('NWSReflectivity', 5, 5)
reflec_norm, reflec_cmap = ctables.registry.get_with_steps('NWSStormClearReflectivity',-20., 0.5)

import get_prod_name
prod_name,dataset_name = get_prod_name.get_prod_name("N0V",None)

import query_radar
query_radar.query_data()

#__main__