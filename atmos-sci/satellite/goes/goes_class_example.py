#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 19:32:40 2020

@author: Justin Richling

Simple plotting of GOES netCDF data for various channels and products
"""

class GoesImages:
    """
    class to quickly plot many GOES images and/or derived products
    """
    def __init__(self):
        '''
        --------------
        Initial values
        --------------
        
        Default values
        
        * image save path -> cwd
        * extent -> CONUS
        '''
        # current working drive for saved images
        self.im_save_path = "./"
        
        # map lat/lon extent
        self.extent = [-130., -70, 20., 60.]
        
        
    def get_julian_number(self,date_time):
        from datetime import datetime
        """
        ------------------------------------
        Grab Julian day number from datetime
        ------------------------------------
        Turn date time into necessary Julian day for nc file nomenclature
        
        example:
        --------
        get_julian_number(datetime(2020, 4, 25))
        
        >>>
        2020-04-25 00:00:00
        date: 2020-04-25 0004Z
        Julian number: 116
        
        """
        # Set the date you want to convert
        print(date_time)
        # Start of year for reference
        d0 = datetime(date_time.year, 1, 1)
    
        # Find the difference and add one to get the day number of the calander year
        delta = date_time - d0
        Julian_Day = delta.days+1
        if Julian_Day < 100:
            Julian_Day = "0"+str(Julian_Day)
            if int(Julian_Day) < 10:
                Julian_Day = "0"+str(Julian_Day)
    
        print(f"Julian number: {Julian_Day}")
        self.Julian_Day = Julian_Day

    def grab_goes_files(self,GOES_file_path,ch):
        """
        -----------------------------------
        Make list of all available nc files
        -----------------------------------
        
        Args:
        -----
        * GOES_file_path: path to nc files
        * ch (str): GOES channel number (must have leading zero for 1-9)
        
        
        
        """
        
        import glob
        GOES_files = sorted([name for name in glob.glob(GOES_file_path+f'/*CMIPC*M6C{ch}*.nc')])
 
        print(f"Number of files in path: {len(GOES_files)}")
        #print(GOES_files[0])
        self.ch = ch
        self.GOES_files = GOES_files
        
    def make_text_time_right(self,ax,title_time,
                         color="w",
                       fontsize=12):  
        from matplotlib import patheffects
    
        text_time = ax.text(.995, 0.01, 
                title_time,
                horizontalalignment='right', transform=ax.transAxes,
                color=color, fontsize=fontsize, weight='bold',zorder=15)
        outline_effect = [patheffects.withStroke(linewidth=5, foreground='black')]
        text_time.set_path_effects(outline_effect)
        self.text_time = text_time
        self.ax = ax
        self.outline_effect = outline_effect
    
    def make_text_time_left(self,ax,station, prod_name,product,
                            color="w",
                           fontsize=12):  
        #from matplotlib import patheffects
        
        text_time2 = ax.text(0.005, 0.01, 
                    "Station: "+station+"\n"+prod_name+" ("+product+")",
                    horizontalalignment='left', transform=ax.transAxes,
                    color=color, fontsize=fontsize, weight='bold',zorder=15)
        outline_effect = [self.patheffects.withStroke(linewidth=5, foreground='black')]
        text_time2.set_path_effects(outline_effect)
        self.text_time2 = text_time2
        self.ax = ax
    
    def get_sat_data(self,GOES_file):
        from netCDF4 import Dataset
        from datetime import datetime
        nc = Dataset(GOES_file)
        file_data = nc.variables['CMI']
        var_data = nc.variables['CMI'][:]
        #def rebin(a, shape):
        #    sh = shape[0],a.shape[0]//shape[0],shape[1],a.shape[1]//shape[1]
        #    return a.reshape(sh).mean(-1).mean(1)
        #if self.ch == "02":
        #    var_data = rebin(var_data, [3000, 5000])
            
        proj_var = nc.variables['goes_imager_projection']
        sat_h = nc.variables['goes_imager_projection'].perspective_point_height
        semi_major_axis = proj_var.semi_major_axis
        semi_minor_axis = proj_var.semi_minor_axis
        central_lon = proj_var.longitude_of_projection_origin
    
        Time = str(datetime.strptime(nc.time_coverage_start[:-6], '%Y-%m-%dT%H:%M'))
        Time = Time[0:10]+Time[11:16]
        timestamp = datetime.strptime(Time, '%Y-%m-%d%H:%M')
        file_time = timestamp.strftime('%Y_%m_%d_%H%M')
        title_time = timestamp.strftime('%d %B %Y %H:%MZ')
        
        X = nc.variables['x'][:] * sat_h
        Y = nc.variables['y'][:] * sat_h
        
        self.X = X
        self.Y = Y
        self.title_time = title_time
        self.file_time = file_time
        self.file_data = file_data
        self.var_data = var_data
        self.proj_var = proj_var
        self.sat_h = sat_h
        self.semi_major_axis = semi_major_axis
        self.semi_minor_axis = semi_minor_axis
        self.central_lon = central_lon
        self.nc = nc
        
        nc.close()
        nc = None
        
    def get_product_cbar_args(self):
        import numpy as np
        if self.ch == "13":
            ticks = np.arange(170,331,40)
           
        if self.ch == "02":
            #ticks = np.arange(20,121,20)
            ticks = []
            
        self.ticks = ticks
        
    def get_goes_projection(self):
        """
        ----------------------------------------------
        Use SatPy to grab GOES projection for plotting
        ----------------------------------------------
        
        SatPy has a built-in function to get the most appropriate CRS for GOES
        
        """
        import glob
        from satpy import Scene
        from satpy.writers import get_enhanced_image
        filename = glob.glob("/Users/chowdahead/Downloads/WX_Data/GOES_Data/*L1b*")
        scn = Scene(reader='abi_l1b', filenames=filename)
        product= f"C{self.ch}"
        scn.load([product])
           
        #new_scn = scn.resample(resampler='native') #scn.min_area(),
        new_scn = scn.resample(resampler='native') #scn.min_area()
        var = get_enhanced_image(new_scn[product]).data
        
        # data needs switching around the axes for matplotlib
        var = var.transpose('y', 'x', 'bands')
        
        # get the native projection to a CartoPy CRS
        abi_crs = var.attrs['area'].to_cartopy_crs()
        self.abi_crs = abi_crs
    
    def plot_goes(self,GOES_file,savepath,extent,my_cmap=None,vmin=None,vmax=None,show=False):
        """
        --------------
        Plot GOES Data
        --------------
        
        Args:
        -----
        * GOES_file: GOES nc file
        * savepath: path for saved images
        * extent: plot lat/lon extent
        * my_cmap: colormap (default none)
        * vmin: lpotting min limit (default none)
        * vmax: plotting max limit (default none)
        * show: show figure (default False)
        """
        import matplotlib.pyplot as plt
        import cartopy.crs as ccrs
        import cartopy.feature as cfeature
        from matplotlib import patheffects
        
        self.get_sat_data(GOES_file)
        
    # Create new figure
        fig = plt.figure(figsize=(17,11))
    
    # Add state boundaries to plot
        states_boundaries = cfeature.NaturalEarthFeature(category='cultural',
            name='admin_1_states_provinces_lakes',scale='50m', facecolor='none')
    
        country_borders = cfeature.NaturalEarthFeature(category='cultural',
            name='admin_0_countries',scale='50m', facecolor='none')
        
        crs =self.abi_crs
    
    # Add the map and set the extent
        ax = plt.subplot(111, projection=crs) 
        
        def plot_us_counties(self,ax):
            import cartopy.io.shapereader as shpreader
            import cartopy.feature as cfeature
            reader = shpreader.Reader('/Users/chowdahead/Documents/shapefiles/countyl010g_shp_nt00964/countyl010g.shp')
            counties = list(reader.geometries())
            COUNTIES = cfeature.ShapelyFeature(counties,ccrs.PlateCarree())
            ax.add_feature(COUNTIES, facecolor='none',edgecolor='r')
            return
            
    # Find and convert Julian day to date    
        
    # Set the plot legend
        self.make_text_time_right(ax,self.title_time,
                             color="w",
                           fontsize=12)    
        
    # Add state boundaries to plot
        ax.add_feature(states_boundaries, edgecolor='blue', linewidth=1)
    
    # Add country borders to plot
        ax.add_feature(country_borders, edgecolor='black', linewidth=1)
    
    # Set the plotting extent    
      
        ax.set_extent(extent,ccrs.PlateCarree())
    
        #ax.gridlines(color="w", linestyle="dotted",alpha=0.5)
        X = self.X
        Y = self.Y
        
        im = plt.imshow(self.var_data,origin='upper',
                        extent=(X.min(), X.max(), Y.min(), Y.max()),
                        interpolation='nearest',
                        vmin=vmin,vmax=vmax,
                        cmap=my_cmap, 
                        transform=crs) 
        
        cbar = plt.colorbar(im,orientation="horizontal") #,ticks=ticks
        self.cbar = cbar
        posn = ax.get_position()
        cbar.ax.set_position([posn.x0+0.001, posn.y0-0.001,
                                (posn.x1-posn.x0)/2, posn.height])
        
        outline_effect = [patheffects.withStroke(linewidth=3, foreground='black')]
        Y = 240    
        for count,ele in enumerate(self.ticks,0): 
            cbar.ax.text(ele, Y, self.ticks[count], 
                         ha='center', va='center',
                         path_effects=outline_effect,
                         color="w",
                         fontsize=6)
        
        cbar.set_ticks([])
        cbar.ax.set_xticklabels([])
        
    # Display the figure
        if show == True:
            plt.show()
        
    # Set the name for saved figure, and save it 
        outfile = f"{self.file_time}_goes_ch{self.ch}.png"
            
        fig.savefig(f"{self.im_save_path}{outfile}",bbox_inches="tight",dpi=200)