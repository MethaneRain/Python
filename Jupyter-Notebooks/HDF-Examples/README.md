# HDF Files

## Working with Reprojected .tif File

### Open the reprojected <i>.tif</i> file
```python
ds = gdal.Open('HDF5_LSASAF_MSG_FAPAR_MSG-Disk_201811010000_rep.tif')
```
### Pull the metadata
```python
Meta = ds.GetMetadata()
```

### Check out the variables in the metadata 
```python
list(Meta)

>>> ['ARCHIVE_FACILITY',
 'AREA_OR_POINT',
 'ASSOCIATED_QUALITY_INFORMATION',
 'CENTRE',
 'CFAC',
 'CLOUD_COVERAGE',
 'COFF',
 'COMPRESSION',
 'DISPOSITION_FLAG',
 'END_ORBIT_NUMBER',
 'FIELD_TYPE',
 'FIRST_LAT',
 'FIRST_LON',
 'FORECAST_STEP',
 'GRANULE_TYPE',
 'IMAGE_ACQUISITION_TIME',
 'INSTRUMENT_ID',
 'INSTRUMENT_MODE',
 'LFAC',
 'LOFF',
 'MEAN_SSLAT',
 'MEAN_SSLON',
 'NB_PARAMETERS',
 'NC',
 'NL',
 'NOMINAL_LAT',
 'NOMINAL_LONG',
 'NOMINAL_PRODUCT_TIME',
 'ORBIT_TYPE',
 'OVERALL_QUALITY_FLAG',
 'PARENT_PRODUCT_NAME',
 'PIXEL_SIZE',
 'PLANNED_CHAN_PROCESSING',
 'PROCESSING_LEVEL',
 'PROCESSING_MODE',
 'PRODUCT',
 'PRODUCT_ACTUAL_SIZE',
 'PRODUCT_ALGORITHM_VERSION',
 'PRODUCT_TYPE',
 'PROJECTION_NAME',
 'REGION_NAME',
 'SAF',
 'SATELLITE',
 'SENSING_END_TIME',
 'SENSING_START_TIME',
 'SPECTRAL_CHANNEL_ID',
 'START_ORBIT_NUMBER',
 'STATISTIC_TYPE',
 'SUB_SATELLITE_POINT_END_LAT',
 'SUB_SATELLITE_POINT_END_LON',
 'SUB_SATELLITE_POINT_START_LAT',
 'SUB_SATELLITE_POINT_START_LON',
 'TIME_RANGE']
```

### Transform the data
```python
geotransform = ds.GetGeoTransform()
print(geotransform)

>>> (-81.26765645410755,
 0.04190368105409881,
 0.0,
 74.11423113858775,
 0.0,
 -0.04190368105409881)
```

###
```python
print(Meta['PRODUCT'])
>>> FAPAR

print(Meta['ORBIT_TYPE'])
>>> GEO

print(Meta['SATELLITE'],"\n")
>>> MSG4                                                                            -                                                                               -                                                                               -                                                                               -                                                                               -                                                                               -                                                                               -                                                                               -                                                                               -                                                                                


# There are some extra lines in this variable, so I just pulled just the satellite
print(Meta['SATELLITE'][0:4])
>>> MSG4
```

### Plotting the FAPAR product over Spain
<img src="https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/HDF-Examples/LandSaf_FAPAR_20181101_Spain.png">
