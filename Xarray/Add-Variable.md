One process that might be necessary would be to add a variable (DataSet) to an existing Xarray DataArray

Let's take a look into a GFS weather model .grb data file and append a new variable with data.

~~~Python
import xarray as xr
import pygrib as pg

File = "gfsanl_3_20190910_0000_000.grb2"

gfs_data = pg.open(File)
~~~

~~~Python
gfs_data()

>>>[1:Cloud mixing ratio:kg kg**-1 (instant):regular_ll:hybrid:level 1:fcst time 0 hrs:from 201909100000,
 2:Ice water mixing ratio:kg kg**-1 (instant):regular_ll:hybrid:level 1:fcst time 0 hrs:from 201909100000,
 3:Rain mixing ratio:kg kg**-1 (instant):regular_ll:hybrid:level 1:fcst time 0 hrs:from 201909100000,
 4:Snow mixing ratio:kg kg**-1 (instant):regular_ll:hybrid:level 1:fcst time 0 hrs:from 201909100000,
 5:Graupel (snow pellets):kg kg**-1 (instant):regular_ll:hybrid:level 1:fcst time 0 hrs:from 201909100000,
 6:Maximum/Composite radar reflectivity:dB (instant):regular_ll:atmosphere:level 0 -:fcst time 0 hrs:from 201909100000,
 7:Visibility:m (instant):regular_ll:surface:level 0:fcst time 0 hrs:from 201909100000,
 8:U component of wind:m s**-1 (instant):regular_ll:unknown:level 0:fcst time 0 hrs:from 201909100000,
 9:V component of wind:m s**-1 (instant):regular_ll:unknown:level 0:fcst time 0 hrs:from 201909100000,
 10:Ventilation Rate:m**2 s**-1 (instant):regular_ll:unknown:level 0:fcst time 0 hrs:from 201909100000,
 11:Wind speed (gust):m s**-1 (instant):regular_ll:surface:level 0:fcst time 0 hrs:from 201909100000,
 12:Geopotential Height:gpm (instant):regular_ll:isobaricInPa:level 40 Pa:fcst time 0 hrs:from 201909100000,
 13:Temperature:K (instant):regular_ll:isobaricInPa:level 40 Pa:fcst time 0 hrs:from 201909100000,
 14:Absolute vorticity:s**-1 (instant):regular_ll:isobaricInPa:level 40 Pa:fcst time 0 hrs:from 201909100000,
 15:Ozone mixing ratio:kg kg**-1 (instant):regular_ll:isobaricInPa:level 40 Pa:fcst time 0 hrs:from 201909100000,
 16:Geopotential Height:gpm (instant):regular_ll:isobaricInhPa:level 100 Pa:fcst time 0 hrs:from 201909100000,
 17:Temperature:K (instant):regular_ll:isobaricInhPa:level 100 Pa:fcst time 0 hrs:from 201909100000,
 18:Relative humidity:% (instant):regular_ll:isobaricInhPa:level 100 Pa:fcst time 0 hrs:from 201909100000,
 19:U component of wind:m s**-1 (instant):regular_ll:isobaricInhPa:level 100 Pa:fcst time 0 hrs:from 201909100000,
 20:V component of wind:m s**-1 (instant):regular_ll:isobaricInhPa:level 100 Pa:fcst time 0 hrs:from 201909100000,
 21:Ozone mixing ratio:kg kg**-1 (instant):regular_ll:isobaricInhPa:level 100 Pa:fcst time 0 hrs:from 201909100000,
 22:Geopotential Height:gpm (instant):regular_ll:isobaricInhPa:level 200 Pa:fcst time 0 hrs:from 201909100000,
 23:Temperature:K (instant):regular_ll:isobaricInhPa:level 200 Pa:fcst time 0 hrs:from 201909100000,
 24:Relative humidity:% (instant):regular_ll:isobaricInhPa:level 200 Pa:fcst time 0 hrs:from 201909100000,
 25:U component of wind:m s**-1 (instant):regular_ll:isobaricInhPa:level 200 Pa:fcst time 0 hrs:from 201909100000,
 26:V component of wind:m s**-1 (instant):regular_ll:isobaricInhPa:level 200 Pa:fcst time 0 hrs:from 201909100000,
 27:Ozone mixing ratio:kg kg**-1 (instant):regular_ll:isobaricInhPa:level 200 Pa:fcst time 0 hrs:from 201909100000,
 28:Geopotential Height:gpm (instant):regular_ll:isobaricInhPa:level 300 Pa:fcst time 0 hrs:from 201909100000,
 ...

 ~~~
