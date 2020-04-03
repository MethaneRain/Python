# Working with <strong><em>shapefiles</em></strong> in Python!

There are very usefual ways of working with shapefles in Python and below are some that I use regularly:
---
* Cartopy
* Geopandas
* Folium
* Bokeh

<ol>
<lil>Cartopy</li>
from cartopy.io.shapereader import Reader
Cartopy's builtin io.shapereader has a method Reader that can read common shapefiles
Cartopy has a method in it's feature call: cartopy.feature -> ShapelyFeature

ShapelyFeature allows for basic use of shapefiles in plotting

<li>Geopandas</li>

```Python
import geopandas
shp = 'someshapefile.shp'
geopandas.read_file(shp)

>>>
	ID	PRODUCT	VALID_TIME	QPF	UNITS	ISSUE_TIME	START_TIME	END_TIME	geometry
0	1	24-hour QPF	00Z 03/03/20 - 00Z 03/04/20	0.01	Inches	2020-03-02 20:31:27	2020-03-03 00:00:00	2020-03-04 00:00:00	POLYGON ((-69.67546 55.55996, -69.83924 55.541...
1	2	24-hour QPF	00Z 03/03/20 - 00Z 03/04/20	0.01	Inches	2020-03-02 20:31:27	2020-03-03 00:00:00	2020-03-04 00:00:00	POLYGON ((-97.47613 57.08302, -97.30711 56.970...
2	3	24-hour QPF	00Z 03/03/20 - 00Z 03/04/20	0.01	Inches	2020-03-02 20:31:27	2020-03-03 00:00:00	2020-03-04 00:00:00	POLYGON ((-104.33220 54.60180, -104.50477 54.5...
3	4	24-hour QPF	00Z 03/03/20 - 00Z 03/04/20	0.01	Inches	2020-03-02 20:31:27	2020-03-03 00:00:00	2020-03-04 00:00:00	POLYGON ((-66.19994 55.08777, -66.22888 55.023...
4	5	24-hour QPF	00Z 03/03/20 - 00Z 03/04/20	0.01	Inches	2020-03-02 20:31:27	2020-03-03 00:00:00	2020-03-04 00:00:00	POLYGON ((-110.21159 54.33732, -110.25039 54.2...
...	...	...	...	...	...	...	...	...	...
725	8	24-hour QPF	00Z 03/03/20 - 00Z 03/04/20	2.00	Inches	2020-03-02 20:31:27	2020-03-03 00:00:00	2020-03-04 00:00:00	POLYGON ((-75.95763 33.31393, -76.11561 33.257...
726	9	24-hour QPF	00Z 03/03/20 - 00Z 03/04/20	2.00	Inches	2020-03-02 20:31:27	2020-03-03 00:00:00	2020-03-04 00:00:00	POLYGON ((-75.42278 32.43779, -75.40114 32.420...
727	12	24-hour QPF	00Z 03/03/20 - 00Z 03/04/20	2.00	Inches	2020-03-02 20:31:27	2020-03-03 00:00:00	2020-03-04 00:00:00	POLYGON ((-108.21153 28.21766, -108.23091 28.1...
728	1	24-hour QPF	00Z 03/03/20 - 00Z 03/04/20	2.50	Inches	2020-03-02 20:31:27	2020-03-03 00:00:00	2020-03-04 00:00:00	POLYGON ((-73.17772 35.83285, -73.04513 35.813...
729	1	24-hour QPF	00Z 03/03/20 - 00Z 03/04/20	3.00	Inches	2020-03-02 20:31:27	2020-03-03 00:00:00	2020-03-04 00:00:00	POLYGON ((-73.93325 35.00080, -73.98394 34.939...
730 rows × 9 columns
```

<li>Folium</li>


<li>Bokeh</li>
</ol>
