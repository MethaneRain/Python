#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


def create_colormap(colors, position=None, bit=False, reverse=False, name='custom_colormap'):
    """
    returns a linear custom colormap
    Parameters
    ----------
    colors : array-like
        contain RGB values. The RGB values may either be in 8-bit [0 to 255]
        or arithmetic [0 to 1] (default).
        Arrange your tuples so that the first color is the lowest value for the
        colorbar and the last is the highest.
    position : array like
        contains values from 0 to 1 to dictate the location of each color.
    bit : Boolean
        8-bit [0 to 255] (in which bit must be set to
        True when called) or arithmetic [0 to 1] (default)
    reverse : Boolean
        If you want to flip the scheme
    name : string
        name of the scheme if you plan to save it
    Returns
    -------
    cmap : matplotlib.colors.LinearSegmentedColormap
        cmap with equally spaced colors
    """
    from matplotlib.colors import LinearSegmentedColormap
    import numpy as np
    if not isinstance(colors, np.ndarray):
        colors = np.array(colors, dtype='f')
    if reverse:
        colors = colors[::-1]
    if position is not None and not isinstance(position, np.ndarray):
        position = np.array(position)
    elif position is None:
        position = np.linspace(0, 1, colors.shape[0])
    else:
        if position.size != colors.shape[0]:
            raise ValueError("position length must be the same as colors")
        elif not np.isclose(position[0], 0) and not np.isclose(position[-1], 1):
            raise ValueError("position must start with 0 and end with 1")
    if bit:
        colors[:] = [tuple(map(lambda x: x / 255., color)) for color in colors]
    cdict = {'red':[], 'green':[], 'blue':[]}
    for pos, color in zip(position, colors):
        cdict['red'].append((pos, color[0], color[0]))
        cdict['green'].append((pos, color[1], color[1]))
        cdict['blue'].append((pos, color[2], color[2]))
    return LinearSegmentedColormap(name, cdict, 256)


# In[ ]:


colors=[(30,30,30),(50,50,50),(65,65,65),(80,80,80),(90,90,90),(100,100,100),(108,108,108),(114,114,114),
        (120,120,120),(130,130,130),(150,150,150),(180,180,180),(190,190,190),(200,200,200),(211,211,211),
        (220,220,220),(230,230,230),(244,244,244),(255, 255, 255),(255, 255, 255),(255, 255, 255),
        (230,250,230),(0, 100, 0),(50,200,50),(200,255,47),(255,255,0),(255,200,50),(255,150,80),
        (255,100,50),(255,0,0),(180,0,0),(140,0,0),(100,0,0),(150,10,0),(208,32,144),(150,32,144),
        (108,32,144),(0,0,100),(0,0,255),(0,150,150),(135,206,250)]

my_cmap = create_colormap(colors, bit=True)


# In[ ]:


import numpy as np
vort_levels = np.arange(-.00055,.0007,0.00001)
