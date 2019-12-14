<font size = 20><i>netCDF Files</i></font>

---

<font size = 16>Some quick tips for working with different <i>.nc</i> files</font>
* GOES data - from saved file
* Reanalysis data - from saved file
* Thredds server model data - remotely from server file

<font size = 16>GOES <i>.nc</i> file:</font>
```python
File = GOES16_samples_9[0]
print(File)

>>> OR_ABI-L1b-RadC-M3C09_G16_s20190711202123_e20190711204502_c20190711204543.nc
```
```python
ch9nc = Dataset(File)

```


<img src="https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/netCDF-Examples/GOES_dataset_methods.png" width="50%">

```python
dir(ch9nc)

>>> ['Conventions',
 'Metadata_Conventions',
 '__class__',
 '__delattr__',
 '__dir__',
 '__doc__',
 '__enter__',
 '__eq__',
 '__exit__',
 '__format__',
 '__ge__',
 '__getattr__',
 '__getattribute__',
 '__getitem__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__ne__',
 '__new__',
 '__orthogonal_indexing__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__unicode__',
 '_close',
 '_close_mem',
 '_enddef',
 '_grpid',
 '_isopen',
 '_ncstring_attrs__',
 '_redef',
 'cdm_data_type',
 'close',
 'cmptypes',
 'createCompoundType',
 'createDimension',
 'createEnumType',
 'createGroup',
 'createVLType',
 'createVariable',
 'data_model',
 'dataset_name',
 'date_created',
 'delncattr',
 'dimensions',
 'disk_format',
 'enumtypes',
 'file_format',
 'filepath',
 'get_variables_by_attributes',
 'getncattr',
 'groups',
 'id',
 'institution',
 'instrument_ID',
 'instrument_type',
 'iso_series_metadata_id',
 'isopen',
 'keepweakref',
 'keywords',
 'keywords_vocabulary',
 'license',
 'naming_authority',
 'ncattrs',
 'orbital_slot',
 'parent',
 'path',
 'platform_ID',
 'processing_level',
 'production_data_source',
 'production_environment',
 'production_site',
 'project',
 'renameAttribute',
 'renameDimension',
 'renameGroup',
 'renameVariable',
 'scene_id',
 'set_always_mask',
 'set_auto_chartostring',
 'set_auto_mask',
 'set_auto_maskandscale',
 'set_auto_scale',
 'set_fill_off',
 'set_fill_on',
 'set_ncstring_attrs',
 'setncattr',
 'setncattr_string',
 'setncatts',
 'spatial_resolution',
 'standard_name_vocabulary',
 'summary',
 'sync',
 'time_coverage_end',
 'time_coverage_start',
 'timeline_id',
 'title',
 'variables',
 'vltypes']
```

```python
print(ch9nc.keywords)

>>> 'SPECTRAL/ENGINEERING > INFRARED WAVELENGTHS > INFRARED RADIANCE'
```

---

<font size = 14>We can think of the file as a hierarchy</font>
An example using the value of the satellite height of GOES:

ch9nc
* ch9nc.variables
  * ch9nc.variables['goes_imager_projection']
    * ch9nc.variables['goes_imager_projection'].perspective_point_height


```python
list(ch9nc.variables)

>>> ['Rad',
 'DQF',
 't',
 'y',
 'x',
 'time_bounds',
 'goes_imager_projection',
 'y_image',
 'y_image_bounds',
 'x_image',
 'x_image_bounds',
 'nominal_satellite_subpoint_lat',
 'nominal_satellite_subpoint_lon',
 'nominal_satellite_height',
 'geospatial_lat_lon_extent',
 'yaw_flip_flag',
 'band_id',
 'band_wavelength',
 'esun',
 'kappa0',
 'planck_fk1',
 'planck_fk2',
 'planck_bc1',
 'planck_bc2',
 'valid_pixel_count',
 'missing_pixel_count',
 'saturated_pixel_count',
 'undersaturated_pixel_count',
 'min_radiance_value_of_valid_pixels',
 'max_radiance_value_of_valid_pixels',
 'mean_radiance_value_of_valid_pixels',
 'std_dev_radiance_value_of_valid_pixels',
 'percent_uncorrectable_L0_errors',
 'earth_sun_distance_anomaly_in_AU',
 'algorithm_dynamic_input_data_container',
 'processing_parm_version_container',
 'algorithm_product_version_container',
 't_star_look',
 'band_wavelength_star_look',
 'star_id']
````

```python
print(ch9nc.variables['goes_imager_projection'])

>>> <class 'netCDF4._netCDF4.Variable'>
int32 goes_imager_projection()
    long_name: GOES-R ABI fixed grid projection
    grid_mapping_name: geostationary
    perspective_point_height: 35786023.0
    semi_major_axis: 6378137.0
    semi_minor_axis: 6356752.31414
    inverse_flattening: 298.2572221
    latitude_of_projection_origin: 0.0
    longitude_of_projection_origin: -75.0
    sweep_angle_axis: x
unlimited dimensions:
current shape = ()
filling on, default _FillValue of -2147483647 used
```

```python
print(ch9nc.variables['goes_imager_projection'].perspective_point_height)

>>> 35786023.0
```
<font size = 16>Thredds Server <i>.nc</i> file:</font>

There are some amazing tools out there now for getting the data on the TREDDS server. Siphon and NetCDF Server Sevice? (NCSS) make access the data pretty straight forward, even if you're not versed on the inner workings of these packages.

```python
from siphon.catalog import TDSCatalog
top_cat = TDSCatalog('http://thredds.ucar.edu/thredds/catalog.xml')
ref = top_cat.catalog_refs['Forecast Model Data']
new_cat = ref.follow()
model = new_cat.catalog_refs[4]
gfs_cat = model.follow()
ds = gfs_cat.datasets[0]
print("Variable Name:",ds.name)
print("Path:",ds.url_path)

>>> Variable Name: Full Collection (Reference / Forecast Time) Dataset
>>> Path: grib/NCEP/GFS/Global_0p25deg/TwoD
```

```python
ds = gfs_cat.datasets[1]
subset = ds.subset()
query_data = subset.query()
query_data.lonlat_box(west=-130, east=-50, south=10, north=60)

# Allow for NetCDF files
query_data.accept('netcdf4')
query_data.time(i)
query_data.variables('Geopotential_height_isobaric',
                   'Pressure_reduced_to_MSL_msl',
                   'u-component_of_wind_isobaric',
                   'v-component_of_wind_isobaric'

print(ds)

>>> Best GFS Quarter Degree Forecast Time Series

```

```python
data = subset.get_data(query_data)
print(data)

>>> <class 'netCDF4._netCDF4.Dataset'>
>>> root group (NETCDF4 data model, file format HDF5):
>>>     Originating_or_generating_Center: US National Weather Service, National Centres for Environmental Prediction (NCEP)
>>>     Originating_or_generating_Subcenter: 0
>>>     GRIB_table_version: 2,1
>>>     Type_of_generating_process: Forecast
>>>     Analysis_or_forecast_generating_process_identifier_defined_by_originating_centre: Analysis from GFS (Global Forecast System)
>>>     Conventions: CF-1.6
>>>     history: Read using CDM IOSP GribCollection v3
>>>     featureType: GRID
>>>     History: Translated to CF-1.0 Conventions by Netcdf-Java CDM (CFGridWriter2)
>>> Original Dataset = /data/ldm/pub/native/grid/NCEP/GFS/Global_0p25deg/GFS-Global_0p25deg.ncx3; Translation Date = 2019-03-31T15:55:39.692Z
>>>     geospatial_lat_min: 10.0
>>>     geospatial_lat_max: 60.0
>>>     geospatial_lon_min: -130.0
>>>     geospatial_lon_max: -50.0
>>>     dimensions(sizes): time(1), isobaric(31), lat(201), lon(321)
>>>     variables(dimensions): float32 u-component_of_wind_isobaric(time,isobaric,lat,lon), float64 reftime(time), float64 time(time), float32 isobaric(isobaric), float32 lat(lat), float32 lon(lon), int32 LatLon_Projection(), float32 Pressure_reduced_to_MSL_msl(time,lat,lon), float32 v-component_of_wind_isobaric(time,isobaric,lat,lon), float32 Geopotential_height_isobaric(time,isobaric,lat,lon)
    groups:

```

```python
print(data.variables['Pressure_reduced_to_MSL_msl'])

>>> <class 'netCDF4._netCDF4.Variable'>
>>> float32 Pressure_reduced_to_MSL_msl(time, lat, lon)
>>>     long_name: Pressure reduced to MSL @ Mean sea level
>>>     units: Pa
>>>     abbreviation: PRMSL
>>>     missing_value: nan
>>>     grid_mapping: LatLon_Projection
>>>     coordinates: reftime time lat lon
>>>     Grib_Variable_Id: VAR_0-3-1_L101
>>>     Grib2_Parameter: [0 3 1]
>>>     Grib2_Parameter_Discipline: Meteorological products
>>>     Grib2_Parameter_Category: Mass
>>>     Grib2_Parameter_Name: Pressure reduced to MSL
>>>     Grib2_Level_Type: 101
>>>     Grib2_Level_Desc: Mean sea level
>>>     Grib2_Generating_Process_Type: Forecast
>>> unlimited dimensions:
>>> current shape = (1, 201, 321)
>>> filling off
```

```Python
mslp_metadata = data.variables['Pressure_reduced_to_MSL_msl']
mslp_metadata.long_name

>>> 'Pressure reduced to MSL @ Mean sea level'
```

```Python
mslp_metadata.units

>>> 'Pa'
```

---

<font size=25>ECMWF Reanalysis</font>

