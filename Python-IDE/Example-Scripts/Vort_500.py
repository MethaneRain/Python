#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 08:52:43 2019

@author: Justin Richling
"""

def Vort_500(time_index,im_save_path,state_borders,country_borders,time_strings,
            time_final,today_year,font,extent,datacrs,plotcrs,hgt,vort,data,lats,lons,
            pv,colorbar_axis,vort_cmap):
    
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

    #add_metpy_logo(fig, 25, 950, size='small')

                                    # Add the Map 
#---------------------------------------------------------------------------------------------------
    ax = plt.subplot(111, projection=plotcrs)

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
    ax.set_title('GFS 20km CONUS: 500mb Heights and Abs Vorticity '+ "("+"$\mathregular{s^{-1}}$"+")", 
                 size=16, loc='left',fontdict=font)
    
    ax.set_title(f"Init Hour: {init_date} {init_hour}\nForecast Hour: {forecast_date} {forecast_hour}",
                 size=16, loc='right',fontdict=font)

    
                                        # 500mb Heights
#---------------------------------------------------------------------------------------------------
    hgt_500 = hgt[time_strings.index(time),data.variables["isobaric1"][:].tolist().index(50000),:,:]

    clev500 = np.arange(5200, 6000, 60)
    cs = ax.contour(lons, lats, hgt_500,clev500 ,colors='black', linewidths=2.0,
                    linestyles='solid', transform=datacrs)
    plt.clabel(cs, **kw_clabels)

                                        # Vorticity
#---------------------------------------------------------------------------------------------------
    vort_500 = vort[time_strings.index(time),data.variables["isobaric"][:].tolist().index(50000),:,:]

    vort_levels = np.arange(-.00055,.0007,0.00001)
    cs2 = ax.contourf(lons, lats, vort_500,vort_levels,
                     transform=datacrs,cmap=vort_cmap)
    
    cbaxes = fig.add_axes(colorbar_axis) # [left, bottom, width, height]
    cbar = plt.colorbar(cs2, orientation='horizontal',cax=cbaxes)
    
    #cbar.set_label(r'$s{^-1}$')
    #plt.clabel(cs2, **kw_clabels)

                                        # Save Figure
#---------------------------------------------------------------------------------------------------    
    VORT = im_save_path+"GFS/Vorticity/"
    if not os.path.isdir(VORT):
        os.makedirs(VORT)
        
    time_index *= 3
    if time_index < 10:
        times = f"0{time_index}"
    else:
        times = f"{time_index}"

    outfile = f"{VORT}GFS_20km_Vort_Heights_500mb_{file_time}_F{times}.png"
    fig.savefig(outfile,bbox_inches='tight',dpi=120)
    plt.close(fig)
