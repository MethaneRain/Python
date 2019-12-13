#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 08:17:18 2019

@author: Justin Richling
"""

def PV_Jets(time_index,im_save_path,state_borders,country_borders,time_strings,
            time_final,today_year,font,extent,datacrs,plotcrs,u_wind,v_wind,data,lats,lons,
            pv,colorbar_axis):
    
    import metpy.calc as mpcalc
    import numpy as np
    import matplotlib.pyplot as plt
    import os
    from metpy.plots import add_metpy_logo

                                # Setup Contour Label Options
#---------------------------------------------------------------------------------------------------    
    kw_clabels = {'fontsize': 11, 'inline': True, 'inline_spacing': 5, 'fmt': '%i',
              'rightside_up': True, 'use_clabeltext': True}

                                    # Setup Figure
#---------------------------------------------------------------------------------------------------    
    fig = plt.figure(figsize=(17., 11.))
    ax = plt.subplot(111, projection=plotcrs)

    #add_metpy_logo(fig, 35, 985, size='small')

                                    # Add the Map 
#---------------------------------------------------------------------------------------------------
    

# Set extent and plot map lines
    ax.set_extent(extent, datacrs)
    
    ax.coastlines(resolution='50m')

                            # Add State/Country Boundaries to Plot
#---------------------------------------------------------------------------------------------------    
    
    ax.add_feature(state_borders, edgecolor='b', linewidth=1, zorder=3)
    
    
    ax.add_feature(country_borders,edgecolor='b',linewidth=0.2)
    
   
                                    # File and Title Times
#---------------------------------------------------------------------------------------------------
    # Time index for data variables
    time = time_strings[time_index]
    
    # Set string for saved image file name
    file_time = str(time_final[0]).replace("-","_").replace(" ","_").replace(":","")[:-2]+"Z"
    
    # Set forecast date and hour  
    forecast_date = "{}".format(today_year)+'-'+time_strings[time_index].replace("/","-")[:-5]
    forecast_hour = time_strings[time_index][-5:]+"Z"
    
    # Set initialization date and hour 
    init_date = "{}".format(today_year)+'-'+time_strings[0].replace("/","-")[:-5]
    init_hour = time_strings[0].replace("/","-")[-5:]+"Z"
    
    
                                        # Plot Title
#---------------------------------------------------------------------------------------------------   
    ax.set_title('GFS 20km CONUS: 250mb Jets (m/s) and\nPV Pressure Surface '+ 
    "("+"$\mathregular{2e^{-6}}$ $\mathregular{K}$ $\mathregular{m^{2}}$ $\mathregular{kg^{-1}}$ $\mathregular{s^{-1}}$"+")", 
                 size=16, loc='left',fontdict=font)
    
    ax.set_title(f"Init Hour: {init_date} {init_hour}\nForecast Hour: {forecast_date} {forecast_hour}",
                 size=16, loc='right',fontdict=font)

    
                                            # 250mb Jets
#---------------------------------------------------------------------------------------------------
    #hgt_500 = hgt[time_strings.index(time),data.variables["isobaric6"][:].tolist().index(50000),:,:]
    #Vort_500 = vort[time_strings.index(time),data.variables["isobaric6"][:].tolist().index(50000),:,:]
    u_250 = u_wind[time_strings.index(time),data.variables["isobaric1"][:].tolist().index(25000),:,:]
    v_250 = v_wind[time_strings.index(time),data.variables["isobaric1"][:].tolist().index(25000),:,:]
    wspd250 = mpcalc.get_wind_speed(u_250, v_250)
    
    clevsped250 = np.arange(40, 100, 5)
    cf = ax.contour(lons, lats, wspd250, clevsped250, colors='r', transform=datacrs)
    plt.clabel(cf, fontsize=10, inline=1, inline_spacing=10, fmt='%i',
               rightside_up=True, use_clabeltext=True,colors='k')

                                            # PV
#---------------------------------------------------------------------------------------------------
    pv_pos = pv[time_strings.index(time),1,:,:]
    
    clevPV = np.arange(7000, 78000, 1000)
    cs2 = ax.contourf(lons, lats, pv_pos,clevPV,alpha=0.7,antialiased = True,
                     transform=datacrs,cmap='cubehelix')

    cbaxes = fig.add_axes(colorbar_axis) # [left, bottom, width, height]

    cbar = plt.colorbar(cs2, orientation='horizontal',cax=cbaxes)
    
    
                                        # Save Figure
#---------------------------------------------------------------------------------------------------    
    PV_Jet = im_save_path+"GFS/PV_Jet/"
    if not os.path.isdir(PV_Jet):
        os.makedirs(PV_Jet)
        
    time_index *= 3
    if time_index < 10:
        times = f"0{time_index}"
    else:
        times = f"{time_index}"
    
    outfile = f"{PV_Jet}GFS_20km_Jet_PV_{file_time}_F{times}.png"
    fig.savefig(outfile,bbox_inches='tight',dpi=120)
    plt.cla()
    plt.close(fig)