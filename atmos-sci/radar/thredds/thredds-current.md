THREDDS current data, only available for roughly a week

---

## For the non-archived data, Level II and III data can be accessed for maybe a week(??) from the current date

* Imports

```python
from siphon.cdmr import Dataset
from siphon.radarserver import get_radarserver_datasets, RadarServer
```

* Get a ist of available datasets 

```python
ds = get_radarserver_datasets('http://thredds.ucar.edu/thredds/')
print(list(ds))

['NEXRAD Level II Radar for Case Study CCS039', 
'NEXRAD Level II Radar from IDD', 
'NEXRAD Level III Radar for Case Study CCS039', 
'NEXRAD Level III Radar from IDD', 
'TDWR Level III Radar from IDD']
```



### Getting Level III data

Example: Base Velocity for Denver/Boulder

```python
ds = get_radarserver_datasets('http://thredds.ucar.edu/thredds/')
print(list(ds))

['NEXRAD Level II Radar for Case Study CCS039', 
'NEXRAD Level II Radar from IDD', 
'NEXRAD Level III Radar for Case Study CCS039', 
'NEXRAD Level III Radar from IDD', 
'TDWR Level III Radar from IDD']
```

```python
ds['NEXRAD Level III Radar from IDD'].follow().catalog_url

'http://thredds.ucar.edu/thredds/radarServer/nexrad/level3/IDD/dataset.xml'
```

* Finding out the ```xlm``` url
```python
url = ds['NEXRAD Level III Radar from IDD'].follow().catalog_url
rs = RadarServer(url)
print(rs)

<siphon.radarserver.RadarServer at 0x1a21dad048>
```

* Query the station, time(s), and variable(s)
```python
query = rs.query()
query.stations('FTG').time(datetime.utcnow()).variables('N1Q',"N1P")

var=N1Q&time=2019-08-26T01%3A55%3A28.721564&stn=FTG
```





* Look at each variable that was queried
1) 1-hr Precip
```python
catalog = rs.get_catalog(query)
dsv = list(catalog.datasets.values())[0]
dsv

Level3_FTG_N1P_20200502_2120.nids
```

```python
list(dsv.access_urls)
['OPENDAP', 'HTTPServer', 'CdmRemote']
```

```python
data = Dataset(dsv.access_urls['CdmRemote'])
data.variables

OrderedDict([('elevation', <siphon.cdmr.dataset.Variable at 0x1a25d15da0>),
             ('azimuth', <siphon.cdmr.dataset.Variable at 0x1a25d15550>),
             ('gate', <siphon.cdmr.dataset.Variable at 0x1a25d15668>),
             ('latitude', <siphon.cdmr.dataset.Variable at 0x1a25d15160>),
             ('longitude', <siphon.cdmr.dataset.Variable at 0x1a25d15a58>),
             ('altitude', <siphon.cdmr.dataset.Variable at 0x1a25d15b00>),
             ('rays_time', <siphon.cdmr.dataset.Variable at 0x1a25d15f98>),
             ('Precip1hr_RAW', <siphon.cdmr.dataset.Variable at 0x1a25d1e1d0>),
             ('Precip1hr', <siphon.cdmr.dataset.Variable at 0x1a25d1e3c8>),
             ('TabMessagePage',
              <siphon.cdmr.dataset.Variable at 0x1a25d1e550>)])
```

```python
data.summary

'Nexrad level 3 data are WSR-88D radar products.N1P is a raster image of 1 hour surface rainfall accumulation at range 124 nm'
```

2) Base Reflectivity
```python
catalog = rs.get_catalog(query)
dsv = list(catalog.datasets.values())[1]
dsv

Level3_FTG_N1Q_20200502_2120.nids
```

```python
list(dsv.access_urls)
['OPENDAP', 'HTTPServer', 'CdmRemote']
```

```python
data = Dataset(dsv.access_urls['CdmRemote'])
data.variables

OrderedDict([('elevation', <siphon.cdmr.dataset.Variable at 0x1a25d20f28>),
             ('azimuth', <siphon.cdmr.dataset.Variable at 0x1a25d25048>),
             ('gate', <siphon.cdmr.dataset.Variable at 0x1a25d25240>),
             ('latitude', <siphon.cdmr.dataset.Variable at 0x1a25d25320>),
             ('longitude', <siphon.cdmr.dataset.Variable at 0x1a25d254a8>),
             ('altitude', <siphon.cdmr.dataset.Variable at 0x1a25d25668>),
             ('rays_time', <siphon.cdmr.dataset.Variable at 0x1a25d25828>),
             ('BaseReflectivityDR_RAW',
              <siphon.cdmr.dataset.Variable at 0x1a25d259e8>),
             ('BaseReflectivityDR',
              <siphon.cdmr.dataset.Variable at 0x1a25d25be0>)])
```

```python
data.summary

'Nexrad level 3 data are WSR-88D radar products.N1Q is a radial image of base reflectivity field and its range 248 nm'
```




