# Working with Datetimes

Within a data array, metadata typically exists along with the actual variable data. One helpful piece of information within the metadata are the time stamps of the files/data values.

within Python there are packages like ```Numpy``` and the data frameworks like ```Xarray``` and ```Pandas``` all have ways of working with date-time variables to put these pieces of information onto correct current time and date and also be able to calculate like numbers. There are also the ```datetime``` and ```netCDF4``` packages which have their own methods for handling date-times.

---
<h2> Example 1 </h2>
<h3> Let's take a look at some archived ECMWF data </h3>

Importing the ```netCDF4``` package and ```Dataset``` method to read int he data and then grabbing the time variable:

```Python
import netCDF4
ncfile = netCDF4.Dataset('_grib2netcdf-atls06-95e2cf679cd58ee9b4db4dd119a05a8d-OT6_qA.nc', 'r')
time = ncfile.variables['time']
print(time)

>>>
<class 'netCDF4._netCDF4.Variable'>
int32 time(time)
    units: hours since 1900-01-01 00:00:00.0
    long_name: time
    calendar: gregorian
unlimited dimensions: time
current shape = (31,)
filling on, default _FillValue of -2147483647 used
```

and

```Python
print(time.units)

>>> hours since 1900-01-01 00:00:00.0
```

So this particular dataset has 31 time steps with units of hours since Jan 1st 1900. Wow, not very helpful if we want to consider plotting and evaluation of the data.

If we grab the actual values fo the time variable:

```Python
print(time[:])

>>>
[1043148 1043172 1043196 1043220 1043244 1043268 1043292 1043316 1043340
 1043364 1043388 1043412 1043436 1043460 1043484 1043508 1043532 1043556
 1043580 1043604 1043628 1043652 1043676 1043700 1043724 1043748 1043772
 1043796 1043820 1043844 1043868]
 ```

 Ok, so we have some big numbers here, and notice that they all have a difference of 24 units or 24 hours. So each time step is one day apart. Cool, but we still don't have much of an idea of the actual date or time.

 We have several tools at our disposal to help figure out the conversion!

 ---

<h3> First, the ```netCDF4``` package has the ```num2date``` method. </h3>

Let's take a quick look the docstring for the ```num2date``` method:

```Python
netCDF4.num2date?

>>>
Docstring:
num2date(times,units,calendar='standard')

Return datetime objects given numeric time values. The units
of the numeric time values are described by the `units` argument
and the `calendar` keyword. The returned datetime objects represent
UTC with no time-zone offset, even if the specified
`units` contain a time-zone offset.

**`times`**: numeric time values.

**`units`**: a string of the form `<time units> since <reference time>`
describing the time units. `<time units>` can be days, hours, minutes,
seconds, milliseconds or microseconds. `<reference time>` is the time
origin. `months_since` is allowed *only* for the `360_day` calendar.

**`calendar`**: describes the calendar used in the time calculations.
All the values currently defined in the
[CF metadata convention](http://cfconventions.org)
Valid calendars `'standard', 'gregorian', 'proleptic_gregorian'
'noleap', '365_day', '360_day', 'julian', 'all_leap', '366_day'`.
Default is `'standard'`, which is a mixed Julian/Gregorian calendar.

**`only_use_cftime_datetimes`**: if False (default), datetime.datetime
objects are returned from num2date where possible; if True dates which
subclass cftime.datetime are returned for all calendars.

returns a datetime instance, or an array of datetime instances with
approximately 100 microsecond accuracy.

***Note***: The datetime instances returned are 'real' python datetime
objects if `calendar='proleptic_gregorian'`, or
`calendar='standard'` or `'gregorian'`
and the date is after the breakpoint between the Julian and
Gregorian calendars (1582-10-15). Otherwise, they are 'phony' datetime
objects which support some but not all the methods of 'real' python
datetime objects. The datetime instances
do not contain a time-zone offset, even if the specified `units`
contains one.
Type:      builtin_function_or_method
```

Thus we need the time values, the time units and an optional calendar call. If you noticed in our ECMWF data, the calendar was ```gregorian```, so that is what we will include.

In our ECMWF example:

```Python
print(netCDF4.num2date(time[:], time.units, time.calendar))

>>>
array([datetime.datetime(2019, 1, 1, 12, 0),
       datetime.datetime(2019, 1, 2, 12, 0),
       datetime.datetime(2019, 1, 3, 12, 0),
       datetime.datetime(2019, 1, 4, 12, 0),
       datetime.datetime(2019, 1, 5, 12, 0),
       datetime.datetime(2019, 1, 6, 12, 0),
       datetime.datetime(2019, 1, 7, 12, 0),
       datetime.datetime(2019, 1, 8, 12, 0),
       datetime.datetime(2019, 1, 9, 12, 0),
       datetime.datetime(2019, 1, 10, 12, 0),
       datetime.datetime(2019, 1, 11, 12, 0),
       datetime.datetime(2019, 1, 12, 12, 0),
       datetime.datetime(2019, 1, 13, 12, 0),
       datetime.datetime(2019, 1, 14, 12, 0),
       datetime.datetime(2019, 1, 15, 12, 0),
       datetime.datetime(2019, 1, 16, 12, 0),
       datetime.datetime(2019, 1, 17, 12, 0),
       datetime.datetime(2019, 1, 18, 12, 0),
       datetime.datetime(2019, 1, 19, 12, 0),
       datetime.datetime(2019, 1, 20, 12, 0),
       datetime.datetime(2019, 1, 21, 12, 0),
       datetime.datetime(2019, 1, 22, 12, 0),
       datetime.datetime(2019, 1, 23, 12, 0),
       datetime.datetime(2019, 1, 24, 12, 0),
       datetime.datetime(2019, 1, 25, 12, 0),
       datetime.datetime(2019, 1, 26, 12, 0),
       datetime.datetime(2019, 1, 27, 12, 0),
       datetime.datetime(2019, 1, 28, 12, 0),
       datetime.datetime(2019, 1, 29, 12, 0),
       datetime.datetime(2019, 1, 30, 12, 0),
       datetime.datetime(2019, 1, 31, 12, 0)], dtype=object)
```

Awesome! Now we can see we have a month's worth of daily time steps at 12Z for January.
