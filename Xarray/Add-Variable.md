One process that might be necessary would be to add a variable (DataSet) to an existing Xarray DataArray

Let's take a look into a GFS weather model .grb data file and append a new variable with data.

~~~Python
import xarray as xr
import pygrib as pg

File = "gfsanl_3_20190910_0000_000.grb2"

ass = pg.open(File)
~~~
