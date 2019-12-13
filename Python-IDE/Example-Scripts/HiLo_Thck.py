#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 08:46:57 2019

@author: Justin Richling
"""

def HiLo_Thck(time_index,im_save_path,state_borders,country_borders,time_strings,
            time_final,today_year,font,extent,datacrs,plotcrs,hgt,mslp,data,lats,lons,
            pv,colorbar_axis):
    
    import numpy as np
    import matplotlib.pyplot as plt
    import os
    from scipy.ndimage import gaussian_filter
    from metpy.plots import add_metpy_logo
    
    def plot_maxmin_points(ax,lon, lat, data, extrema, nsize, symbol,color='k',
                       plotValue=True, transform=None):

        """
        I have added some path effects on the symbols and pressure readings - outlining them in black 
        to make them pop a bit more.
        
        
        This function will find and plot relative maximum and minimum for a 2D grid. The function
        can be used to plot an H for maximum values (e.g., High pressure) and an L for minimum
        values (e.g., low pressue). It is best to used filetered data to obtain  a synoptic scale
        max/min value. The symbol text can be set to a string value and optionally the color of the
        symbol and any plotted value can be set with the parameter color
        lon = plotting longitude values (2D)
        lat = plotting latitude values (2D)
        data = 2D data that you wish to plot the max/min symbol placement
        extrema = Either a value of max for Maximum Values or min for Minimum Values
        nsize = Size of the grid box to filter the max and min values to plot a reasonable number
        symbol = String to be placed at location of max/min value
        color = String matplotlib colorname to plot the symbol (and numerica value, if plotted)
        plot_value = Boolean (True/False) of whether to plot the numeric value of max/min point
        The max/min symbol will be plotted on the current axes within the bounding frame
        (e.g., clip_on=True)
        """
        import numpy as np
        from matplotlib import patheffects
        from scipy.ndimage.filters import maximum_filter, minimum_filter
        outline_effect = [patheffects.withStroke(linewidth=2.5, foreground='black')]
    
        if (extrema == 'max'):
            data_ext = maximum_filter(data, nsize, mode='nearest')
        elif (extrema == 'min'):
            data_ext = minimum_filter(data, nsize, mode='nearest')
        else:
            raise ValueError('Value for hilo must be either max or min')
        
        mxy, mxx = np.where(data_ext == data)
        #print(mxy,mxx)
        
        for i in range(len(mxy)):
            A = ax.text(lon[mxy[i], mxx[i]], lat[mxy[i], mxx[i]], symbol, color=color, size=24,
                    clip_on=True, horizontalalignment='center', verticalalignment='center',
                    transform=transform)
            A.set_path_effects(outline_effect)
            B = ax.text(lon[mxy[i], mxx[i]], lat[mxy[i], mxx[i]]-0.66,
                    str(np.int(data[mxy[i], mxx[i]])),
                    color=color, size=12, clip_on=True, fontweight='bold',
                    horizontalalignment='center', verticalalignment='top', transform=transform)
            B.set_path_effects(outline_effect)
        
       
    
    
    
    
    

                                # Setup Contour Label Options
#---------------------------------------------------------------------------------------------------    
    kw_clabels = {'fontsize': 11, 'inline': True, 'inline_spacing': 5, 'fmt': '%i',
              'rightside_up': True, 'use_clabeltext': True}

                                    # Setup Figure
#---------------------------------------------------------------------------------------------------    
    fig = plt.figure(figsize=(17., 11.))

    #add_metpy_logo(fig, 25, 925, size='small')

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
    ax.set_title('GFS 20km CONUS: MSLP w/ Highs/Lows and\n1000-500mb Thickness (m)', 
                 size=16, loc='left',fontdict=font)
    
    ax.set_title(f"Init Hour: {init_date} {init_hour}\nForecast Hour: {forecast_date} {forecast_hour}",
                 size=16, loc='right',fontdict=font)

    
                                    # 1000-500mb Thickness
#---------------------------------------------------------------------------------------------------
    hgt_500 = hgt[time_strings.index(time),data.variables["isobaric1"][:].tolist().index(50000),:,:]
    hgt_1000 = hgt[time_strings.index(time),data.variables["isobaric1"][:].tolist().index(100000),:,:]
    thickness_1000_500 = gaussian_filter(hgt_500 - hgt_1000, sigma=3.0)
    
    clevs = (np.arange(0, 5400, 60), np.arange(5400,5401,1), np.arange(5460, 7000, 60))
    colors = ('tab:blue', 'b', 'tab:red')
    
    for clevthick, color in zip(clevs, colors):
        cs = ax.contour(lons, lats, thickness_1000_500, levels=clevthick, colors=color,
                    linewidths=1.0, linestyles='dashed', transform=datacrs)
        plt.clabel(cs, **kw_clabels)

                                           # MSLP
#---------------------------------------------------------------------------------------------------
    clevmslp = np.arange(800., 1120., 4)
    cs2 = ax.contour(lons, lats, mslp[time_strings.index(time),:,:], clevmslp, colors='k', linewidths=1.25,
                 linestyles='solid', transform=datacrs)
    plt.clabel(cs2, **kw_clabels)

                                    # High and Low Symbols
#---------------------------------------------------------------------------------------------------
    #HL(ax,lon_2d, lat_2d, mslp[time_strings.index(time),:,:], 'max', 50, symbol='H',color='b',  transform=datacrs)
    #HL(ax,lon_2d, lat_2d, mslp[time_strings.index(time),:,:], 'min', 25, symbol='L',color='r', transform=datacrs)
    plot_maxmin_points(ax,lons, lats, mslp[time_strings.index(time),:,:], 'max', 50, symbol='H',color='b',  transform=datacrs)
    plot_maxmin_points(ax,lons, lats, mslp[time_strings.index(time),:,:], 'min', 25, symbol='L',color='r', transform=datacrs)
    
                                        # Save Figure
#---------------------------------------------------------------------------------------------------    
    GFS_HILO = im_save_path+"GFS/HILO/"
    if not os.path.isdir(GFS_HILO):
        os.makedirs(GFS_HILO)
        
    time_index *= 3
    if time_index < 10:
        times = f"0{time_index}"
    else:
        times = f"{time_index}"

    outfile = f"{GFS_HILO}GFS_20km_HL_Thickness_{file_time}_F{times}.png"
    fig.savefig(outfile,bbox_inches='tight',dpi=120)
    plt.close(fig)
    
    
    