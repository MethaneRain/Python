#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 22:30:10 2020

@author: Justin Richling
"""
from matplotlib import patheffects
def make_text_time_right(ax,end,
                         color="w",
                       fontsize=12):  
    
    text_time = ax.text(.995, 0.01, 
            "NWS Level 3 Radar (dbz)"+"\n"+"{0:%Y-%m-%d %H%MZ}".format(end),
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

