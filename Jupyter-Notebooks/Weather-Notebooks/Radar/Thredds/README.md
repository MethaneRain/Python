# Attempting to Plot NEXRAD Composite Reflectivity from the Thredds Server

##

I'm having one major problem; getting he data to plot in the correct projection


## Pull the data

```python
from siphon.catalog import TDSCatalog
top_cat = TDSCatalog('http://thredds.ucar.edu/thredds/catalog.xml')
ref = top_cat.catalog_refs['Radar Data']

new_cat = ref.follow()
model = new_cat.catalog_refs[4]
gfs_cat = model.follow()

ds = gfs_cat.datasets[0]
subset = ds.subset()
query_data = subset.query()
    #query_data.lonlat_box(west=-130, east=-50, south=10, north=60)
from datetime import datetime, timedelta
now = datetime.utcnow()
now = datetime(2019,4,12,hour,0*5)
print(now)
    # Allow for NetCDF files
query_data.accept('netcdf4')
query_data.time(now)
query_data.variables('Base_reflectivity_surface_layer')

    # Finally attempt to access the data
data = subset.get_data(query_data)

    #rd = Dataset(i)
time = data.variables['time']
dtime = num2date(time[:],time.units)


Time = dtime[0].strftime('%Y-%m-%d %H:%MZ')
print(Time)
reflec_data = data.variables['Base_reflectivity_surface_layer']
reflec = data.variables['Base_reflectivity_surface_layer'][:]

```
## Find the projection variable

```python
list(data.variables)

>>> ['Base_reflectivity_surface_layer',
 'reftime',
 'time',
 'y',
 'x',
 'LambertConformal_Projection']
```

## Check the projection of the data

```python
data.variables['LambertConformal_Projection']

>>> <class 'netCDF4._netCDF4.Variable'>
int32 LambertConformal_Projection()
    grid_mapping_name: lambert_conformal_conic
    latitude_of_projection_origin: 40.0
    longitude_of_central_meridian: 260.0
    standard_parallel: 40.0
    earth_radius: 6371200.0
    _CoordinateTransformType: Projection
    _CoordinateAxisTypes: GeoX GeoY
unlimited dimensions:
current shape = ()
filling on, default _FillValue of -2147483647 used
```
## Grab some lat/lon info

```python
cent_lon = data.variables['LambertConformal_Projection'].longitude_of_central_meridian
cent_lat = data.variables['LambertConformal_Projection'].latitude_of_projection_origin
```

## Attempt at plotting:

```python
fig = plt.figure(figsize=(11,8))

geocrs = ccrs.Geostationary(central_longitude=cent_lon)

# Add state and country boundaries to plot
states_boundaries = cfeature.NaturalEarthFeature(category='cultural',
        name='admin_1_states_provinces_lakes',scale='50m', facecolor='none')

country_borders = cfeature.NaturalEarthFeature(category='cultural',
        name='admin_0_countries',scale='50m', facecolor='none')


plot_proj = ccrs.LambertConformal()

plotcrs = ccrs.LambertConformal(central_latitude=cent_lat, central_longitude=cent_lon)

ax = plt.subplot(111,projection = plotcrs)



ax.add_feature(states_boundaries,edgecolor='b',linewidth=1)
ax.add_feature(country_borders,edgecolor='b',linewidth=1)
#ax.set_extent([-130,-70,20,50])

ax.imshow(reflec[0,:,:],origin='lower',cmap='nipy_spectral',transform=plot_proj,interpolation='nearest'),
          #extent=(500,1000,500,1000))
text_time = ax.text(.995, 0.01,
        Time,
        horizontalalignment='right', transform=ax.transAxes,
        color='white', fontsize=15, weight='bold')

text_time2 = ax.text(0.005, 0.01,
            "Radar",
            horizontalalignment='left', transform=ax.transAxes,
            color='white', fontsize=15, weight='bold')

outline_effect = [patheffects.withStroke(linewidth=5, foreground='black')]
text_time.set_path_effects(outline_effect)
text_time2.set_path_effects(outline_effect)


plt.show()
plt.savefig("Radar_+Time[0:10].replace("-","_")+"_"+Time[-6:].replace(":","")+".png",bbox_inches="tight")
plt.close(fig)
```

<img src="https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/Radar/Thredds/Radar_2019_04_12_0000Z.png">


# Fixed!

I was able to plot the Radar successfully by using the `pcolormesh` call instead of the `contourf` or the `imshow` calls. I still don't know why this worked but the others didn't. I have asked this on Stack Overflow to see if someone more familiar with the projections could give me some insight.

```python
ax.pcolormesh(lon[:], lat[:], reflec[0,:,:],cmap='nipy_spectral',transform=ccrs.PlateCarree())
```

<img src='https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/Radar/Thredds/Radar_CONUS_2019_04_12_0000Z.png'>


# Accessing the Level III Radar
## * Base Reflectivity and Velocity
<img src="https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/Radar/Thredds/Denver_Radar_Reflectivity_thredds_2019_05_27_1935Z.png">,<img src="https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/Radar/Thredds/Denver_Radar_Velocity_thredds_2019_05_27_1935Z.png">
