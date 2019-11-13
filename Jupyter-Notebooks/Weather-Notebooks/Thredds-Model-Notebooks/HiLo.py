
def plot_maxmin_points(Ax,lon, lat, data, extrema, nsize, symbol,color='k',
                       plotValue=True, transform=None):

    """
    Some path effects on the symbols and pressure readings have been added - outlining them in black 
    to make them pop a bit more.
    
    An Ax argument has also been added to call the current axes to plot on - mainly used if importing this from an external folder
    
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
        A = Ax.text(lon[mxy[i], mxx[i]], lat[mxy[i], mxx[i]], symbol, color=color, size=24,
                    clip_on=True, horizontalalignment='center', verticalalignment='center',
                    transform=transform)
        A.set_path_effects(outline_effect)
        B = Ax.text(lon[mxy[i], mxx[i]], lat[mxy[i], mxx[i]]-0.66,
                    str(np.int(data[mxy[i], mxx[i]])),
                    color=color, size=12, clip_on=True, fontweight='bold',
                    horizontalalignment='center', verticalalignment='top', transform=transform)
        B.set_path_effects(outline_effect)
            

