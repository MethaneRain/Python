# A nice repository for little things I've picked up along the way

## * Made my first color bar from scratch (with a little help)
#### Costom Colorbar Function

#### Wonderful piece of code to make a custom color bar thanks to Chris Slocum

source: 
* https://github.com/CSlocumWX/custom_colormap
* https://github.com/CSlocumWX/custom_colormap/blob/master/custom_colormaps.py

<img src="https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/Playground/Images/CSU_colorbar_func-1.png" width="60%">

#### Piecing the colorbar together one color at a time
![Vorticity Colorbar](https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/Playground/Images/vort_colorbar_updated.png)![]()
#### Vorticity levels for plotting
![Vorticity Levels](https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/Playground/Images/vort_levels.png)
#### My Vorticity 
![Vorticity](https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/Playground/Images/Resized_Vort_Heights_500mb_2019_03_10_06Z.png)
#### College of DuPage NEXLAB Vorticity
![](https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/Playground/Images/Resized_GFSUS_500_avort_000.png)
#### Obviously mine is much more skewed towards the white end and the greens are much darker, it still shows a close agreement and that was the goal!
## * MODIS Satellite Images
* https://scitools.org.uk/cartopy/docs/v0.15/examples/wmts_time.html
#### Colorado with Denver at the white star and counties plotted. Good visualization of difference of clouds and snow
![Colorado MODIS Image](https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/Playground/Images/MODIS_2018_05_04.png)

## * Four-Panel Map: Isentropic Analysis w/ Precip
#### Nice way to highlight the isentropic lift


        # Create a figure object, title it, and do the plots.
        fig = plt.figure(figsize = (25,18))
        fig.subplots_adjust(hspace=0.06)
        fig.subplots_adjust(wspace=0.08)

        ##############################################################################################################
                                                # 1st Plot
        ##############################################################################################################

        # Add the map and set the extent
        ax1 = plt.subplot(2,2,4, projection=plotcrs)

        # Add state boundaries to plot
        ax1.add_feature(states_provinces, edgecolor='k', linewidth=1)

        # Add country borders to plot
        ax1.add_feature(country_borders, edgecolor='black', linewidth=1)

            #Set the lat and lon boundaries
        ax1.set_extent(extent, datacrs)

        cs = ax1.contourf(lon,lat,dew,40, cmap="jet",transform=datacrs)


        ##############################################################################################################
                                                # 2nd Plot
        ##############################################################################################################

        # Add the map and set the extent
        ax2 = plt.subplot(2,2,1, projection=plotcrs)

        # Add state boundaries to plot
        ax2.add_feature(states_provinces, edgecolor='k', linewidth=1)

        # Add country borders to plot
        ax2.add_feature(country_borders, edgecolor='black', linewidth=1)

        cntr = ax2.contour(lon, lat, isen_press, transform=datacrs,
                         cmap='rainbow',levels=levels,linewidths=2) 

        ax2.set_extent(extent, datacrs)


        ##############################################################################################################
                                                # 3rd Plot
        ##############################################################################################################
        # Add the map and set the extent
        ax3 = plt.subplot(2,2,2, projection=plotcrs)

        # Add state boundaries to plot
        ax3.add_feature(states_provinces, edgecolor='k', linewidth=1)

        # Add country borders to plot
        ax3.add_feature(country_borders, edgecolor='black', linewidth=1)


        cntr2 = ax3.contourf(lon, lat, isen_mixing, transform=datacrs,
                    levels=mixing_levels, cmap='YlGn')

        ax3.set_extent(extent, datacrs)


        ##############################################################################################################
                                                # 4th Plot
        ##############################################################################################################
        # Add the map and set the extent
        ax4 = plt.subplot(2,2,3, projection=plotcrs)

        # Add state boundaries to plot
        ax4.add_feature(states_provinces, edgecolor='k', linewidth=1)

        # Add country borders to plot
        ax4.add_feature(country_borders, edgecolor='black', linewidth=1)

        cntr = ax4.contour(lon, lat, isen_press, transform=ccrs.PlateCarree(), colors='black', levels=levels,linewidths=2.0)

        ax4.set_extent(extent, datacrs)


![Isentropic Analysis](https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/Playground/Images/4_Panel_Isentropic2019_02_16_00Z.png)

## * Organizing files populated in list from for-loop based off numerical values
#### I noticed early on when I used glob to populate an empty list for file names based off time stamps, the list was unorganized. This was a bit of an annoyance since I usually wanted them choronologically ordered.

![unorganized](https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/Playground/Images/Python_list_unorganized.png)

#### Then I was able to find this little handy list comprehension code that organized it for me!

![organized](https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/Playground/Images/Python_list_organized.png)

## * Jupyter Cell Code Toggle 
#### I was teaching students with Jupyter notebooks and we were learning how to plot and create our own functions. I wanted to show my code output but not show the actual code so they could learn to figure it out themselves. I came across this wonderful little function

#### The Code:
![Cell Toggle Code](https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/Playground/Images/Cell_Toggle.png)

#### Cell Example:
![Code Example](https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/Playground/Images/Cell_Toggle_Example.png)

#### Video
![Video](https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/Playground/Images/Code_Toggle.gif)

## * Resize Images based off orignal dimensions
#### When needing to resize images, say for GitHub pages, I was able to accomplish this task easily

    from PIL import Image
    basewidth = "size for base of resized image"
    img = Image.open('original_image.png')
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), Image.ANTIALIAS)
    img.save('Resized_original_image.png') 


## * Plot and Subplot
####

<img src='https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/Playground/Images/Plot_zoom.png' width='60%'><img src='https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/Playground/Images/Plot_zoom_2.png' width='60%'>

## * Converting Datetime to Julian Day and vice versa
#### Sometimes I need to be able to quickly figure out what the date is for a given Julian day number, like in the file name for GOES satellite data. Sometimes I need to figure out the Julian day for a given date. These handy little functions help resolve that easily.
```python
import calendar

def JulianDate_to_MMDDYYY(y,jd):
    month = 1
    day = 0
    while jd - calendar.monthrange(y,month)[1] > 0 and month <= 12:
        jd = jd - calendar.monthrange(y,month)[1]
        month = month + 1
    print(month,jd,y)
    
JulianDate_to_MMDDYYY(int(YYYY),int(DD))
```

and 

```python 
from datetime import date

# Start of year for reference
d0 = date(int(YYYY), 1, 1)

# Set the date you want to convert
d1 = date(int(YYYY), int(MM), int(DD))

# 
delta = d1 - d0
Day = delta.days+1
print("Julian Day Number:",Day)
```

## * Listing all the attributes from an object
```python
dir(_object_) # _object_ is the object you want to look at the attributes for

>>> 
```
