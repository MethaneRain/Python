## Plots from the fantastic GOES-16 and 17 Satellites

### A lot of external work from some very talented people (I have tried to give all credit where credit is due on the various pieces) plus a lot of my own piecing together has manifested into plotting of GOES 16 and 17 satellite images for: 

* Visible - ch 2
* Water Vapor - ch 9
* Infrared - ch 13
* Psuedo True Color: R (ch 2), G (ch 3), B (ch 1)
* GOES Lightning Mapper

There are still some things that need to be worked out and clarified in the code. One major hiccup I have with plotting GOES-16 data in my Lambert Conformal projection is a slight misalignment of data and map on the west coast. See the issues/problems folder.

The files can be quickly downloaded via Python and rclone with Amazon Web Services remote connection setup. 

Take a look at the notebook here: https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/GOES%20Satellite%20Maps/rclone_AWS_GOES.ipynb

With setup instructions here: https://github.com/blaylockbk/pyBKB_v3/blob/master/rclone_howto.md

## Colorado Bomb Cyclone 2-day setup in WV
![wv_CO_bomb](https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/GOES%20Satellite%20Maps/Sample%20Maps/WV.gif)

## Sweet Frontal Boundary Over the Pacific
![alt text](https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/GOES%20Satellite%20Maps/Sample%20Maps/GOES17_TrueColor_Jan16_2019.gif)

## 2017 Total Solar Eclipse!!
![CONUS Solar Eclipse](https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/GOES%20Satellite%20Maps/Sample%20Maps/2017_Eclipse.gif)

## GLM Over Texas
![GLM Texas](https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/GOES%20Satellite%20Maps/Sample%20Maps/GOES_GLM_20181226.gif)

## Cyclone over Northeast
![](https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/GOES%20Satellite%20Maps/Sample%20Maps/Resized_GOES_Ch13_IR_2018_004_15_30.png)

## Combining station plots with GOES satellite images
### MetPy station plot notebook customized with parts from my GOES notebook 
#### Super thanks to Bryan Guarente from UCAR on showing me how to download ASOS station data using Python

![GOES and Station Plots](https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/Playground/Images/Resized_GOES16_Ch2_StationPlot2018_12_10_1647.png)

## A quick plot of both GOES east and west as a mosiac
### Obviously this is not the best mosiac approach. The east plot is plotted over the west, so it is clear that the western part of GOES east is different from what GOES west would have plotted. I believe the next step I will try is to plot east to longitude -100 and same for the west...

![GOES Mosiac](https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/GOES%20Satellite%20Maps/Sample%20Maps/GOES16_17_Mosiac.png)

* Better Mosiac (limiting plotting from datasets)
![GOES Mosiac](https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/GOES%20Satellite%20Maps/Sample%20Maps/GOES_Mosiac_2019_05_23_0601.png)

## Colorado Bomb
![](https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/GOES%20Satellite%20Maps/Sample%20Maps/GOES16_Ch13_2019_03_13_1902.png)

## Mid-Level Water Vapor
* Black and White                                                              Colored

<img src="https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/GOES%20Satellite%20Maps/Sample%20Maps/GOES_Ch9_WV_2018_356_12_02.png" width="50%"><img src="https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/GOES%20Satellite%20Maps/Sample%20Maps/GOES_Ch9_WV_2018_356_12_02_colored.png" width="50%">
