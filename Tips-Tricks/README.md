# Tips-Tricks

### Over the years I've been able to collect various tips and tricks of the trade that have helped me along the way in Python. To help find these quickly I've documented them here. 

### 
----

Passing variables as strings:

* Bash example

```Python
a = 'these'
b = 'are positional'
c = ''.join(['py','th','on',' ','va','ri','ab','le','s']) + '!'

%%bash -s "$a" "$b" "$c"
echo "a=$1 b=$2 c=$3"

>>>
a=these b=are positional c=python variables!
```

* f-strings example (Python >=3.6)

```Python
var = 36
print(f'2 times 18 will equal {var}')

>>>
2 times 18 will equal 36
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


---

Matplotlib Path Effects:

For plotting text, matplotlib has a great formatter called ```patheffects``` that can allow for all types of cool text formatting such as text outline, text boxes, etc.

For example creating a black outline for contour labels:

```python
import matplotlib.patheffects as mp
    for text in plt.clabel(wind_contour, colors='r',fmt='%d'):
        text.set_path_effects([mp.withStroke(foreground='k',
                                                       linewidth=3)])
```
Result image:

<img src="https://raw.githubusercontent.com/MethaneRain/Python-Jupyter/master/Tips-Tricks/path_effects_contour_label_example.png">
