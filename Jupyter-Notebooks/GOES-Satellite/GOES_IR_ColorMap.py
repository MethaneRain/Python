#!/usr/bin/env python
# coding: utf-8

# In[2]:


print("For plotting (ie pcolormesh, imshow, etc.) set the max/min:\nvmin=162.  vmax=330.")


# In[2]:


# Recreation of NESDIS IR color bar, thanks to Unidata for making this possible
def IR_Colormap():
    """
    This color bar is a recreation of the NESDIS Clean IR color bar, thanks to Unidata for
    archiveing mailing lists:
    
    https://www.unidata.ucar.edu/mailing_lists/archives/ldm-users/2018/msg00025.html
    
    Color bar credit to: Pete Pokrandt - Systems Programmer
    UW-Madison Dept of Atmospheric and Oceanic Sciences
    
    In the pcolormesh or imshow functions set:
        vmin=162.  and  vmax=330.
    
    """
    import matplotlib as mpl
    from matplotlib.colors import LinearSegmentedColormap
    red = []
    green = []
    blue = []
    valmin=-110.
    valmax=55.
    red.append( [0.0, 0.0, 0.0] ) 
    green.append( [0.0, 0.0, 0.0] )
    blue.append( [0.0, 0.0, 0.0] )
    red.append( [ (-50.0-valmin)/(valmax-valmin), 0.0, 0.0 ] )
    green.append( [ (-50.0-valmin)/(valmax-valmin), 1.0, 1.0 ] )
    blue.append( [ (-50.0-valmin)/(valmax-valmin), 0.0, 0.0 ] )
    red.append( [ (-40.0-valmin)/(valmax-valmin), 0.0, 0.0 ] )
    green.append( [ (-40.0-valmin)/(valmax-valmin), 0.0, 0.0 ] )
    blue.append( [ (-40.0-valmin)/(valmax-valmin), 0.4, 0.4 ] )
    red.append( [ (-30.0-valmin)/(valmax-valmin), 0.0, 0.8 ] )
    green.append( [ (-30.0-valmin)/(valmax-valmin), 1.0, 0.8 ] )
    blue.append( [ (-30.0-valmin)/(valmax-valmin), 1.0, 0.8 ] )
    red.append( [ 1.0, 0.0, 0.0 ] )
    green.append( [ 1.0, 0.0, 0.0 ] )
    blue.append( [ 1.0, 0.0, 0.0 ] )
    cdict = {'red': red, 'green': green, 'blue': blue}
    ctbl = LinearSegmentedColormap('custom', cdict)

    cdict = {'red': ((0.0, 0.0, 0.0),
                     (.001, 1.00, 1.00),
                     (.107, 1.00, 1.00),
                     (.113, 0.498, 0.498),
                     (.173, 1.00, 1.00),
                     (.179, 0.902, 0.902),
                     (.227, 0.102, 0.102),
                     (.233, 0.00, 0.00),
                     (.287, 0.902, 0.902),
                     (.293, 1.00, 1.00),
                     (.346, 1.00, 1.00),
                     (.352, 1.00, 1.00),
                     (.406, 0.101, 0.101),
                    (.412, 0.00, 0.00),
                     (.481, 0.00, 0.00),
                     (.484, 0.00, 0.00),
                     (.543, 0.00, 0.00),
                     (.546, 0.773, 0.773),
                     (.994, 0.012, 0.012),
                     (.997, 0.004, 0.004),
                     (1.0, 0.0, 0.0)),
             'green': ((0.0, 0.0, 0.0),
                     (.001, 1.00, 1.00),
                     (.107, 1.00, 1.00),
                     (.113, 0.00, 0.00),
                     (.173, 0.498, 0.498),
                     (.179, 0.902, 0.902),
                     (.227, 0.102, 0.102),
                     (.233, 0.00, 0.00),
                     (.287, 0.00, 0.00),
                     (.293, 0.00, 0.00),
                     (.346, 0.902, 0.902),
                     (.352, 1.00, 1.00),
                     (.406, 1.00, 1.00),
                     (.412, 1.00, 1.00),
                     (.481, 0.00, 0.00),
                     (.484, 0.00, 0.00),
                     (.543, 1.00, 1.00),
                     (.546, 0.773, 0.773),
                     (.994, 0.012, 0.012),
                     (.997, 0.004, 0.004),
                       (1.0, 0.0, 0.0)),
             'blue': ((0.0, 0.00, 0.00),
                     (.001, 1.00, 1.00),
                     (.107, 0.00, 0.00),
                     (.113, 0.498, 0.498),
                     (.173, 0.786, 0.786),
                     (.179, 0.902, 0.902),
                     (.227, 0.102, 0.102),
                     (.233, 0.00, 0.00),
                     (.287, 0.00, 0.00),
                     (.293, 0.00, 0.00),
                     (.346, 0.00, 0.00),
                     (.352, 0.00, 0.00),
                     (.406, 0.00, 0.00),
                     (.412, 0.00, 0.00),
                     (.481, 0.451, 0.451),
                     (.484, 0.451, 0.451),
                     (.543, 1.00, 1.00),
                     (.546, 0.773, 0.773),
                     (.994, 0.012, 0.012),
                     (.997, 0.004, 0.004),
                      (1.0, 0.0, 0.0))}

    IR_cmap = mpl.colors.LinearSegmentedColormap('my_colormap',cdict,2048)
    return(IR_cmap)


# In[ ]:




