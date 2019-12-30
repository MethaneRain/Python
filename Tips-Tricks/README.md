# Tips-Tricks

### Over the years I've been able to collect various tips and tricks of the trade that have helped me along the way in Python. To help find these quickly I've documented them here. 

### 
----

Passing variables as strings:

```Python
a = 'these'
b = 'are positional'
c = ''.join(['py','th','on',' ','va','ri','ab','le','s']) + '!'

%%bash -s "$a" "$b" "$c"
echo "a=$1 b=$2 c=$3"

>>>
a=these b=are positional c=python variables!
```

---

A little cool ```markdown``` styling:

```
4 day forecasts: old graphics             |  Combined
:-------------------------:|:-------------------------:
![](https://www.wpc.ncep.noaa.gov/basicwx/92fndfd.gif)  |  ![](https://raw.githubusercontent.com/MethaneRain/Python-Jupyter/master/Jupyter-Notebooks/Weather-Notebooks/Various%20Weather%20Agency%20Maps/WPC_4_Day%20Forecast_%2017%20November%202019%2011%3A00Z.png)

3 day forecasts: updated graphics             |  Combined
:-------------------------:|:-------------------------:
![](https://www.wpc.ncep.noaa.gov/noaa/noaad2.gif)  |  ![](https://raw.githubusercontent.com/MethaneRain/Python-Jupyter/master/Jupyter-Notebooks/Weather-Notebooks/Various%20Weather%20Agency%20Maps/WPC_3_Day%20Forecast_%2017%20November%202019%2011%3A00Z.png)
```

<h6> The above code in a ```markdown``` cell will produce the image below! </h6>

4 day forecasts: old graphics             |  Combined
:-------------------------:|:-------------------------:
![](https://www.wpc.ncep.noaa.gov/basicwx/92fndfd.gif)  |  ![](https://raw.githubusercontent.com/MethaneRain/Python-Jupyter/master/Jupyter-Notebooks/Weather-Notebooks/Various%20Weather%20Agency%20Maps/WPC_4_Day%20Forecast_%2017%20November%202019%2011%3A00Z.png)

3 day forecasts: updated graphics             |  Combined
:-------------------------:|:-------------------------:
![](https://www.wpc.ncep.noaa.gov/noaa/noaad2.gif)  |  ![](https://raw.githubusercontent.com/MethaneRain/Python-Jupyter/master/Jupyter-Notebooks/Weather-Notebooks/Various%20Weather%20Agency%20Maps/WPC_3_Day%20Forecast_%2017%20November%202019%2011%3A00Z.png)
