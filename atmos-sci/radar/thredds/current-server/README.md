Grabbing Radar Data from Unidata's THREDDS Server

* This server has roughly a month'd worth of current data

---

I've put together a class fo functions that is meant to be a quick plotting script using ```siphon``` to access the THREDDS server
 
 ---

Here is an example of running it in a Jupyter notebook:

* The name of the script is Thredds_Lev3_Radar.py

```python
import Thredds_Lev3_Radar as radar

This library only plots Base Reflectivity and Radial Velocity
Many other products are available in the data!

Avaliable THREDDS Dataset Names:
------------------------------
NEXRAD Level II Radar for Case Study CCS039
NEXRAD Level II Radar from IDD
NEXRAD Level III Radar for Case Study CCS039
NEXRAD Level III Radar from IDD
TDWR Level III Radar from IDD

Start by running the query_radar_data() function, then the radar_plot() fucntion
```

There is an ```example``` function that will quickly plot the most recent time avaliable for Denver (FTG) and Base Reflectivity

```python
radar.example()

Queried Time Range:
------------------------------
query start time: 2020-05-16 16:20:08.400528
query end time: 2020-05-16 16:20:08.400528 


Station (FTG: Denver) Info: 
--------------------------
Station(id='FTG', elevation=1675.0, latitude=39.78, longitude=-104.53, name='DENVER/BOULDER/Denver')


List of Queried Files:
---------------------------------
Level3_FTG_N0V_20200516_1611.nids


File Time Info
--------------------------------
Date: 2020-05-16
Time: 16:11:02
Date-time: 2020-05-16 16:11:02
title time: 16 May 2020 1611Z
filename time: 2020_05_16_1611Z 


Full data printout: 
---------------------------------
  https://thredds.ucar.edu/thredds/cdmremote/nexrad/level3/IDD/N0V/FTG/20200516/Level3_FTG_N0V_20200516_1611.nids
Dimensions:
<class 'siphon.cdmr.dataset.Dimension'> name = azimuth, size = 360
<class 'siphon.cdmr.dataset.Dimension'> name = gate, size = 230
Variables:
<class 'siphon.cdmr.dataset.Variable'>
float32 elevation(azimuth)
        _CoordinateAxisType: RadialElevation
        units: degrees
        long_name: elevation angle in degres: 0 = parallel to pedestal base, 90 = perpendicular
shape = 360
<class 'siphon.cdmr.dataset.Variable'>
float32 azimuth(azimuth)
        _CoordinateAxisType: RadialAzimuth
        units: degrees
        long_name: azimuth angle in degrees: 0 = true north, 90 = east
shape = 360
<class 'siphon.cdmr.dataset.Variable'>
float32 gate(gate)
        _CoordinateAxisType: RadialDistance
        units: meters
        long_name: Radial distance to the start of gate
shape = 230
<class 'siphon.cdmr.dataset.Variable'>
float32 latitude(azimuth)
        _CoordinateAxisType: Lat
        units: degrees
        long_name: Latitude of the instrument
shape = 360
<class 'siphon.cdmr.dataset.Variable'>
float32 longitude(azimuth)
        _CoordinateAxisType: Lon
        units: degrees
        long_name: Longitude of the instrument
shape = 360
<class 'siphon.cdmr.dataset.Variable'>
float32 altitude(azimuth)
        _CoordinateAxisType: Height
        units: meters
        long_name: Altitude in meters (asl) of the instrument
shape = 360
<class 'siphon.cdmr.dataset.Variable'>
float64 rays_time(azimuth)
        _CoordinateAxisType: Time
        units: milliseconds since 1970-01-01 00:00 UTC
        long_name: rays time
shape = 360
<class 'siphon.cdmr.dataset.Variable'>
int8 RadialVelocity_RAW(azimuth, gate)
        units: m/s
        _CoordinateAxes: elevation azimuth gate rays_time latitude longitude altitude
        _Unsigned: true
shape = (360, 230)
<class 'siphon.cdmr.dataset.Variable'>
float32 RadialVelocity(azimuth, gate)
        long_name: VEL: Radial Velocity
        units: m/s
        _CoordinateAxes: elevation azimuth gate rays_time latitude longitude altitude
shape = (360, 230)
Attributes:
        title: Nexrad Level 3 Data
        keywords: WSR-88D; NIDS
        creator_name: NOAA/NWS
        creator_url: http://www.ncdc.noaa.gov/oa/radar/radarproducts.html
        naming_authority: NOAA/NCDC
        Divider: -1
        RadarLatitude: 39.786
        RadarLongitude: -104.546
        RadarAltitude: 1709.928
        ProductStation: FTG
        ProductStationName: Denver/Boulder,CO,US
        OperationalMode: 1
        VolumeCoveragePatternName: 35
        SequenceNumber: 5455
        VolumeScanNumber: 3
        DateCreated: 2020-05-16T16:12:40Z
        ElevationNumber: 1
        NumberOfMaps: 0
        summary: Nexrad level 3 data are WSR-88D radar products.N0V is a radial image of base velocity at tilt 1
        keywords_vocabulary: N0V
        conventions: _Coordinates
        format: Level3/NIDS
        geospatial_lat_min: 37.72081756591797
        geospatial_lat_max: 41.85118103027344
        geospatial_lon_min: -101.8558349609375
        geospatial_lon_max: -107.23616790771484
        geospatial_vertical_min: 1709.927978515625
        geospatial_vertical_max: 1709.927978515625
        RadarElevationNumber: 5
        time_coverage_start: 2020-05-16T16:11:02Z
        time_coverage_end: 2020-05-16T16:11:02Z
        data_min: -32665.0
        data_max: 104.0
        isRadial: 1
        cdm_data_type: RADIAL
```