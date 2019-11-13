#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def plot_maxmin_points(Ax,lon, lat, data, extrema, nsize, symbol, model,color='k',
                       plotValue=True, transform=None):
    
    """
    MetPy Function for plotting High and Low symbols with pressures, so credit to the team at Unidata for 
    allowing such an integral graphics piece. (MetPy Comments Below...)

    I have added some code to allow for RAP and GFS Lat/Lon dimensions since they differ in the grib files from 
    THREDDS.

    I have also added some path effects on the symbols and pressure readings - outlining them in black 
    to make them pop a bit more.

    Required Arguments: 
    * Ax - Axes to plot H/L on 
    * lat - latitudes
    * lon - longitudes
    * data - 2d data (ex. MSLP or 500mb Heights)
    * extrema - labels for max and min
    * symbol - H or L
    * model - RAP or GFS, etc. The data is different so model must be specified
        - GFS and RAP have been tested so far. 
        - Still need to look at NAM and others...

    Optional Arguments:
    * color -  can be overwritten (defualt black)
    * plotValue - ??
    * transform - transform the plot into data projection

    """
    
    """
    MetPy Comments:
    
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
        if model == "RAP" or "NAM":
            """
            A = AX.text(lon[mxy[i], mxx[i]], lat[mxy[i], mxx[i]], symbol, color=color, size=24,
                    clip_on=True, horizontalalignment='center', verticalalignment='center',
                    transform=transform)
            A.set_path_effects(outline_effect)

            B = AX.text(lon[mxy[i], mxx[i]], lat[mxy[i], mxx[i]],
                    str(np.int(data[mxy[i], mxx[i]])),
                    color=color, size=12, clip_on=True, fontweight='bold',
                    horizontalalignment='center', verticalalignment='top', transform=transform)
            B.set_path_effects(outline_effect)
            """
            A = Ax.text(lon[mxy[i], mxx[i]], lat[mxy[i], mxx[i]], symbol, color=color, size=24,
                    clip_on=True, horizontalalignment='center', verticalalignment='center',
                    transform=transform)
            A.set_path_effects(outline_effect)
            B = Ax.text(lon[mxy[i], mxx[i]], lat[mxy[i], mxx[i]]-0.66,
                    str(np.int(data[mxy[i], mxx[i]])),
                    color=color, size=12, clip_on=True, fontweight='bold',
                    horizontalalignment='center', verticalalignment='top', transform=transform)
            B.set_path_effects(outline_effect)
            
        if model == "GFS":
            A = Ax.text(lon[mxx[i]], lat[mxy[i]], symbol, color=color, size=24,
                    clip_on=True, horizontalalignment='center', verticalalignment='center',
                    transform=transform)
            A.set_path_effects(outline_effect)

            B = Ax.text(lon[mxx[i]], lat[mxy[i]]-0.66,
                    str(np.int(data[mxy[i], mxx[i]])),
                    color=color, size=12, clip_on=True, fontweight='bold',
                    horizontalalignment='center', verticalalignment='top', transform=transform)
            B.set_path_effects(outline_effect)


    

