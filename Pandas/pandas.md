The Pandas package is extremely helpful, but it also has many methods that can come in handy when working with dataframes.

Several data file types can be used with Pandas:
* csv
* json
* excel
* html
* sql
* etc.

---

## Let's take a look at a sample ```csv``` file of weather data:

~~~python
import pandas as import pd
weather = pd.read_csv("weather.csv")
print(type(weather))

>>>
pandas.core.frame.DataFrame
~~~
~~~python
print(weather)

>>>
Day	MxT	MnT	AvT	AvDP	1HrP TPcpn	PDir	AvSp	Dir	MxS	SkyC	MxR	Mn	R AvSLP
0	1	88	59	74	53.8	0	280	9.6	270	17	1.6	93	23	1004.5
1	2	79	63	71	46.5	0	330	8.7	340	23	3.3	70	28	1004.5
2	3	77	55	66	39.6	0	350	5.0	350	9	2.8	59	24	1016.8
3	4	77	59	68	51.1	0	110	9.1	130	12	8.6	62	40	1021.1
4	5	90	66	78	68.3	0	220	8.3	260	12	6.9	84	55	1014.4
5	6	81	61	71	63.7	0	30	6.2	30	13	9.7	93	60	1012.7
6	7	73	57	65	53.0	0	50	9.5	50	17	5.3	90	48	1021.8
7	8	75	54	65	50.0	0	160	4.2	150	10	2.6	93	41	1026.3
8	9	86	32	59	61.5	0	240	7.6	220	12	6.0	78	46	1018.6
9	10	84	64	74	57.5	0	210	6.6	50	9	3.4	84	40	1019.0
10	11	91	59	75	66.3	0	250	7.1	230	12	2.5	93	45	1012.6
11	12	88	73	81	68.7	0	250	8.1	270	21	7.9	94	51	1007.0
12	13	70	59	65	55.0	0	150	3.0	150	8	10.0	83	59	1012.6
13	14	61	59	60	55.9	0	60	6.7	80	9	10.0	93	87	1008.6
14	15	64	55	60	54.9	0	40	4.3	200	7	9.6	96	70	1006.1
15	16	79	59	69	56.7	0	250	7.6	240	21	7.8	87	44	1007.0
16	17	81	57	69	51.7	0	260	9.1	270	29	5.2	90	34	1012.5
17	18	82	52	67	52.6	0	230	4.0	190	12	5.0	93	34	1021.3
18	19	81	61	71	58.9	0	250	5.2	230	12	5.3	87	44	1028.5
19	20	84	57	71	58.9	0	150	6.3	160	13	3.6	90	43	1032.5
20	21	86	59	73	57.7	0	240	6.1	250	12	1.0	87	35	1030.7
21	22	90	64	77	61.1	0	250	6.4	230	9	0.2	78	38	1026.4
22	23	90	68	79	63.1	0	240	8.3	230	12	0.2	68	42	1021.3
23	24	90	77	84	67.5	0	350	8.5	10	14	6.9	74	48	1018.2
24	25	90	72	81	61.3	0	190	4.9	230	9	5.6	81	29	1019.6
25	26	97	64	81	70.4	0	50	5.1	200	12	4.0	107	45	1014.9
26	27	91	72	82	69.7	0	250	12.1	230	17	7.1	90	47	1009.0
27	28	84	68	76	65.6	0	280	7.6	340	16	7.0	100	51	1011.0
28	29	88	66	77	59.7	0	40	5.4	20	9	5.3	84	33	1020.6
29	30	90	45	68	63.6	0	240	6.0	220	17	4.8	200	41	1022.7
~~~

---

Pandas can parse the data into columns if necessary and can be transposed also.

~~~python
weather.columns

>>>
Index(['Day', 'MxT', 'MnT', 'AvT', 'AvDP', '1HrP TPcpn', 'PDir', 'AvSp', 'Dir',
       'MxS', 'SkyC', 'MxR', 'Mn', 'R AvSLP'],
      dtype='object')
~~~

---

Sweet, now we can get an idea of the column names that we might be interested in working with. Say the Average MSLP data is of interest to us. We can pull just that column now that we can access the column by name.

This can be achieved by index method ```weather["R AvSLP"]```

~~~Python
weather["R AvSLP"]

>>>
0     1004.5
1     1004.5
2     1016.8
3     1021.1
4     1014.4
5     1012.7
6     1021.8
7     1026.3
8     1018.6
9     1019.0
10    1012.6
11    1007.0
12    1012.6
13    1008.6
14    1006.1
15    1007.0
16    1012.5
17    1021.3
18    1028.5
19    1032.5
20    1030.7
21    1026.4
22    1021.3
23    1018.2
24    1019.6
25    1014.9
26    1009.0
27    1011.0
28    1020.6
29    1022.7
Name: R AvSLP, dtype: float64
~~~

---

We can assign this to a Pandas Series object which is similar to a native list or an array.

Check out the docs for the Series data type here:
* https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html

~~~Python
slp = weather["R AvSLP"]
type(slp)

>>>
pandas.core.series.Series
~~~

---

Grabbing the columns is great if you want the values for a specific variable, but suppose you're more interested in the all the variables for a specific row (Day number in our case here).

Unfortunately Pandas don't have a rows method like the columns, but as hinted at earlier, the data can be transposed. This will swap rows and columns.

~~~python
weatherT = weather.T
print(weatherT)

>>>
0	1	2	3	4	5	6	7	8	9	...	20	21	22	23	24	25	26	27	28	29
Day	1.0	2.0	3.0	4.0	5.0	6.0	7.0	8.0	9.0	10.0	...	21.0	22.0	23.0	24.0	25.0	26.0	27.0	28.0	29.0	30.0
MxT	88.0	79.0	77.0	77.0	90.0	81.0	73.0	75.0	86.0	84.0	...	86.0	90.0	90.0	90.0	90.0	97.0	91.0	84.0	88.0	90.0
MnT	59.0	63.0	55.0	59.0	66.0	61.0	57.0	54.0	32.0	64.0	...	59.0	64.0	68.0	77.0	72.0	64.0	72.0	68.0	66.0	45.0
AvT	74.0	71.0	66.0	68.0	78.0	71.0	65.0	65.0	59.0	74.0	...	73.0	77.0	79.0	84.0	81.0	81.0	82.0	76.0	77.0	68.0
AvDP	53.8	46.5	39.6	51.1	68.3	63.7	53.0	50.0	61.5	57.5	...	57.7	61.1	63.1	67.5	61.3	70.4	69.7	65.6	59.7	63.6
1HrP TPcpn	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	...	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0
PDir	280.0	330.0	350.0	110.0	220.0	30.0	50.0	160.0	240.0	210.0	...	240.0	250.0	240.0	350.0	190.0	50.0	250.0	280.0	40.0	240.0
AvSp	9.6	8.7	5.0	9.1	8.3	6.2	9.5	4.2	7.6	6.6	...	6.1	6.4	8.3	8.5	4.9	5.1	12.1	7.6	5.4	6.0
Dir	270.0	340.0	350.0	130.0	260.0	30.0	50.0	150.0	220.0	50.0	...	250.0	230.0	230.0	10.0	230.0	200.0	230.0	340.0	20.0	220.0
MxS	17.0	23.0	9.0	12.0	12.0	13.0	17.0	10.0	12.0	9.0	...	12.0	9.0	12.0	14.0	9.0	12.0	17.0	16.0	9.0	17.0
SkyC	1.6	3.3	2.8	8.6	6.9	9.7	5.3	2.6	6.0	3.4	...	1.0	0.2	0.2	6.9	5.6	4.0	7.1	7.0	5.3	4.8
MxR	93.0	70.0	59.0	62.0	84.0	93.0	90.0	93.0	78.0	84.0	...	87.0	78.0	68.0	74.0	81.0	107.0	90.0	100.0	84.0	200.0
Mn	23.0	28.0	24.0	40.0	55.0	60.0	48.0	41.0	46.0	40.0	...	35.0	38.0	42.0	48.0	29.0	45.0	47.0	51.0	33.0	41.0
R AvSLP	1004.5	1004.5	1016.8	1021.1	1014.4	1012.7	1021.8	1026.3	1018.6	1019.0	...	1030.7	1026.4	1021.3	1018.2	1019.6	1014.9	1009.0	1011.0	1020.6	1022.7
~~~~

---

Now the object can be called like an index for a list. Let's take a look at all the variables for Day 1 (index number 0):

~~~Python
weatherT[0]

>>>
Day              1.0
MxT             88.0
MnT             59.0
AvT             74.0
AvDP            53.8
1HrP TPcpn       0.0
PDir           280.0
AvSp             9.6
Dir            270.0
MxS             17.0
SkyC             1.6
MxR             93.0
Mn              23.0
R AvSLP       1004.5
Name: 0, dtype: float64
~~~

---

We can dive deeper into the flexibility of Pandas

How about trying to find how many times the average MSLP was, say 1004.5 hPa. Pandas can do it!

First, we need to locate in the data where the value of 1004.5 exist. The ```.loc``` will be our guide.

~~~python
weather.loc?

>>>
Type:        property
String form: <property object at 0x1211c7688>
Docstring:  
Access a group of rows and columns by label(s) or a boolean array.

``.loc[]`` is primarily label based, but may also be used with a
boolean array.

Allowed inputs are:

- A single label, e.g. ``5`` or ``'a'``, (note that ``5`` is
  interpreted as a *label* of the index, and **never** as an
  integer position along the index).
- A list or array of labels, e.g. ``['a', 'b', 'c']``.
- A slice object with labels, e.g. ``'a':'f'``.

  .. warning:: Note that contrary to usual python slices, **both** the
      start and the stop are included

- A boolean array of the same length as the axis being sliced,
  e.g. ``[True, False, True]``.
- A ``callable`` function with one argument (the calling Series, DataFrame
  or Panel) and that returns valid output for indexing (one of the above)

See more at :ref:`Selection by Label <indexing.label>`

Raises
------
KeyError:
    when any items are not found

See Also
--------
DataFrame.at : Access a single value for a row/column label pair.
DataFrame.iloc : Access group of rows and columns by integer position(s).
DataFrame.xs : Returns a cross-section (row(s) or column(s)) from the
    Series/DataFrame.
Series.loc : Access group of values using labels.

~~~~

So we just need to pass the variable name and the value we're looking for:

~~~python
weather.loc[weather["R AvSLP"] == 1004.5]

>>>
Day	MxT	MnT	AvT	AvDP	1HrP TPcpn	PDir	AvSp	Dir	MxS	SkyC	MxR	Mn	R AvSLP
0	1	88	59	74	53.8	0	280	9.6	270	17	1.6	93	23	1004.5
1	2	79	63	71	46.5	0	330	8.7	340	23	3.3	70	28	1004.5
~~~

This call grabs the entire row where the MSLP is 1004.5

The last piece we need is the ```.count``` method to get total it up for us:

~~~python
weather.loc[weather["R AvSLP"] == 1004.5].count()

>>>
Day           2
MxT           2
MnT           2
AvT           2
AvDP          2
1HrP TPcpn    2
PDir          2
AvSp          2
Dir           2
MxS           2
SkyC          2
MxR           2
Mn            2
R AvSLP       2
~~~

OK, a little redundant because we know the variable total will be 2 for each of the 2 times MSLP is 1004.5. We can clean it up a tad bit by invoking an additional call in the ```loc``` method.

However if we want the Day number associated with these values, we can add the variable name as well

~~~python
weather.loc[weather["R AvSLP"] == 1004.5, "Day"]

>>>
0    1
1    2
Name: Day, dtype: int64
~~~

If we add the variable ```R AvSLP``` name as well, it will count the number of times 1004.5 is in the ```R AvSLP``` variable.

~~~Python
weather.loc[weather["R AvSLP"] == 1004.5, "R AvSLP"].count()

>>>
2
~~~

---

We can also manipulate the data of columns to create new columns. We can make a copy of the data so we don't ruin our original data set:

~~~Python
df = weather.copy()
~~~

Let's just make a new column for the difference of high and low temperature for each day. Call the new variable ```DiffT```

~~~python
df["DiffT"] = df.MxT-df.MnT
~~~

The beautiful thing about working with Pandas is that we don't have to iterate over all rows like we would for a list!

Check out the new column data:

~~~Python
df["DiffT"]

>>>
0     29
1     16
2     22
3     18
4     24
5     20
6     16
7     21
8     54
9     20
10    32
11    15
12    11
13     2
14     9
15    20
16    24
17    30
18    20
19    27
20    27
21    26
22    22
23    13
24    18
25    33
26    19
27    16
28    22
29    45
Name: DiffT, dtype: int64
~~~
---
---

## Taking a break from working with actual data, we can play around a bit with populating data frames with our own data. This is obviously a very helpful skill if you plan on using Pandas further.

Panda Series is a powerful data structure, it has some draw backs: you can only store one attribute for each key. If we turn our attention to Pandas DataFrame (which was the data structure of our weather data above), we can be more flexible in the data that is stored. DataFrames are essentially a sequence of Series objects.

---

I will make a new DataFrame based off some meteorology courses I've taken. I want the name of the course to be the column headers (variables) and each row to be associated with the grade received, professor, and university I took it at.

~~~Python
met_courses = pd.DataFrame(
    index=["Grade","Prof","School"],
    data=[["A","A","A","B"],["Wagner","Schuenemann","Cassano","Ng"],["MSU","MSU","CU","MSU"]],
    columns=["Intro to Meteorology", "Advanced Synoptic", "Dynamics","Meso"])
print(met_courses)

>>>
Intro to Meteorology	Advanced Synoptic	Dynamics	Meso
Grade	A	A	A	B
Prof	Wagner	Schuenemann	Cassano	Ng
School	MSU	MSU	CU	MSU
~~~



