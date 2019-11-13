# Daily-Map-Generator

My longest running project to date is my daily map generator program. As I was teaching myself Python I really needed a large project once I had figured out some basic and intermediate examples. I was really sick of having to open a browser and search through all my tabs to look at all the maps and info, and all the other resources for understanding the weather for the day and near future.

Soooooo, I tried to tackle this using only Python (Jupyter notebooks and Pythons scripts). The project was rather ambitious but I thought there was an achievable way to progress through it.

I knew I was going to need images being scraped off websites, model and sat/radar data plotted in Python, screenshots of websites (working on if these actions could also be web scraped), and folders created, named, and put in proper location on laptop for current date.

I have had several iterations that worked (for the most part), but I have changed and expanded each time. What I want to do this time around is continue this change and expansion and see if there is a more Pythonic or industry favorable approach.

With that said, this iteration I believe I want to make separate packages (individual .py scripts) and run them via
~~~ python
import
~~~
or even maybe via terminal window.

---

Before I get too far into this, here is a (probably incomplete list) of the maps, images, and screenshots I want for this project.
  * These will be downloaded/generated into a newly created folder on my laptop in my weather blog folder. The folder will be named the current date and the program will always check to see if it exists first

Some usual suspects of maps generally to look at when trying to understand the day's weather are:
* Model Runs for 24 hrs out (Currently only using GFS)
  * MSLP and Surface Winds
  * 500mb Heights and Vorticity
  * 250mb Heights and Jets
  * 700mb Temps?
  * Thickness and Surface Highs/Lows (winds??)
  * Precipitable Water
  * 2m Dew Points
  * 24-Hr Precipitation
  * CAPE/CIN and others...
  * Upward Radiative Flux
  * Isentropic Surface - needs fixing
* Satellite
* Radar
* SPC Storm Reports (if applicable)
* WPC Watches and Warnings w/ Legend (screenshot for now)
* Soundings - both simple Metpy version and WPC (if it works)
  * Looking into why Sharppy doesn't have observed in the data for my setup...
* Metars?? (don't have this currently but might be helpful)
* ...

---
