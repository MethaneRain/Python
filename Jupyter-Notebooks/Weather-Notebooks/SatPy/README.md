My first attempt at using the SatPy package. This is a powerful tool that injests satellite data and create the various composite images!

```python
# Need to have channel 1, 2, and 3 data files in path
scn = Scene(reader='abi_l1b', filenames=glob.glob('*M3C0*.nc'))

scn.load(['true_color'])
 
new_scn = scn.resample(scn.min_area(), resampler='native')
new_scn.save_dataset('true_color', filename='true_color'+'.png')
```

<img src="https://github.com/MethaneRain/Weather-Jupyter-Notebooks/blob/master/SatPy/Sample-Images/Resized_true_color.png">
