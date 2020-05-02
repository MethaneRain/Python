Working with Radar data from Unidata's THREDDS server

---

### Getting Level III data

Example: 
```python
from siphon.cdmr import Dataset
from siphon.radarserver import get_radarserver_datasets, RadarServer
```

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

```python
url = ds['NEXRAD Level III Radar from IDD'].follow().catalog_url
rs = RadarServer(url)
print(rs)

<siphon.radarserver.RadarServer at 0x1a21dad048>
```

```python
query = rs.query()
query.stations('FTG').time(datetime.utcnow()).variables('N1Q')

var=N1Q&time=2019-08-26T01%3A55%3A28.721564&stn=FTG
```

```python
catalog = rs.get_catalog(query)
dsv = list(catalog.datasets.values())[0]
dsv

Level3_FTG_N1Q_20190826_0145.nids
```

```python
list(dsv.access_urls)
['OPENDAP', 'HTTPServer', 'CdmRemote']
```

```python
data = Dataset(dsv.access_urls['CdmRemote'])
data.variables

OrderedDict([('elevation', <siphon.cdmr.dataset.Variable at 0x182ab50470>),
             ('azimuth', <siphon.cdmr.dataset.Variable at 0x182ab505c0>),
             ('gate', <siphon.cdmr.dataset.Variable at 0x18278c4ba8>),
             ('latitude', <siphon.cdmr.dataset.Variable at 0x182a3652b0>),
             ('longitude', <siphon.cdmr.dataset.Variable at 0x182432cf60>),
             ('altitude', <siphon.cdmr.dataset.Variable at 0x182432c470>),
             ('rays_time', <siphon.cdmr.dataset.Variable at 0x182432ca20>),
             ('RadialVelocity_RAW',
              <siphon.cdmr.dataset.Variable at 0x182acd4f60>),
             ('RadialVelocity',
              <siphon.cdmr.dataset.Variable at 0x182acd4e80>)])
```

```python
data.summary

'Nexrad level 3 data are WSR-88D radar products.N0V is a radial image of base velocity at tilt 1'
```




