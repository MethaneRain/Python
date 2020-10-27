### Pandas are another flexible and easy to use package that will allow exploration and manipulation of data, as well as an interface into Python for plotting and other usage.

___Pandas work in DataFrames___

<i>Pandas Series is a one-dimensional labeled array capable of holding data of any type (integer, string, float, python objects, etc.). The axis labels are collectively called index. <b>Pandas Series is nothing but a column in an excel sheet.</b>

Labels need not be unique but must be a hashable type. <b>The object supports both integer and label-based indexing</b> and provides a host of methods for performing operations involving the index.</i>




~~~Python

~~~

---

Pandas Meteogram Example:
* https://github.com/MethaneRain/Python-Jupyter/blob/master/Pandas/Panda_Meteogram_Example.ipynb

---

Create new dataframe and add some values as well as column headers
```python
df = pd.DataFrame({'name': "COLD",
                       'latitude': list(map(float, lats_cold)),
                       'longitude': list(map(float, lons_cold)),
                  },index=None)

```

Add more data to the existing dataframe
```python
def add_latlon_to_df(df,lats,lons):
    """Add existing set of lat/lon pairs from specific front (Hi/Lo) 
    to the already created pandas dataframe
    
    Parameters
    ----------
    df : pandas.core.frame.DataFrame
        existing dataframe to add new rows
        
    lats : list
        latitudes (must match dimensions of lons)
    
    lons : list
        longitudes (must match dimensions of lats)   
    
    Returns
    -------
    df : pandas.core.frame.DataFrame
        updated dataframe
    """
    for i in range(len(lats)):
        to_append = ["WARM",lats[i],lons[i]]
        to_series = pd.Series(to_append, index = df.columns)
        df = df.append(to_series, ignore_index=True)
    return df
    
    
df = add_latlon_to_df(df,lats_warm,lons_warm)
print(df)

>>>
	name	latitude	longitude
0	COLD	57.5	-58.9
1	COLD	56.3	-58.1
2	COLD	54.5	-58.5
3	COLD	53.1	-59.5
4	COLD	50.8	-61.5
5	COLD	47.6	-63.5
6	COLD	44.9	-66.6
7	COLD	41.4	-70.7
8	COLD	39.1	-73.4
9	WARM	57.5	-58.9
10	WARM	57.1	-55.9
11	WARM	55.8	-52.5
12	WARM	54.5	-50.3
```
