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



### Getting Level III metadata

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


---

### Looking at the data? (2nd way of accessing data from server)

* Grab a quik summary of the meta data (again)
```python

cat = TDSCatalog("http://thredds.ucar.edu/thredds/radarServer/catalog.xml")
rs = RadarServer(cat.catalog_refs['NEXRAD Level III Radar from IDD'].href)
rs.metadata["documentation"]

{'summary': ['The NIDS data feed provides roughly 20 radar products sent every 5-10 minutes from 154 sites over NOAAPORT broadcast. These "derived" products include base reflectivity and velocity, composite reflectivity, precipitation estimates, echo tops and VAD winds']}
```

* List all of the available stations
```python
rs.stations

{'ABC': Station(id='ABC', elevation=49.0, latitude=60.78, longitude=-161.87, name='ANCHORAGE/Bethel'),
 'ABR': Station(id='ABR', elevation=397.0, latitude=45.45, longitude=-98.4, name='ABERDEEN/Aberdeen'),
 'ABX': Station(id='ABX', elevation=1789.0, latitude=35.13, longitude=-106.82, name='ALBUQUERQUE/Albuquerque'),
 'ACG': Station(id='ACG', elevation=63.0, latitude=56.85, longitude=-135.52, name='JUNEAU/Sitka'),
 'AEC': Station(id='AEC', elevation=16.0, latitude=64.5, longitude=-165.28, name='FAIRBANKS/Nome'),
 'AHG': Station(id='AHG', elevation=74.0, latitude=60.72, longitude=-151.35, name='ANCHORAGE/Nikiski'),
 'AIH': Station(id='AIH', elevation=20.0, latitude=59.45, longitude=-146.3, name='ANCHORAGE/Middleton_Island'),
 'AKC': Station(id='AKC', elevation=19.0, latitude=58.67, longitude=-156.62, name='ANCHORAGE/King_Salmon'),
 'AKQ': Station(id='AKQ', elevation=34.0, latitude=36.98, longitude=-77.0, name='WAKEFIELD/Wakefield'),
 'AMA': Station(id='AMA', elevation=1093.0, latitude=35.23, longitude=-101.7, name='AMARILLO/Amarillo'),
 'AMX': Station(id='AMX', elevation=4.0, latitude=25.6, longitude=-80.4, name='MIAMI/Miami'),
 'APD': Station(id='APD', elevation=790.0, latitude=65.03, longitude=-147.5, name='FAIRBANKS/Pedro_Dome'),
 'APX': Station(id='APX', elevation=446.0, latitude=44.9, longitude=-84.72, name='NORTH_CENTRAL_LOWER_MICHIGAN'),
 'ARX': Station(id='ARX', elevation=389.0, latitude=43.82, longitude=-91.18, name='LA_CROSSE/La_Crosse'),
 'ATX': Station(id='ATX', elevation=151.0, latitude=48.18, longitude=-122.48, name='SEATTLE/TACOMA/Camano_Island'),
 'BBX': Station(id='BBX', elevation=53.0, latitude=39.48, longitude=-121.62, name='SACRAMENTO/Oro_Dam_Blvd_West'),
 'BGM': Station(id='BGM', elevation=490.0, latitude=42.18, longitude=-75.98, name='BINGHAMTON/Binghamton'),
 'BHX': Station(id='BHX', elevation=732.0, latitude=40.48, longitude=-124.28, name='EUREKA/Humboldt_County'),
 'BIS': Station(id='BIS', elevation=505.0, latitude=46.77, longitude=-100.75, name='BISMARCK/Bismarck'),
 'BLX': Station(id='BLX', elevation=1097.0, latitude=45.85, longitude=-108.6, name='BILLINGS/Yellowstone_County'),
 'BMX': Station(id='BMX', elevation=197.0, latitude=33.17, longitude=-86.77, name='BIRMINGHAM/Alabaster'),
 'BOX': Station(id='BOX', elevation=36.0, latitude=41.95, longitude=-71.13, name='BOSTON/Taunton'),
 'BRO': Station(id='BRO', elevation=7.0, latitude=25.9, longitude=-97.42, name='BROWNSVILLE/Brownsville'),
 'BUF': Station(id='BUF', elevation=211.0, latitude=42.93, longitude=-78.73, name='BUFFALO/Cheektowaga'),
 'BYX': Station(id='BYX', elevation=2.0, latitude=24.58, longitude=-81.7, name='MIAMI/Boca_Chica_Key'),
 'CAE': Station(id='CAE', elevation=70.0, latitude=33.93, longitude=-81.12, name='COLUMBIA/Columbia'),
 'CBW': Station(id='CBW', elevation=227.0, latitude=46.03, longitude=-67.8, name='PORTLAND/Houlton'),
 'CBX': Station(id='CBX', elevation=933.0, latitude=43.48, longitude=-116.23, name='BOISE/Ada_County'),
 'CCX': Station(id='CCX', elevation=733.0, latitude=40.92, longitude=-78.0, name='CENTRAL_PENNSYLVANIA/Rush'),
 'CLE': Station(id='CLE', elevation=233.0, latitude=41.4, longitude=-81.85, name='CLEVELAND/Cleveland'),
 'CLX': Station(id='CLX', elevation=30.0, latitude=32.65, longitude=-81.03, name='CHARLESTON/Grays'),
 'CRP': Station(id='CRP', elevation=14.0, latitude=27.78, longitude=-97.5, name='CORPUS_CHRISTI/Corpus_Christ'),
 'CXX': Station(id='CXX', elevation=97.0, latitude=44.5, longitude=-73.17, name='BURLINGTON/Colchester'),
 'CYS': Station(id='CYS', elevation=1868.0, latitude=41.15, longitude=-104.8, name='CHEYENNE/Cheyenne'),
 'DAX': Station(id='DAX', elevation=9.0, latitude=38.5, longitude=-121.67, name='SACRAMENTO/Sacramento'),
 'DDC': Station(id='DDC', elevation=789.0, latitude=37.75, longitude=-99.97, name='DODGE_CITY/Dodge_City'),
 'DFX': Station(id='DFX', elevation=345.0, latitude=29.27, longitude=-100.27, name='AUSTIN/SAN_ANTONIO/US_Hwy_90'),
 'DGX': Station(id='DGX', elevation=186.0, latitude=32.17, longitude=-89.59, name='BRANDON/Jackson'),
 'DIX': Station(id='DIX', elevation=45.0, latitude=39.93, longitude=-74.4, name='PHILADELPHIA/Manchester'),
 'DLH': Station(id='DLH', elevation=435.0, latitude=46.83, longitude=-92.2, name='DULUTH/Duluth'),
 'DMX': Station(id='DMX', elevation=299.0, latitude=41.72, longitude=-93.72, name='DES_MOINES/Johnston'),
 'DOX': Station(id='DOX', elevation=15.0, latitude=38.82, longitude=-75.43, name='WAKEFIELD/Ellendale_State_Fo'),
 'DTX': Station(id='DTX', elevation=327.0, latitude=42.68, longitude=-83.47, name='DETROIT/White_Lake'),
 'DVN': Station(id='DVN', elevation=230.0, latitude=41.6, longitude=-90.57, name='QUAD_CITIES/Davenport'),
 'DYX': Station(id='DYX', elevation=462.0, latitude=32.53, longitude=-99.25, name='SAN_ANGELO/Shackelford_Count'),
 'EAX': Station(id='EAX', elevation=303.0, latitude=38.8, longitude=-94.25, name='KANSAS_CITY/PLEASANT_HILL/Pl'),
 'EMX': Station(id='EMX', elevation=1586.0, latitude=31.88, longitude=-110.62, name='TUCSON/Pima_County'),
 'ENX': Station(id='ENX', elevation=557.0, latitude=42.58, longitude=-74.05, name='ALBANY/East_Berne'),
 'EOX': Station(id='EOX', elevation=132.0, latitude=31.45, longitude=-85.45, name='BIRMINGHAM/Fort_Rucker'),
 'EPZ': Station(id='EPZ', elevation=1251.0, latitude=31.87, longitude=-106.68, name='EL_PASO/Santa_Teresa'),
 'ESX': Station(id='ESX', elevation=1483.0, latitude=35.7, longitude=-114.88, name='LAS_VEGAS/Nelson'),
 'EVX': Station(id='EVX', elevation=43.0, latitude=30.55, longitude=-85.92, name='TALLAHASSEE/Eglin_AFB'),
 'EWX': Station(id='EWX', elevation=193.0, latitude=29.7, longitude=-98.02, name='AUSTIN/SAN_ANTONIO/New_Braun'),
 'EYX': Station(id='EYX', elevation=840.0, latitude=35.08, longitude=-117.55, name='LAS_VEGAS/Edwards_AFB'),
 'FCX': Station(id='FCX', elevation=874.0, latitude=37.02, longitude=-80.27, name='ROANOKE/Floyd_County'),
 'FDR': Station(id='FDR', elevation=386.0, latitude=34.35, longitude=-98.97, name='OKLAHOMA_CITY/Altus_AFB'),
 'FDX': Station(id='FDX', elevation=1417.0, latitude=34.63, longitude=-103.62, name='ALBUQUERQUE/State_Rd_89'),
 'FFC': Station(id='FFC', elevation=262.0, latitude=33.35, longitude=-84.55, name='ATLANTA/Peachtree_City'),
 'FSD': Station(id='FSD', elevation=436.0, latitude=43.58, longitude=-96.72, name='SIOUX_FALLS/Sioux_Falls'),
 'FSX': Station(id='FSX', elevation=2261.0, latitude=34.57, longitude=-111.18, name='FLAGSTAFF/Coconino'),
 'FTG': Station(id='FTG', elevation=1675.0, latitude=39.78, longitude=-104.53, name='DENVER/BOULDER/Denver'),
 'FWS': Station(id='FWS', elevation=208.0, latitude=32.57, longitude=-97.3, name='DALLAS/FORT_WORTH/Fort_Worth'),
 'GGW': Station(id='GGW', elevation=694.0, latitude=48.2, longitude=-106.62, name='GLASGOW/Glasgow'),
 'GJX': Station(id='GJX', elevation=3045.0, latitude=39.05, longitude=-108.2, name='GRAND_JUNCTION/Mesa'),
 'GLD': Station(id='GLD', elevation=1113.0, latitude=39.37, longitude=-101.7, name='GOODLAND/Goodland'),
 'GRB': Station(id='GRB', elevation=208.0, latitude=44.48, longitude=-88.1, name='GREEN_BAY/Ashwaubenon'),
 'GRK': Station(id='GRK', elevation=164.0, latitude=30.72, longitude=-97.37, name='DALLAS/FORT_WORTH/Ft_Hood'),
 'GRR': Station(id='GRR', elevation=237.0, latitude=42.88, longitude=-85.53, name='GRAND_RAPIDS/Grand_Rapids'),
 'GSP': Station(id='GSP', elevation=287.0, latitude=34.88, longitude=-82.22, name='GREENVILLE/SPARTANBURG/Greer'),
 'GUA': Station(id='GUA', elevation=80.0, latitude=13.45, longitude=144.8, name='GUAM/Barrigada_Communication'),
 'GWX': Station(id='GWX', elevation=145.0, latitude=33.88, longitude=-88.32, name='MEMPHIS/MS_Hwy_8_and_US_Hwy_27'),
 'GYX': Station(id='GYX', elevation=125.0, latitude=43.88, longitude=-70.25, name='PORTLAND/Gray'),
 'HDX': Station(id='HDX', elevation=1287.0, latitude=33.07, longitude=-106.12, name='EL_PASO/White_Sands_Missile'),
 'HGX': Station(id='HGX', elevation=5.0, latitude=29.47, longitude=-95.07, name='HOUSTON/GALVESTON/Dickinson'),
 'HKI': Station(id='HKI', elevation=55.0, latitude=21.88, longitude=-159.55, name='HONOLULU/Kauai'),
 'HKM': Station(id='HKM', elevation=1162.0, latitude=20.12, longitude=-155.77, name='HONOLULU/Kohala'),
 'HMO': Station(id='HMO', elevation=415.0, latitude=21.12, longitude=-157.17, name='HONOLULU/Molokai'),
 'HNX': Station(id='HNX', elevation=74.0, latitude=36.3, longitude=-119.62, name='SAN_JOAQUIN_VALLEY/Hanford'),
 'HPX': Station(id='HPX', elevation=176.0, latitude=36.73, longitude=-87.28, name='PADUCAH/US_Hwy_41_N'),
 'HTX': Station(id='HTX', elevation=536.0, latitude=34.92, longitude=-86.08, name='BIRMINGHAM/Northeastern_AL'),
 'HWA': Station(id='HWA', elevation=421.0, latitude=19.08, longitude=-155.57, name='HONOLULU/Hawaii'),
 'ICT': Station(id='ICT', elevation=407.0, latitude=37.65, longitude=-97.43, name='WICHITA/Wichita'),
 'ICX': Station(id='ICX', elevation=3231.0, latitude=37.58, longitude=-112.85, name='SALT_LAKE_CITY/Cedar_City'),
 'ILN': Station(id='ILN', elevation=322.0, latitude=39.42, longitude=-83.82, name='CINCINNATI/Wilmington'),
 'ILX': Station(id='ILX', elevation=177.0, latitude=40.15, longitude=-89.33, name='CENTRAL_ILLINOIS/Lincoln'),
 'IND': Station(id='IND', elevation=241.0, latitude=39.7, longitude=-86.27, name='INDIANAPOLIS/Indianapolis'),
 'INX': Station(id='INX', elevation=204.0, latitude=36.17, longitude=-95.55, name='TULSA/Inola'),
 'IWA': Station(id='IWA', elevation=412.0, latitude=33.28, longitude=-111.67, name='PHOENIX/Mesa'),
 'IWX': Station(id='IWX', elevation=293.0, latitude=41.35, longitude=-85.7, name='NORTHERN_INDIANA/North_Webst'),
 'JAX': Station(id='JAX', elevation=10.0, latitude=30.48, longitude=-81.7, name='JACKSONVILLE/Jacksonville'),
 'JGX': Station(id='JGX', elevation=159.0, latitude=32.67, longitude=-83.35, name='ATLANTA/State_Hwy_96'),
 'JKL': Station(id='JKL', elevation=416.0, latitude=37.58, longitude=-83.3, name='JACKSON/Noctor'),
 'JUA': Station(id='JUA', elevation=931.0, latitude=18.12, longitude=-66.08, name='San_Juan/Puerta_Rico'),
 'KJK': Station(id='KJK', elevation=191.0, latitude=35.924, longitude=126.622, name='KOREA/Kunsan AFB'),
 'KSG': Station(id='KSG', elevation=1521.0, latitude=37.207, longitude=127.285, name='KOREA/Camp Humphreys'),
 'LBB': Station(id='LBB', elevation=993.0, latitude=33.65, longitude=-101.8, name='LUBBOCK/Lubbock'),
 'LCH': Station(id='LCH', elevation=4.0, latitude=30.12, longitude=-93.2, name='LAKE_CHARLES/Lake_Charles'),
 'LIX': Station(id='LIX', elevation=7.0, latitude=30.33, longitude=-89.82, name='NEW_ORLEANS/BATON_ROUGE/Slid'),
 'LNX': Station(id='LNX', elevation=905.0, latitude=41.95, longitude=-100.57, name='NORTH_PLATTE/Thedford'),
 'LOT': Station(id='LOT', elevation=202.0, latitude=41.6, longitude=-88.08, name='CHICAGO/Romeoville'),
 'LRX': Station(id='LRX', elevation=2056.0, latitude=40.73, longitude=-116.8, name='ELKO/Lander_County'),
 'LSX': Station(id='LSX', elevation=185.0, latitude=38.68, longitude=-90.67, name='ST._LOUIS/St_Charles'),
 'LTX': Station(id='LTX', elevation=20.0, latitude=33.98, longitude=-78.42, name='WILMINGTON/Shallotte'),
 'LVX': Station(id='LVX', elevation=219.0, latitude=37.97, longitude=-85.93, name='LOUISVILLE/Fort_Knox'),
 'LWX': Station(id='LWX', elevation=83.0, latitude=38.97, longitude=-77.47, name='BALTIMORE/WASH/Sterling'),
 'LZK': Station(id='LZK', elevation=173.0, latitude=34.83, longitude=-92.25, name='LITTLE_ROCK/N_Little_Rock'),
 'MAF': Station(id='MAF', elevation=874.0, latitude=31.93, longitude=-102.18, name='MIDLAND/ODESSA/Midland'),
 'MAX': Station(id='MAX', elevation=2290.0, latitude=42.07, longitude=-122.72, name='MEDFORD/Jackson_County'),
 'MBX': Station(id='MBX', elevation=455.0, latitude=48.38, longitude=-100.85, name='BISMARCK/McHenry_County'),
 'MHX': Station(id='MHX', elevation=9.0, latitude=34.77, longitude=-76.87, name='MOREHEAD_CITY/Newport'),
 'MKX': Station(id='MKX', elevation=292.0, latitude=42.97, longitude=-88.55, name='MILWAUKEE/Dousman'),
 'MLB': Station(id='MLB', elevation=11.0, latitude=28.1, longitude=-80.65, name='MELBOURNE/Melbourne'),
 'MOB': Station(id='MOB', elevation=63.0, latitude=30.67, longitude=-88.23, name='MOBILE/Mobile'),
 'MPX': Station(id='MPX', elevation=288.0, latitude=44.83, longitude=-93.55, name='MINNEAPOLIS/Chanhassen'),
 'MQT': Station(id='MQT', elevation=430.0, latitude=46.52, longitude=-87.53, name='MARQUETTE/Marquette'),
 'MRX': Station(id='MRX', elevation=408.0, latitude=36.17, longitude=-83.4, name='KNOXVILLE/TRI-CITIES/Morrist'),
 'MSX': Station(id='MSX', elevation=2394.0, latitude=47.03, longitude=-113.98, name='MISSOULA/Missoula_County'),
 'MTX': Station(id='MTX', elevation=1969.0, latitude=41.25, longitude=-112.43, name='SALT_LAKE_CITY/Elder_County'),
 'MUX': Station(id='MUX', elevation=1057.0, latitude=37.15, longitude=-121.88, name='SAN_FRANCISCO_BAY_AREA/Santa'),
 'MVX': Station(id='MVX', elevation=301.0, latitude=47.52, longitude=-97.32, name='EASTERN_NORTH_DAKOTA/Mayvill'),
 'MXX': Station(id='MXX', elevation=122.0, latitude=32.53, longitude=-85.78, name='BIRMINGHAM/Maxwell_AFB'),
 'NKX': Station(id='NKX', elevation=291.0, latitude=32.92, longitude=-117.03, name='SAN_DIEGO/San_Diego'),
 'NQA': Station(id='NQA', elevation=86.0, latitude=35.33, longitude=-89.87, name='MEMPHIS/Millington'),
 'OAX': Station(id='OAX', elevation=350.0, latitude=41.32, longitude=-96.37, name='OMAHA/Valley'),
 'ODN': Station(id='ODN', elevation=412.0, latitude=26.308, longitude=127.903, name='JAPAN/Kadena AFB'),
 'OHX': Station(id='OHX', elevation=176.0, latitude=36.23, longitude=-86.55, name='NASHVILLE/Old_Hickory'),
 'OKX': Station(id='OKX', elevation=26.0, latitude=40.85, longitude=-72.85, name='NEW_YORK_CITY/Upton'),
 'OTX': Station(id='OTX', elevation=727.0, latitude=47.67, longitude=-117.62, name='SPOKANE/Spokane'),
 'PAH': Station(id='PAH', elevation=119.0, latitude=37.07, longitude=-88.77, name='PADUCAH/Paducah'),
 'PBZ': Station(id='PBZ', elevation=361.0, latitude=40.52, longitude=-80.22, name='PITTSBURGH/Coraopolis'),
 'PDT': Station(id='PDT', elevation=462.0, latitude=45.68, longitude=-118.85, name='PENDLETON/Pendleton'),
 'POE': Station(id='POE', elevation=124.0, latitude=31.15, longitude=-92.97, name='LAKE_CHARLES/Fort_Polk'),
 'PUX': Station(id='PUX', elevation=1600.0, latitude=38.45, longitude=-104.17, name='PUEBLO/Pueblo_County'),
 'RAX': Station(id='RAX', elevation=106.0, latitude=35.65, longitude=-78.48, name='RALEIGH/DURHAM/Clayton'),
 'RGX': Station(id='RGX', elevation=2530.0, latitude=39.75, longitude=-119.45, name='RENO/Washoe_County'),
 'RIW': Station(id='RIW', elevation=1697.0, latitude=43.05, longitude=-108.47, name='RIVERTON/Riverton'),
 'RLX': Station(id='RLX', elevation=329.0, latitude=38.3, longitude=-81.72, name='CHARLESTON/Ruthdale'),
 'RTX': Station(id='RTX', elevation=479.0, latitude=45.7, longitude=-122.95, name='PORTLAND/Scappoose'),
 'SFX': Station(id='SFX', elevation=1364.0, latitude=43.1, longitude=-112.68, name='POCATELLO/IDAHO_FALLS/Spring'),
 'SGF': Station(id='SGF', elevation=390.0, latitude=37.23, longitude=-93.4, name='SPRINGFIELD/Springfield'),
 'SHV': Station(id='SHV', elevation=83.0, latitude=32.45, longitude=-93.83, name='SHREVEPORT/Shreveport'),
 'SJT': Station(id='SJT', elevation=576.0, latitude=31.37, longitude=-100.48, name='SAN_ANGELO/San_Angelo'),
 'SOX': Station(id='SOX', elevation=923.0, latitude=33.82, longitude=-117.63, name='SAN_DIEGO/Orange_County'),
 'SRX': Station(id='SRX', elevation=195.0, latitude=35.28, longitude=-94.35, name='TULSA/Western_Arkansas'),
 'TBW': Station(id='TBW', elevation=12.0, latitude=27.7, longitude=-82.4, name='TAMPA_BAY_AREA/Ruskin'),
 'TFX': Station(id='TFX', elevation=1132.0, latitude=47.45, longitude=-111.38, name='GREAT_FALLS/Great_Falls'),
 'TLH': Station(id='TLH', elevation=19.0, latitude=30.38, longitude=-84.32, name='TALLAHASSEE/Tallahassee'),
 'TLX': Station(id='TLX', elevation=370.0, latitude=35.32, longitude=-97.27, name='OKLAHOMA_CITY/Norman'),
 'TWX': Station(id='TWX', elevation=417.0, latitude=38.98, longitude=-96.22, name='TOPEKA/Alma'),
 'TYX': Station(id='TYX', elevation=562.0, latitude=43.76, longitude=-75.76, name='MONTAGUE/Fort_Drum'),
 'UDX': Station(id='UDX', elevation=919.0, latitude=44.12, longitude=-102.82, name='RAPID_CITY/New_Underwood'),
 'UEX': Station(id='UEX', elevation=602.0, latitude=40.32, longitude=-98.43, name='HASTINGS/Webster_County'),
 'VAX': Station(id='VAX', elevation=54.0, latitude=30.88, longitude=-83.0, name='TALLAHASSEE/State_Rd_129'),
 'VBX': Station(id='VBX', elevation=373.0, latitude=34.83, longitude=-120.38, name='LOS_ANGELES/Orcutt_Oil_Field'),
 'VNX': Station(id='VNX', elevation=369.0, latitude=36.73, longitude=-98.12, name='OKLAHOMA_CITY/Kegelman_Aux_F'),
 'VTX': Station(id='VTX', elevation=831.0, latitude=34.4, longitude=-119.17, name='LOS_ANGELES/Ventura_County'),
 'VWX': Station(id='VWX', elevation=190.0, latitude=38.27, longitude=-87.72, name='EVANSVILLE/Owensville'),
 'YUX': Station(id='YUX', elevation=53.0, latitude=32.48, longitude=-114.65, name='PHOENIX/Yuma')}
```

##### Calling specific station, ie Denver (FTG)

```python
rs.stations["FTG"]

Station(id='FTG', elevation=1675.0, latitude=39.78, longitude=-104.53, name='DENVER/BOULDER/Denver')
```

