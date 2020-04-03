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
```
<img src="https://raw.githubusercontent.com/MethaneRain/Python/master/geospatial-python/shapefiles/geopandas_shapefile.png" width="70%">

<li>Folium</li>


<li>Bokeh</li>
</ol>
