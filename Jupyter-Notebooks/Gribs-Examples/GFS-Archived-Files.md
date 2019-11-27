# Access GFS data from gribs file types

<img src="https://www.earthsystemcog.org/site_media/logos/gfs4c.png">

## This can be very helpful as a lot of model data and other weather data are in this file type
---
I had to create a separate ```env``` for working with ```pygrib```, my libraries weren't playing nicely otherwise.

In the terminal:

$ conda create -n test-pygrib python=3.7

You must install all your Python libraries again since this is a blank slate environment

$ conda activate test-pygrib
---
GFS Analysis and Forecast:
* Some days are missing...

* Roughly 10 days behind current date

* https://www.ncdc.noaa.gov/data-access/model-data/model-datasets/global-forcast-system-gfs

---
```Python
grbs
```
will be the new instance of the data and file and
```Python
grb```
will be the lines of the file read in

```python
grbs = pygrib.open(_grib_file_)
grb = grbs.read()
```
There are so many variables, we can just print out a couple to see the data in raw form

```python
grb[0:10]
```

```python
>>>
[1:Cloud mixing ratio:kg kg**-1 (instant):regular_ll:hybrid:level 1:fcst time 0 hrs:from 201911150000,
 2:Ice water mixing ratio:kg kg**-1 (instant):regular_ll:hybrid:level 1:fcst time 0 hrs:from 201911150000,
 3:Rain mixing ratio:kg kg**-1 (instant):regular_ll:hybrid:level 1:fcst time 0 hrs:from 201911150000,
 4:Snow mixing ratio:kg kg**-1 (instant):regular_ll:hybrid:level 1:fcst time 0 hrs:from 201911150000,
 5:Graupel (snow pellets):kg kg**-1 (instant):regular_ll:hybrid:level 1:fcst time 0 hrs:from 201911150000,
 6:Maximum/Composite radar reflectivity:dB (instant):regular_ll:atmosphere:level 0 -:fcst time 0 hrs:from 201911150000,
 7:Visibility:m (instant):regular_ll:surface:level 0:fcst time 0 hrs:from 201911150000,
 8:U component of wind:m s**-1 (instant):regular_ll:unknown:level 0:fcst time 0 hrs:from 201911150000,
 9:V component of wind:m s**-1 (instant):regular_ll:unknown:level 0:fcst time 0 hrs:from 201911150000,
 10:Ventilation Rate:m**2 s**-1 (instant):regular_ll:unknown:level 0:fcst time 0 hrs:from 201911150000
>>>
```



---

There are several ways to access data, lets take a look a some:
---

#### Simplest Method


In your notebook:
```python
import pygrib
grib = "gfsanl_3_20190129_1200_000.grb2"# Set the file name of your input GRIB file
grbs = pygrib.open(grib)
```

```python
grbs.read()

>>> 1:Visibility:m (instant):regular_ll:surface:level 0:fcst time 0 hrs:from 201901291200,
 2:U component of wind:m s**-1 (instant):regular_ll:unknown:level 0:fcst time 0 hrs:from 201901291200,
 3:V component of wind:m s**-1 (instant):regular_ll:unknown:level 0:fcst time 0 hrs:from 201901291200,
 4:Ventilation Rate:m**2 s**-1 (instant):regular_ll:unknown:level 0:fcst time 0 hrs:from 201901291200,
 5:Wind speed (gust):m s**-1 (instant):regular_ll:surface:level 0:fcst time 0 hrs:from 201901291200,
 6:Geopotential Height:gpm (instant):regular_ll:isobaricInhPa:level 100 Pa:fcst time 0 hrs:from 201901291200,
 7:Temperature:K (instant):regular_ll:isobaricInhPa:level 100 Pa:fcst time 0 hrs:from 201901291200,
 8:Relative humidity:% (instant):regular_ll:isobaricInhPa:level 100 Pa:fcst time 0 hrs:from 201901291200,
 9:U component of wind:m s**-1 (instant):regular_ll:isobaricInhPa:level 100 Pa:fcst time 0 hrs:from 201901291200,
 10:V component of wind:m s**-1 (instant):regular_ll:isobaricInhPa:level 100 Pa:fcst time 0 hrs:from 201901291200,
 11:Ozone mixing ratio:kg kg**-1 (instant):regular_ll:isobaricInhPa:level 100 Pa:fcst time 0 hrs:from 201901291200,
 12:Geopotential Height:gpm (instant):regular_ll:isobaricInhPa:level 200 Pa:fcst time 0 hrs:from 201901291200,
 13:Temperature:K (instant):regular_ll:isobaricInhPa:level 200 Pa:fcst time 0 hrs:from 201901291200,
 14:Relative humidity:% (instant):regular_ll:isobaricInhPa:level 200 Pa:fcst time 0 hrs:from 201901291200,
 15:U component of wind:m s**-1 (instant):regular_ll:isobaricInhPa:level 200 Pa:fcst time 0 hrs:from 201901291200,
 16:V component of wind:m s**-1 (instant):regular_ll:isobaricInhPa:level 200 Pa:fcst time 0 hrs:from 201901291200,
 17:Ozone mixing ratio:kg kg**-1 (instant):regular_ll:isobaricInhPa:level 200 Pa:fcst time 0 hrs:from 201901291200,
 18:Geopotential Height:gpm (instant):regular_ll:isobaricInhPa:level 300 Pa:fcst time 0 hrs:from 201901291200,
 19:Temperature:K (instant):regular_ll:isobaricInhPa:level 300 Pa:fcst time 0 hrs:from 201901291200,
 .
 .
 .
 345:Vertical speed shear:s**-1 (instant):regular_ll:potentialVorticity:level 2e-06 K m2 kg-1 s-1:fcst time 0 hrs:from 201901291200,
 346:U component of wind:m s**-1 (instant):regular_ll:potentialVorticity:level 2.147485648 K m2 kg-1 s-1:fcst time 0 hrs:from 201901291200,
 347:V component of wind:m s**-1 (instant):regular_ll:potentialVorticity:level 2.147485648 K m2 kg-1 s-1:fcst time 0 hrs:from 201901291200,
 348:Temperature:K (instant):regular_ll:potentialVorticity:level 2.147485648 K m2 kg-1 s-1:fcst time 0 hrs:from 201901291200,
 349:Geopotential Height:gpm (instant):regular_ll:potentialVorticity:level 2.147485648 K m2 kg-1 s-1:fcst time 0 hrs:from 201901291200,
 350:Pressure:Pa (instant):regular_ll:potentialVorticity:level 2.147485648 K m2 kg-1 s-1:fcst time 0 hrs:from 201901291200,
 351:Vertical speed shear:s**-1 (instant):regular_ll:potentialVorticity:level 2.147485648 K m2 kg-1 s-1:fcst time 0 hrs:from 201901291200,
 352:Pressure reduced to MSL:Pa (instant):regular_ll:meanSea:level 0:fcst time 0 hrs:from 201901291200,
 353:5-wave geopotential height:gpm (instant):regular_ll:isobaricInhPa:level 50000 Pa:fcst time 0 hrs:from 201901291200,
 354:Land-sea coverage (nearest neighbor) [land=1,sea=0]:~ (instant):regular_ll:surface:level 0:fcst time 0 hrs:from 201901291200]
```

If you want to access a speific entry in the data, you need to remember Python is zeroth index language. So if we wanted the 500mb Geopotential Heights:

```python
142:Geopotential Height:gpm (instant):regular_ll:isobaricInhPa:level 50000 Pa:fcst time 0 hrs:from 201901291200
```

It appears that the entry is #142, however this is the entry in the gribs data file, not the Python readout, so we would want the ```141st``` entry:

```python
grib = "gfsanl_3_20190129_1200_000.grb2"
grbs = pygrib.open(grib)
grb_500 = grbs.select()[141]
print(grb_500)

>>> 142:Geopotential Height:gpm (instant):regular_ll:isobaricInhPa:level 50000 Pa:fcst time 0 hrs:from 201901291200
```
Check!

We can also look at the keys for this data:

```python
list(grb_500.keys())

>>> ['globalDomain',
 'GRIBEditionNumber',
 'tablesVersionLatest',
 'grib2divider',
 'is_efas',
 'angularPrecision',
 'missingValue',
 'ieeeFloats',
 'isHindcast',
 'section0Length',
 'identifier',
 'discipline',
 'editionNumber',
 'totalLength',
 'sectionNumber',
 'section1Length',
 'numberOfSection',
 'centre',
 'centreDescription',
 'subCentre',
 'tablesVersion',
 'masterDir',
 'localTablesVersion',
 'significanceOfReferenceTime',
 'year',
 'month',
 'day',
 'hour',
 'minute',
 'second',
 'dataDate',
 'julianDay',
 'dataTime',
 'productionStatusOfProcessedData',
 'typeOfProcessedData',
 'md5Section1',
 'selectStepTemplateInterval',
 'selectStepTemplateInstant',
 'stepType',
 'setCalendarId',
 'deleteCalendarId',
 'is_uerra',
 'sectionNumber',
 'grib2LocalSectionPresent',
 'deleteLocalDefinition',
 'sectionNumber',
 'gridDescriptionSectionPresent',
 'section3Length',
 'numberOfSection',
 'sourceOfGridDefinition',
 'numberOfDataPoints',
 'numberOfOctectsForNumberOfPoints',
 'interpretationOfNumberOfPoints',
 'PLPresent',
 'gridDefinitionTemplateNumber',
 'gridDefinitionDescription',
 'shapeOfTheEarth',
 'scaleFactorOfRadiusOfSphericalEarth',
 'scaledValueOfRadiusOfSphericalEarth',
 'scaleFactorOfEarthMajorAxis',
 'scaledValueOfEarthMajorAxis',
 'scaleFactorOfEarthMinorAxis',
 'scaledValueOfEarthMinorAxis',
 'radius',
 'Ni',
 'Nj',
 'basicAngleOfTheInitialProductionDomain',
 'mBasicAngle',
 'angleMultiplier',
 'mAngleMultiplier',
 'subdivisionsOfBasicAngle',
 'angleDivisor',
 'latitudeOfFirstGridPoint',
 'longitudeOfFirstGridPoint',
 'resolutionAndComponentFlags',
 'resolutionAndComponentFlags1',
 'resolutionAndComponentFlags2',
 'iDirectionIncrementGiven',
 'jDirectionIncrementGiven',
 'uvRelativeToGrid',
 'resolutionAndComponentFlags6',
 'resolutionAndComponentFlags7',
 'resolutionAndComponentFlags8',
 'ijDirectionIncrementGiven',
 'latitudeOfLastGridPoint',
 'longitudeOfLastGridPoint',
 'iDirectionIncrement',
 'jDirectionIncrement',
 'scanningMode',
 'iScansNegatively',
 'jScansPositively',
 'jPointsAreConsecutive',
 'alternativeRowScanning',
 'iScansPositively',
 'scanningMode5',
 'scanningMode6',
 'scanningMode7',
 'scanningMode8',
 'g2grid',
 'latitudeOfFirstGridPointInDegrees',
 'longitudeOfFirstGridPointInDegrees',
 'latitudeOfLastGridPointInDegrees',
 'longitudeOfLastGridPointInDegrees',
 'iDirectionIncrementInDegrees',
 'jDirectionIncrementInDegrees',
 'latLonValues',
 'latitudes',
 'longitudes',
 'distinctLatitudes',
 'distinctLongitudes',
 'gridType',
 'md5Section3',
 'sectionNumber',
 'section4Length',
 'numberOfSection',
 'NV',
 'neitherPresent',
 'productDefinitionTemplateNumber',
 'genVertHeightCoords',
 'parameterCategory',
 'parameterNumber',
 'parameterUnits',
 'parameterName',
 'typeOfGeneratingProcess',
 'backgroundProcess',
 'generatingProcessIdentifier',
 'hoursAfterDataCutoff',
 'minutesAfterDataCutoff',
 'indicatorOfUnitOfTimeRange',
 'stepUnits',
 'forecastTime',
 'startStep',
 'endStep',
 'stepRange',
 'stepTypeInternal',
 'validityDate',
 'validityTime',
 'typeOfFirstFixedSurface',
 'unitsOfFirstFixedSurface',
 'nameOfFirstFixedSurface',
 'scaleFactorOfFirstFixedSurface',
 'scaledValueOfFirstFixedSurface',
 'typeOfSecondFixedSurface',
 'unitsOfSecondFixedSurface',
 'nameOfSecondFixedSurface',
 'scaleFactorOfSecondFixedSurface',
 'scaledValueOfSecondFixedSurface',
 'pressureUnits',
 'typeOfLevel',
 'level',
 'bottomLevel',
 'topLevel',
 'tempPressureUnits',
 'paramIdECMF',
 'paramId',
 'shortNameECMF',
 'shortName',
 'unitsECMF',
 'units',
 'nameECMF',
 'name',
 'cfNameECMF',
 'cfName',
 'cfVarNameECMF',
 'cfVarName',
 'modelName',
 'ifsParam',
 'PVPresent',
 'deletePV',
 'md5Section4',
 'lengthOfHeaders',
 'md5Headers',
 'sectionNumber',
 'section5Length',
 'numberOfSection',
 'numberOfValues',
 'dataRepresentationTemplateNumber',
 'packingType',
 'referenceValue',
 'referenceValueError',
 'binaryScaleFactor',
 'decimalScaleFactor',
 'optimizeScaleFactor',
 'bitsPerValue',
 'typeOfOriginalFieldValues',
 'groupSplittingMethodUsed',
 'missingValueManagementUsed',
 'primaryMissingValueSubstitute',
 'secondaryMissingValueSubstitute',
 'numberOfGroupsOfDataValues',
 'referenceForGroupWidths',
 'numberOfBitsUsedForTheGroupWidths',
 'referenceForGroupLengths',
 'lengthIncrementForTheGroupLengths',
 'trueLengthOfLastGroup',
 'numberOfBitsForScaledGroupLengths',
 'orderOfSpatialDifferencing',
 'numberOfOctetsExtraDescriptors',
 'md5Section5',
 'sectionNumber',
 'section6Length',
 'numberOfSection',
 'bitMapIndicator',
 'bitmapPresent',
 'missingValuesPresent',
 'md5Section6',
 'sectionNumber',
 'section7Length',
 'numberOfSection',
 'codedValues',
 'values',
 'maximum',
 'minimum',
 'average',
 'numberOfMissing',
 'standardDeviation',
 'skewness',
 'kurtosis',
 'isConstant',
 'changeDecimalPrecision',
 'decimalPrecision',
 'setBitsPerValue',
 'getNumberOfValues',
 'scaleValuesBy',
 'offsetValuesBy',
 'productType',
 'md5Section7',
 'section8Length',
 'analDate',
 'validDate']
```

Now we can declare a variable for the data by calling the ```values``` key:
```python
data_500mb = grb_500.values
```

Let's explore some of the time keys of ```grb_500```:
```python
print(grb_500['dataDate'])
>>> 20190129

print(grb_500['hour'])
>>> 12

print(grb_500['minute'])
>>> 0
print(grb_500['forecastTime'])
>>> 0

print(grb_500['dataTime'])
>>> 1200

file_time = str(grb_500['dataDate'])+"_"+str(grb_500['dataTime'])+"Z"
print(file_time)
>>> '20190129_1200Z'
```

When we go to plot, we're going to need the latitudes and longitudes, which we can pull from the ```keys()``` as well:
```python
lat,lon = grb_500.latlons()
```

Lets pull the 500mb vorticity as well so we can generate our plot:
```python
grb_Vort = grbs.select()[147]
data_Vort = grb_Vort.values

# Create new figure
datacrs = ccrs.PlateCarree()
plotcrs = ccrs.NorthPolarStereo(central_longitude=-100.0)

fig = plt.figure(figsize=(17., 11.))

add_metpy_logo(fig, 30, 940, size='small')
gs = gridspec.GridSpec(2, 1, height_ratios=[1, .02],
        bottom=.02, top=.95, hspace=0.01, wspace=0.01)

ax = plt.subplot(gs[0], projection=plotcrs)
# Add the map and set the extent
#ax = plt.subplot(111, projection=plotcrs)

#Set the lat and lon boundaries
#ax.set_extent(extent, datacrs)
ax.set_extent([-180, 180, 10, 90], ccrs.PlateCarree())

# Add state boundaries to plot
ax.add_feature(states_provinces, edgecolor='blue', linewidth=1)

# Add country borders to plot
ax.add_feature(country_borders, edgecolor='black', linewidth=1)

# Plot Title
plt.title(' ', fontsize=16,loc='left')
vort_levels = np.arange(-.00055,.0007,0.00001)
#data_Vort = np.ma.masked_where(data_Vort < -.00085,data_Vort)
#data_Vort = np.ma.masked_where(data_Vort > .0085,data_Vort)

data_500mb_lev = np.arange(4500,6000,100)

cs = ax.contour(lon, lat, data_500mb,colors='k',
                 transform=datacrs)

cs2 = ax.contourf(lon, lat, data_Vort,vort_levels,
                 transform=datacrs,cmap=vort_cmap)

cbaxes = fig.add_axes(colorbar_axis) # [left, bottom, width, height]

cbar = plt.colorbar(cs2, orientation='horizontal',cax=cbaxes)
ax.set_autoscaley_on(False)

plt.show()
```
![500mb Vorticity](https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/Gribs-Examples/Sample-Maps/vort_gribs_example.png)

---
# We can also grab the variables if we know a little bit about the data

* https://jswhit.github.io/pygrib/docs/pygrib.index-class.html

Say we want the 500mb Geopotential Heights:
```python
grbindx=pygrib.index(grib,'shortName','typeOfLevel','level')
selected_grbs=grbindx.select(shortName='gh',typeOfLevel='isobaricInhPa',level=500)
for grb in selected_grbs:
    print(grb)

>>> 1:Geopotential Height:gpm (instant):regular_ll:isobaricInhPa:level 50000 Pa:fcst time 3 hrs:from 201908111800
```
Sweet!

### * Notice however, we must have some outside knowledge of the shortname. In the actual data it appears it is ```'gpm'```, but the call we need to make is ```'gh'```
