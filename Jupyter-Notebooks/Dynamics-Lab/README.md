# My first attempt at teaching students in Python!

## I was granted a wonderful opportunity to redo Dr. Schuenemann's Atmospheric Dynamics IDL lab into Python.
The lab consists of basic dynamics equations based off the inital variable in the netCDF file; geopotential heights. From that value the geostrophic winds and absoulte vorticity could be theoretically calculated.

This part of the class was an addition to lecture and homework. However, folding Python (newly used at MSU Denver) will help them get a more useful programming requisite for graduation. The current most used are R and Java, with most choosing Java, struggling, and learning no real coding when they graduate. And the old way of IDL was attainable in the past, but now has high user cost and may not be the most relevant coding either. So the underlying two goals were:
* Form a different relationship to the functions and the variables, generating they're own functions and plots will hopefully let the students see the equations for the known produced plot
* Bring a tangible coding environment to the students in a relevant manner with Python increasingly benefiting the atmospheric community
### <font fontsize='40'>The students were assigned a lab as part of their final grade to read in raw data and manipulate it to get atmospheric variables for plotting.
## <font>For this dynamics lab, the date chosen for the case study was February 2nd, 2016; Denver's Groundhog Day Storm. </font>

### <font>The setup for Denver's storm was a classic Low pressure center around Southeast Colorado bringing upslope flow.</font>
### Surface Analysis
http://www2.mmm.ucar.edu/imagearchive1/SatSfcComposite/20160202/sat_sfc_map_2016020207.gif

<p align="center">
  <img src="http://www2.mmm.ucar.edu/imagearchive1/SatSfcComposite/20160202/sat_sfc_map_2016020207.gif" width="420" title="Sfc Analysis"><img src="http://www2.mmm.ucar.edu/imagearchive1/SatSfcComposite/20160202/sat_sfc_map_2016020213.gif" width="420" title="Sfc Analysis">
</p>

### HRRR Predicted Radar
http://www.bouldercast.com/wp-content/uploads/2016/02/18Z-20160201_hrrrCGPsf_prec_radar.gif

<p align="center">
  <img src="http://www.bouldercast.com/wp-content/uploads/2016/02/18Z-20160201_hrrrCGPsf_prec_radar.gif" width="600" title="Sfc Analysis">
</p>

### Snow Fall Totals
http://mediaassets.scrippsnationalnews.com/photo/2016/02/01/GroundhogDayBlizzard-SnowfallTotals_1454342782744_31151996_ver1.0_900_675.jpg

<p align="center">
  <img src="http://mediaassets.scrippsnationalnews.com/photo/2016/02/01/GroundhogDayBlizzard-SnowfallTotals_1454342782744_31151996_ver1.0_900_675.jpg" width="600" title="Snowfall Totals">
</p>





# Variables Used:
* Geopotential Heights
* Latitude/Longitudes

# They made functions for:
* ## Coriolis Parameter
![](https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/Dynamics%20Lab/Equations/github_Dynamics_CorFac_eqns.png)
```Python
  # We will need to pass the latitude from the Lat array to get the value!

  def CorFac(mylat):
    cof = 2*7.292E-5*np.sin(Lat[mylat]*np.pi/180)
    return float(cof)
```

* ## Pressure Gradient Force
![](https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/Dynamics%20Lab/Equations/Resized_github_Dynamics_PGF_eqns.png)
```Python
    height_Denver = height[mytime][5][Denlat][Denlon]
    print("Denver's height:",height_Denver,"m")
    ​
    # The reason why the northern height is Denlat-1 instead of +1 is because how the lat data was read in?
    height_north = height[mytime][5][Denlat-1][Denlon]
    print("Height north:",height_north,"m")
    ​
    height_south = height[mytime][5][Denlat+1][Denlon]
    print("Height south:",height_south,"m")
    ​
    height_east = height[mytime][5][Denlat][Denlon+1]
    print("Height east:",height_east,"m")
    ​
    height_west = height[mytime][5][Denlat][Denlon-1]
    print("Height west:",height_west,"m")
    ​
    Denver's height: 5362.0 m
    Height north: 5390.0 m
    Height south: 5362.0 m
    Height east: 5339.0 m
    Height west: 5392.0 m
```

```python
    def PGF(time,level,height_east,height_west,height_north,height_south,dx,dy):
      pgfx = -9.8*((height_east-height_west)/(dx*2))
      pgfy = -9.8*((height_north-height_south)/(dy*2))
      pgf = np.sqrt((pgfx**2)+(pgfy**2))
      return float(pgfx), float(pgfy), float(pgf)
```
* ## Geostrophic Winds

![](https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/Dynamics%20Lab/Equations/Resized_github_Dynamics_GeoWind_eqns.png)
![f1](http://chart.apis.google.com/chart?cht=tx&chl=m=\frac{m_0}{\sqrt{1-{\frac{v^2}{c^2}}}})


![f1](http://chart.apis.google.com/chart?cht=tx&chl=\vec{V{_g}}=-\frac{1}{f}(\frac{dQ_{1}}{dy}\hat{i}-\frac{dQ_{2}}{dx}\hat{j}))

![](https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/Dynamics%20Lab/Equations/Resized_github_Dynamics_uGeoWind_eqns.png)
```Python
  def uGeoWind(level,time,lat,lon,dy):
    ug = (-9.8/CorFac(lat))*\
          ((height[time][level][lat-1][lon]-height[time][level][lat+1][lon])/(dy*2))   

    return ug

```
![](https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/Dynamics%20Lab/Equations/Resized_github_Dynamics_vGeoWind_eqns.png)

```Python
  def vGeoWind(level,time,lat,lon,dx):
     vg = (9.8/CorFac(lat))*\
            ((height[time][level][lat][lon+1]-height[time][level][lat][lon-1])/(dx*2))   

     return vg

```
![](https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/Dynamics%20Lab/Equations/Resized_github_Dynamics_GeoWind_Magnitude_eqns.png)

```Python
  def GeoWind(level,time,lat,lon,dx,dy):

    ug = uGeoWind(level,time,lat,lon,dy)
    vg = vGeoWind(level,time,lat,lon,dx)
    
    return np.sqrt((ug**2)+(vg**2))

```
* ## Absolute Vorticity - based off Geostrophic Winds
![](https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/Dynamics%20Lab/Equations/Resized_github_Dynamics_Vort_eqns.png)
```IPython
  def Vort(level,time,lat,lon,dx,dy):    
      vort = ((vGeoWind(level,time,lat,lon+1,dx)-vGeoWind(level,time,lat,lon-1,dx))/(2*dx))-\
                              ((uGeoWind(level,time,lat-1,lon,dy)-uGeoWind(level,time,lat+1,lon,dy))/(2*dy))
      return vort

```


# Plots Generated:
## Blank CONUS Map and w/ Denver Highlighted
### Set the map's projections and boundaries
```python
  # Set pur lat/lon box for plotting 
  #extent = [-125,-70,20,50]
  extent = [-125,-70,25,48]

  # Set projection of data
  datacrs = ccrs.PlateCarree()

  # Set projection of map
  plotcrs = ccrs.LambertConformal(central_latitude=[20, 60], central_longitude=-100)

  # Add Map Features
  country_borders = cfeature.NaturalEarthFeature(category='cultural',
      name='admin_0_countries',scale='50m', facecolor='none')

  state_boundaries = cfeature.NaturalEarthFeature(category='cultural',
          name='admin_1_states_provinces_lakes', scale='50m', facecolor='none')
```
### Make a new figure; a drawing of the CONUS map
```python
  # Draw a new figure
  fig=plt.figure(figsize=(20,20))
  ax = fig.add_subplot(1, 1, 1, projection=plotcrs) 
  ax.add_feature(cfeature.LAND)
  ax.add_feature(cfeature.OCEAN)

  # draw coastlines, state and country boundaries, edge of map.
  ax.coastlines('10m', color='black',alpha=0.5)
  ax.add_feature(state_boundaries, edgecolor='black',alpha=0.5)
  ax.add_feature(cfeature.LAKES,alpha=0.5)

  # plot only the CONUS from the lat/lon extent
  ax.set_extent(extent, datacrs)

  plt.show()
```
![](https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/Dynamics%20Lab/Output%20Maps/Resized_blank_CONUS.png)

### Do it again, but put a star where Denver is and label it
```python
  # Draw a new figure
  fig=plt.figure(figsize=(20,20))
  ax = fig.add_subplot(1, 1, 1, projection=plotcrs) 
  ax.add_feature(cfeature.LAND)
  ax.add_feature(cfeature.OCEAN)
      # draw coastlines, state and country boundaries, edge of map.
  ax.coastlines('10m', color='black',alpha=0.5)
  ax.add_feature(state_boundaries, edgecolor='black',alpha=0.5)
  ax.add_feature(cfeature.LAKES,alpha=0.5)
  ax.set_extent(extent, datacrs)

  # Labeling Denver with a star
  ax.scatter(-104.9903, 39.7392, marker='*', c="blue",transform=datacrs,s=205)
  transform = datacrs._as_mpl_transform(ax)
  ax.annotate('Denver', xy=(-106, 38.8), xycoords=transform)

  plt.show()
 
```
![](https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/Dynamics%20Lab/Output%20Maps/Resized_blank_CONUS_Denver.png)

## 500mb Geopotential Heights

![](https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/Dynamics%20Lab/Output%20Maps/Resized_500mb_Height_Contour_2016_02_02_1200Z.png)

## 500mb Geostrophic Winds with Heights

![](https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/Dynamics%20Lab/Output%20Maps/Resized_500mb_Winds_2016_02_02_1200Z.png)

## 500mb Vorticity for 3 times

![](https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/Dynamics%20Lab/Output%20Maps/Resized_500mb_Vort_2016_02_02_0600Z.png)

![](https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/Dynamics%20Lab/Output%20Maps/Resized_500mb_Vort_2016_02_02_1200Z.png)

![](https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/Dynamics%20Lab/Output%20Maps/Resized_500mb_Vort_2016_02_02_1800Z.png)

And as a nice addition they could have the option of writing a new neCDF file to avoid having to run the calculations everytime they opened their notebook.
Create the new netCDF file:
```python
  dataset = Dataset('/home/username/Desktop/Groundhogs_Day_Storm_Calcs.nc','w')
```
Create variables to fill in our new .nc file
```python
  level = dataset.createDimension('level', len(Level))
  lat = dataset.createDimension('lat', len(Lat))
  lon = dataset.createDimension('lon', len(Lon))
  date = dataset.createDimension('date', len(Time))
  
  levels = dataset.createVariable('level', np.int32, ('level',))
  latitudes = dataset.createVariable('latitude', np.float32,('lat',))
  longitudes = dataset.createVariable('longitude', np.float32,('lon',))
  dates = dataset.createVariable('dates', str, ('date',))

  # Create the 2-d arrays for Winds and Vorticities for 3 times each
  winds_130_500 = dataset.createVariable('winds_130_500', np.float32,('lat','lon',))
  uwinds_130_500 = dataset.createVariable('uwinds_130_500', np.float32,('lat','lon',))
  vwinds_130_500 = dataset.createVariable('vwinds_130_500', np.float32,('lat','lon',))

  vorts_130_500 = dataset.createVariable('vorticity_130_500', np.float32,('lat','lon',))

  # Create the 3-d arrays for Winds and Vorticities for day 130
  #winds_130 = dataset.createVariable('winds_130', np.float32,('lat','lon','level'))
  #vorts_130 = dataset.createVariable('vorticity_130', np.float32,('lat','lon','level'))

  # Create the 4-d array for geopotential heights
  hgts = dataset.createVariable('hgt', np.float32,('date','level','lat','lon'))

```
Fill the newly created variables with our data
```python
  # Each variable entry will be the data value entry from our arrays:

  latitudes[:] = Lat
  longitudes[:] = Lon
  levels[:] = Level
  hgts[:] = height

  # 2-d arrays at days 129, 130, and 131 and 500mb only
  #winds_129_500[:] = WindsFull_129_500mb.values
  winds_130_500[:] = WindsFull_130_500mb
  uwinds_130_500[:] = uWindsFull_130_500mb
  vwinds_130_500[:] = vWindsFull_130_500mb
  #winds_131_500[:] = WindsFull_131_500mb.values
  #vorts_129_500[:] = Vort_129_500mb.values
  vorts_130_500[:] = Vort_130_500mb
  #vorts_131_500[:] = Vort_131_500mb.values

  # 3-d arrays for day 130
  #winds_130[:] = WindsFull_130.values
  #vorts_130[:] = VortFull_130.values
```
Let's check to see if our data stored properly in the new .nc file
```python
  datafile2 = NetCDFFile('/home/username/Desktop/Groundhogs_Day_Storm_Calcs.nc')
```
List the variables
```python
  list(datafile2.variables.keys())
 
 # output
  ['level',
   'latitude',
   'longitude',
   'dates',
   'winds_130_500',
   'uwinds_130_500',
   'vwinds_130_500',
   'vorticity_130_500',
   'hgt']
```
Vorticity data
```python
  Vort_130_500mb = datafile2.variables['vorticity_130_500'][:]
```
And finally plot it agian to see if we're all good
```python
  # Draw a new figure
  fig=plt.figure(figsize=(20,20))
  ax = fig.add_subplot(1, 1, 1, projection=plotcrs) 
  #ax.add_feature(cfeature.LAND)
  #ax.add_feature(cfeature.OCEAN)

  # draw coastlines, state and country boundaries, edge of map.
  ax.coastlines('10m', color='black',alpha=0.5)
  ax.add_feature(state_boundaries, edgecolor='black',alpha=0.5)
  ax.add_feature(cfeature.LAKES,alpha=0.5)
  ax.set_extent(extent, datacrs)

  # We can set the limits for the contours by taking the max and min
  vort_levels = np.arange(float(Vort_130_500mb[12:32,88:122].min()),
              float(Vort_130_500mb[12:32,88:122].max()),0.00001)

  # Gaussian Filter to smooth the data and make it a little neater 
  vort_smooth = ndimage.gaussian_filter(Vort_130_500mb[12:32,88:122], sigma=1, order=0)


  vort_contourfill = ax.contourf(Lon[88:122], Lat[12:32],Vort_130_500mb[12:32,88:122],100,
              transform=datacrs,cmap=vort_cmap)

  # Let's set the colorbar and position
  cb = plt.colorbar(vort_contourfill,alpha=0.4,orientation="vertical", pad=0.02,shrink=0.45)
  cb.ax.tick_params(labelsize=14)
  cb.ax.set_title('$s^{-1}$', fontsize=15,horizontalalignment='center',y=1.01,x=1)

  hgt_contour = ax.contour(Lon[88:122], Lat[12:32], hgt130_500mb,hgt130_500mb_levels,
              colors='k',transform=datacrs,alpha=0.7)# Labeling the contours
  #ax.clabel(hgt_contour, inline=True, fmt='%1i',fontsize=20,colors='k')

  # Labeling Denver with a star
  ax.scatter(-104.9903, 39.7392, marker='*', c="k",transform=datacrs,s=205)
  transform = datacrs._as_mpl_transform(ax)
  ax.annotate('Denver', xy=(-106, 38.8), xycoords=transform,color="k")

  # Label plot title
  plt.title('500mb Absolute Vorticity (shaded) and Heights',fontsize=30)

  text_time = ax.text(.995, 0.01, 
          str(dates[130])[:-3]+" Z",
          horizontalalignment='right', transform=ax.transAxes,
          color='white', fontsize=20, weight='bold')

  outline_effect = [patheffects.withStroke(linewidth=5, foreground='black')]
  text_time.set_path_effects(outline_effect)

  # make everything on the plot line up nicely
  #plt.tight_layout()

  # Save the figure
  file_date = str(dates[130])[:-3].replace(" ","_")
  file_date = file_date.replace("-","_")
  file_date = file_date.replace(":","")
  file_date = file_date+"Z"
  #plt.savefig("/home/username/Desktop/500mb_Vort_"+file_date+".png",bbox_inches='tight')

  plt.show()
```
# There are aspects that could be changed:
* <strike>Break the Master lab into Intro, Data, and Plotting notebooks?</strike>
* <strike>Impliment the writing of new netCDF file</strike>
* Set metadata for the variables of new netCDF file
* <strike>Missing data on plots could be resolved with assigning color ranges better</strike>
* <strike>Switch over from Python 2 to 3</strike>
* <strike>Switch over from Basemap to CartoPy</strike>
* Have Vorticity colorbar values in 10^-5 ranges
* Less hand-holding on my part
* Make lab manual/handout <i> <b>- In Progress</b> </i>
* More time for the students to get used to Python/Jupyter
* Work closer with the students to give a better commented code/final write-up
