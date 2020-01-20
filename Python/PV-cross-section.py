#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 17:08:18 2020

@author: chowdahead
"""

from metpy.plots import ctables
mycmap = ctables.registry.get_colortable("NWSReflectivity")
import xarray as xr
import numpy as np

def Cross(data, start, end):
    from metpy.interpolate import cross_section
    import metpy
    import metpy.calc as mpcalc
   
    import matplotlib.pyplot as plt
    
    # Define the figure object and primary axes
    fig = plt.figure(1, figsize=(16., 9.))
    ax = plt.axes()
    
    cross = cross_section(data, start, end)
    cross.set_coords(('lat', 'lon'), True)
        #print(cross['isobaric'])
    temperature, pressure = xr.broadcast(cross['Temperature_isobaric'],cross['isobaric4'])
    
    theta = mpcalc.potential_temperature(pressure, temperature)
        #rh = mpcalc.relative_humidity_from_specific_humidity(specific_humidity, temperature, pressure)
    
        # These calculations return unit arrays, so put those back into DataArrays in our Dataset
    cross['Potential_temperature'] = xr.DataArray(theta,
                                                      coords=temperature.coords,
                                                      dims=temperature.dims,
                                                      attrs={'units': theta.units})
        #cross['Relative_humidity'] = xr.DataArray(rh,
        #                                          coords=specific_humidity.coords,
        #                                          dims=specific_humidity.dims,
        #                                          attrs={'units': rh.units})
    
    u = cross['u-component_of_wind_isobaric'].metpy.convert_units('knots')
    v = cross['v-component_of_wind_isobaric'].metpy.convert_units('knots')
    cross['t_wind'], cross['n_wind'] = mpcalc.cross_section_components(cross['u-component_of_wind_isobaric'],
                                                                           cross['v-component_of_wind_isobaric'])
    #wind = metpy.calc.wind_speed(u, v)
    levels = np.arange(30, 100, 3)
    #levels = [30:100]
    theta_contour = ax.contour(cross['lon'], cross['isobaric4'], cross['Potential_temperature'][0,:,:],
                               levels=np.arange(250, 850, 3), colors='k', linewidths=2)
    wind_contour = ax.contour(cross['lon'], cross['isobaric'], 
            metpy.calc.wind_speed(cross['u-component_of_wind_isobaric'],cross['v-component_of_wind_isobaric'])[0,:,:],
                               levels=levels, colors='r', linewidths=2)
    import matplotlib.patheffects as mp
    for text in plt.clabel(wind_contour, colors='r',fmt='%d'):
        text.set_path_effects([mp.withStroke(foreground='k',
                                                       linewidth=3)])
        #text.set_bbox({'boxstyle': 'sawtooth', 'facecolor': 'none',
        #               'edgecolor': 'blue'})
    
        
    
    #cs_opts = {'fmt' : '%d', 'fontsize' : 14,
    #           'colors' : 'r'}
    #plt.clabel(wind_contour,**cs_opts)
    
    #fmt='%d',weight='bold'
    #wind_slc_vert = list(range(0, 19, 2)) + list(range(19, 29))
    #wind_slc_horz = slice(5, 100, 5)
    #ax.contour(cross['lon'][wind_slc_horz], cross['isobaric'][wind_slc_vert],
    #     cross['t_wind'][wind_slc_vert, wind_slc_horz],
    #     cross['n_wind'][wind_slc_vert, wind_slc_horz], color='k')
    
    
    # Adjust the y-axis to be logarithmic
    #ax.set_yscale('symlog')
    plt.yscale('log')
    #ax.set_yticklabels(np.arange(1000, 50, -100))
    #ax.set_ylim(cross['isobaric'].max(), cross['isobaric'].min())
    ax.set_ylim(cross['isobaric'].max(), cross['isobaric'][10])
    
    
File = "~/Desktop/GFS_Global_0p25deg_20190916_1200.grib2.nc"
data = xr.open_dataset(File)

data = data.metpy.parse_cf().squeeze()


start = (45, -110.0)
end = (35, -97.0)

inset = (0.0255, 0.45, 0.43, 0.43)
extent = [start[1]-5,end[1]+5,start[0]+5,end[0]-5]


Cross(data, start, end)

