#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 22:24:19 2020

@author: Justin Richling
"""
def make_vel_cmap():
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

    return rad_vel_cmap