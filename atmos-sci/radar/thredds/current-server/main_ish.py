#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 22:14:51 2020

@author: Justin Richling
"""

from datetime import datetime, timedelta
import time
from siphon.catalog import TDSCatalog
from siphon.radarserver import RadarServer
import cartopy
from siphon.cdmr import Dataset
import matplotlib.pyplot as plt

import metpy
from metpy.plots import ctables
from matplotlib import patheffects
#reflec_norm, reflec_cmap = ctables.registry.get_with_steps('NWSReflectivity', 5, 5)
reflec_norm, reflec_cmap = ctables.registry.get_with_steps('NWSStormClearReflectivity',-20., 0.5)

import pandas as pd
from matplotlib.colors import LinearSegmentedColormap
rad_vel = pd.read_csv("/Users/chowdahead/Downloads/radial_velocity_cmap.csv")
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


cat = TDSCatalog("http://thredds.ucar.edu/thredds/radarServer/catalog.xml")
rs = RadarServer(cat.catalog_refs['NEXRAD Level III Radar from IDD'].href)

