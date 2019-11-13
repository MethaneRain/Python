# A Quick Trial Into MetPy's Cross Section Function!

* The work done behind the scenes is amazing. With some minor modifications one could change the variables being plotted in Unidata's example.

### I decided to try some easy variables: RH, Omega, and Temp, and a pretty hard one: PV

These examples were taken using downloaded GFS Half Degree data via the THREDDS Server.
## My code needs:
* To manually download a netcdf file through the THREDDS catalog: http://thredds.ucar.edu/thredds/catalog.html
  * Here you can manually pick the variables you want, lat/lon extent, and times to add to your downloaded .nc file

## GFS Half Degree Forecast Example:

### Start at the Top of the THREDDS Server:

<img src="https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/Metpy-Cross-Section/Files/TREDDS_Current_Top_Cat.png" width="95%">

### Chose

<img src="https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/Metpy-Cross-Section/Files/TREDDS_Current_Model_List.png" width="95%">

###

<img src="https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/Metpy-Cross-Section/Files/TREDDS_Current_GFS_0p25_Forecast.png" width="95%">

###

<img src="https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/Metpy-Cross-Section/Files/TREDDS_Current_GFS_Latest_File.png" width="95%">

###

<img src="https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/Metpy-Cross-Section/Files/TREDDS_Current_GFS_Latest_Access.png" width="95%">

###

<img src="https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/Metpy-Cross-Section/Files/TREDDS_Current_GFS_Latest_NCSS_Full.png" width="95%">


### Once the file has been accesses in HTML, subsetting of data is optional:

<img src="https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/Metpy-Cross-Section/Files/Thredds_GFS_Current_Extent_1.png" width="20%"><img src="https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/Metpy-Cross-Section/Files/Thredds_GFS_Current_Extent_2.png" width="30%">

#### At the very bottom center of the website is the NCSS Request URL button. You need to click the <b>Submit</b> button to download the .nc file

<img src="https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/Metpy-Cross-Section/Files/Thredds_GFS_Current_Extent_3.png" width="90%">

## One major hiccup in generalizing the code to any variables is that the vertical and/or temporal levels need to be known. For example, currently in the GFS file:
### <ins>Single vertical level for Storm Motion</ins>
<img src="https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/Metpy-Cross-Section/Files/Thredds_GFS_Current_Isobaric_Lev_StromMotionHeight.png" width="55%">

* U-Component Storm Motion @ Specified height level above ground layer is at the vertical level: <i>height_above_ground_layer1</i> which is <b>3000.0 m</b>


### <ins>Omega (vertical velocity)</ins>
<img src="https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/Metpy-Cross-Section/Files/Thredds_Current_GFS_Isobaric_Levs_Omega.png" width="55%">

##### Omega has several vertical levels and that's why we can use it for vertical cross sections, but we also must know the <b>isobaric level</b> which is <b><i>isobaric6</i></b> to feed that into MetPy's <i>cross_section</i> function.
* The <b>isobaric6</b> levels are only for the vertical velocity variables. Temperature, winds, RH, etc. are on other levels such as <b>isobaric</b> or <b>isobaric4</b>, etc.

<img src="https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/Metpy-Cross-Section/Files/Thredds_Current_GFS_Isobaric_Levs_docs.png" width="55%">


## Omega (Vertical Velocity on Pressure Levels)
### Plotting omega in a vertical cross section
*

<img src="https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/Metpy-Cross-Section/Files/Omega_cross2019_09_10_0300ZZ.png" width="80%">



## Potential Vorticity!
### A vertical cross section of PV
#### I took on a challenge here with the potential to be a total bust, and so far it is.
* GFS PV variable doesn't have vertical levels so this will be the first obstacle
* PV levels are either 2e-06 or -2e-06, with the value being a <i><b>pressure level</b></i>
 * So we need to make a new DataArray with all the same coordinates and dimensions as the data file
  * (time, PVU_value, lat, lon) w/ PVU_value being 1 of 2 levels: 2e-06 or -2e-06
  * Geopotential_height_potential_vorticity_surface2 => New DataArray w/ shape (time,2,lat,lon)
  * We want 2e-06 level so the PVU_value be 1 (0th is -2e-06)
 * The vertical cooridante needs to be the color map!! -> still working on...
* The MetPy Cross Section function takes a very specific form of data, so there will have to be a new data variable to plot

### Relative Humidity Data Example:
<img src="https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/Metpy-Cross-Section/Files/THREDDS_GFS_Current_RH_data_printout.png" width="70%">

### Raw PV Data Example:
<img src="https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/Metpy-Cross-Section/Files/THREDDS_GFS_Current_PV_data_printout.png" width="70%">

### So we need to make a new PV DataArray creating vertical levels for the PV and use the pressure heights of the raw PV data to fill these vertical levels, and making the value of the new DataArray as either +/-2e-06 or zero.

*

#### Make a new coordinate for the PV vertical levels

<img src="https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/Metpy-Cross-Section/Files/THREDDS_GFS_Current_VertLevs.png" width="70%">

#### Fill the new array with either 2e-06 or zero for all lons in cross section space and vertical levels

<img src="https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/Metpy-Cross-Section/Files/THREDDS_GFS_Current_fillnew.png" width="70%">

#### Make a new DataArray with the new data and PV vertical levels

<img src="https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/Metpy-Cross-Section/Files/THREDDS_GFS_Current_New_DataArray.png" width="70%">

#### Add the new DataArray to the existing .nc file

<img src="https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/Metpy-Cross-Section/Files/THREDDS_GFS_Current_Add_DataArray_to_netcdf_data.png" width="70%">

#### Check the .nc file for the new variable

<img src="https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/Metpy-Cross-Section/Files/THREDDS_GFS_Current_PV2_data_1.png" width="70%">
<img src="https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/Metpy-Cross-Section/Files/THREDDS_GFS_Current_PV2_data_2.png" width="70%">



<br> </br>
<br> </br>
<br> </br>
