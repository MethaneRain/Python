#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 15:55:53 2020

@author: Justin Richling

Using classes to approach retreiving and plotting model data from the THREDDS server.

This is my attempt at simplifying grabbing data and plotting from the thredds server
Please credit my work if used

"""

class THREDDS_Models:
    '''
    Class to gather model data from the THREDDS server and plot variables
    
    * Credit to UCAR, Unidata, MetPy, and all hard working devs!!
    
    * Reference Catalog: http://thredds-jetstream.unidata.ucar.edu/thredds/idd/forecastModels.html
        - Good for roughly a couple of days current data
    
    !* As of Jan 22, 2020 only RAP products are included, stay tuned for further additions *!
    
    Methods:
    ---------
        * __init__
            args:
            * initialization hour
            
        * change_run_time
            args:
            * year, month, day
            
        * change_im_save_path
            args:
            * image save path
            
        * get_var_info
            args:
            * model
            * prod
        
        * get_model_data
            Access the THREDDS server for query of variables
            args:
            * model -> name (abbr.)
            * prod 
            * *argv flexible number of variables
            
        * get_time
            args:
            * data -> from get_model_data() return
            
        * change_map_attrs:
            args:
            * extent
            * cmap=None
            * clevs=None
            * colors=None
        
        * make_map
            args:
            * data
            * time_index
            * lats
            * lons 
            * time_strings
            * time_final
            * font
            * model
            * title_prod
            * filename_var
            * contours=True
            
    '''
    
    model_dict = {"Model:{Product:url extension}":"",
                  "RAP":{"13km":"CONUS_13km/RR_CONUS_13km",
                     "20km":"CONUS_20km/RR_CONUS_20km",
                     "40km":"CONUS_40km/RR_CONUS_40km"},
              
              "GFS":{"0p25_ana":"Global_0p25deg_ana/GFS_Global_0p25deg_ana",
                     "0p25":"Global_0p25deg/GFS_Global_0p25deg",
                     "0p5_ana":"Global_0p5deg_ana/GFS_Global_0p5deg_ana",
                     "0p5":"Global_0p5deg/GFS_Global_0p5deg",
                     "onedeg_ana":"Global_onedeg_ana/GFS_Global_onedeg_ana",
                     "onedeg":"Global_onedeg/GFS_Global_onedeg",
                     "Pac_20km":"Pacific_20km/GFS_Pacific_20km",
                     "PR_0p25":"Puerto_Rico_0p25deg/GFS_Puerto_Rico_0p25deg",
                     "CONUS_95km":"CONUS_95km/GFS_CONUS_95km",
                     "CONUS_80km":"CONUS_80km/GFS_CONUS_80km",
                     "CONUS_20km":"CONUS_20km/GFS_CONUS_20km",
                     "AK_20km":"Alaska_20km/GFS_Alaska_20km"},
              
              "HRRR":{"CONUS_3km":"CONUS_3km/surface/HRRR_CONUS_3km",
                      "CONUS_2p5km_ana":"CONUS_2p5km_ANA/HRRR_CONUS_2p5km_ana",
                      "CONUS_2p5km":"CONUS_2p5km/HRRR_CONUS_2p5km"},
              
              "GEFS":{"onedeg_ana":"Global_1p0deg_Ensemble/members-analysis/GEFS_Global_1p0deg_Ensemble_ana",
                  "onedeg":"Global_1p0deg_Ensemble/members/GEFS_Global_1p0deg_Ensemble",
                  "onedeg_derived":"Global_1p0deg_Ensemble/derived/GEFS_Global_1p0deg_Ensemble_derived"}
              }
    
    
    def __init__(self):
        '''
        Default values
        
        * date -> current date
        * initialization hour -> 0000Z
        * image save path -> cwd
        * countour levels -> 100
        * extent -> CONUS
        * contour color -> black
        '''
        from datetime import datetime
        now = datetime.utcnow()
        self.today_day = int('{0:%d}'.format(now))
        self.today_year = int('{0:%Y}'.format(now))
        self.today_month = int('{0:%m}'.format(now))
        print(self.today_day,self.today_year,self.today_month)
        
        # initialization hour for model forecast
        self.init_hour = "0000"
        
        # current working drive for saved images
        self.im_save_path = "./"
        
        # 
        self.arg = ""
        
        # contour levels for plotting
        self.clevs = 100
        
        # map lat/lon extent
        self.extent = [-130., -70, 20., 60.]
        
        # plot contour line color
        self.colors = "k"
        
        self.cmap = "jet"
    
    model_filename_prod_dict = {"RAP":{"13km":"CONUS_13km",
                                   "20km":"CONUS_20km",
                                   "40km":"CONUS_40km"},
                            
                            "GFS":{"0p25_ana":"Global_0p25deg_ana",
                                    "0p25":"Global_0p25deg",
                                    "0p5_ana":"Global_0p5deg_ana",
                                    "0p5":"Global_0p5deg",
                                    "onedeg_ana":"Global_onedeg_ana",
                                    "onedeg":"Global_onedeg",
                                    "Pac_20km":"Pacific_20km",
                                    "PR_0p25":"Puerto_Rico_0p25deg",
                                    "CONUS_95km":"CONUS_95km",
                                    "CONUS_80km":"CONUS_80km",
                                    "CONUS_20km":"CONUS_20km",
                                    "AK_20km":"Alaska_20km"},
                            
                            "HRRR":{"CONUS_3km":"CONUS_3km",
                                    "CONUS_2p5km_ana":"CONUS_2p5km_ana",
                                    "CONUS_2p5km":"CONUS_2p5km"},
                            
                            "GEFS":{"onedeg_ana":"Global_1p0deg_Ensemble_ana",
                                    "onedeg":"Global_1p0deg_Ensemble",
                                    "onedeg_derived":"Global_1p0deg_Ensemble"}
                           }
    
    def change_run_time(self,year,month,day,init_hour):
        '''
        Change the queued date for data
        -------------------------------
        '''
        from datetime import datetime
        now = datetime(year,month,day)
        #now = datetime(year,month,day,int(self.init_hour[0:2]))
        self.today_day = int('{0:%d}'.format(now))
        self.today_year = int('{0:%Y}'.format(now))
        self.today_month = int('{0:%m}'.format(now))
        self.init_hour = init_hour
        print(self.today_day,self.today_year,self.today_month)
        
    
    def change_im_save_path(self,im_save_path):
        '''
        Change where the image is saved
        -------------------------------
        
        '''
        import os
        
        # Check to see if the folder already exists, if not create it
        if not os.path.isdir(im_save_path):
            os.makedirs(im_save_path)
        self.im_save_path = im_save_path
        #return im_save_path
    
    def get_var_info(self,model,prod):
        '''
        Reference for specific variable names needed for queue.
        
        Opens new browser tab with NCSS variables for desired model and product
        -----------------------------------------------------------------------
        
        See model_dict() method for help
        
        Ex args:
            Model -> RAP (Rapid Refresh)
            Product -> 13km (13km CONUS)
        '''
        import webbrowser 
        cat_1 = "http://thredds-jetstream.unidata.ucar.edu/thredds/ncss/grib/NCEP/"
        cat_2 = f"{model}/{self.model_dict[model][prod]}_{self.today_year}{self.today_month:02d}{self.today_day:02d}_{self.init_hour}.grib2/dataset.html"
        catalog = cat_1+cat_2
        print(catalog)
        webbrowser.open(catalog)
        
    
    def get_model_data(self,model,prod,*argv,latlon=None):
        '''
        Queue data from given datasets
        ------------------------------
        Arguments:
            * init_hour
            * model
            * prod
            * args - felxible number of plotting variables
            * latlon (optional) - [west,east,south,north]
                defaults to north=60, south=20, east=310, west=230
        
        Returns:
            * Data        
        '''
       
        print(self.init_hour)
        from datetime import datetime, timedelta
        
        # Accessing Data from XLM Catalog via Siphon Libraries
        from siphon.ncss import NCSS
        from siphon.catalog import TDSCatalog
 
        for arg in argv:  
            print (arg)
            
        
        
        # Grab all the variables that get passed for queue
        var_list = [i for i in argv]
        
        
        cat_1 = "http://thredds-jetstream.unidata.ucar.edu/thredds/catalog/grib/NCEP/"
        cat_2 = f"{model}/{self.model_dict[model][prod]}_{self.today_year}{self.today_month:02d}{self.today_day:02d}_{self.init_hour}.grib2/catalog.xml"
        
        catalog = TDSCatalog(cat_1+cat_2)
        
        file_time_string = str(catalog)[-19:-6]
        file_time = f"{file_time_string[0:4]}_{file_time_string[4:6]}_{file_time_string[6:8]}_{file_time_string[9:13]}Z"
        init_date_title = file_time[0:-6].replace("_","-")
        init_hour_title = f"{file_time_string[9:11]}:{file_time_string[11:13]}Z"
       
        self.file_time = file_time
        self.init_date_title = init_date_title
        self.init_hour_title = init_hour_title
        #self.init_hour = init_hour
        
        dataset = list(catalog.datasets.values())[0]
        
        # Create NCSS object to access the NetcdfSubset
        ncss = NCSS(dataset.access_urls['NetcdfSubset'])
        
        # get current date and time
        now = datetime(self.today_year,self.today_month,self.today_day,int(self.init_hour[0:2]))
        
        # define time range you want the data for
        print(now)
        delta_t = 48
        end = now + timedelta(hours=delta_t)
        
        query = ncss.query()
        query.time_range(now, end)
        
        if latlon != None:
            north = latlon[3]
            south = latlon[2]
            east = latlon[1]
            west = latlon[0]
        else:
            north = 60
            south = 20
            east = -70#310
            west = -120#230
            
        print(north,south,east,west)
        query.lonlat_box(north=north, south=south, east=east, west=west)
        #query.lonlat_box(north=60, south=20, east=310, west=230)
        query.accept('netcdf4')
        
        for i in var_list:
            query.variables(i).add_lonlat(True)

        # Request data for the variables you want to use
        data = ncss.get_data(query)
        
        print("Data grab complete!")
       
        self.arg = arg
        self.model = model
        self.title_prod = self.model_filename_prod_dict[model][prod]
        return data

    def get_time(self,data):
        '''
        *! Need to run the get_model_data() method first !*
        
        Grabs actual time stamps for data
        
        Returns: time_strings,time_var,time_final 
        '''
        # NetCDF Libraries
        from netCDF4 import num2date
            
        def find_time_var(var, time_basename='time'):
            for coord_name in var.coordinates.split():
                if coord_name.startswith(time_basename):
                    return coord_name
            raise ValueError('No time variable found for ' + var.name)
        # Get time into a datetime object
        time_var = data.variables[find_time_var(data.variables[self.arg])]
        time_var = num2date(time_var[:], time_var.units).tolist()
        time_strings = [t.strftime('%m/%d %H:%M') for t in time_var]

        self.time_strings = time_strings
        
        time_var = data.variables[find_time_var(data.variables[self.arg])]
        time_final = num2date(time_var[:].squeeze(), time_var.units)
        
        return time_var,time_final 
    
    
    def change_map_attrs(self,extent=None,cmap=None,clevs=None,colors=None):
        self.cmap = cmap
        self.clevs = clevs
        self.colors = colors
        self.extent = extent
        print(extent)
        
    
    def precip_time_info():
        '''
        Correcting the F hour for precip products
        In the models, there is a lag for precip data
        ---------------------------------------------
        
        This is a dictionary reference based off model and
        precip preoduct. As of now, it is just for GFS until I scale up
        
        GFS is 3-hours off init hour for precip products
        
        
        '''
        model_F_hr_offset = {"GFS":{"CONUS_20km":["Categorical_Rain_surface_Mixed_intervals_Average",
                              "Pressure_middle_cloud_bottom_Mixed_intervals_Average",
                              "Convective_precipitation_surface_Mixed_intervals_Accumulation",
                              "Categorical_Snow_surface_Mixed_intervals_Average",
                              "Categorical_Ice_Pellets_surface_Mixed_intervals_Average",
                              "Pressure_high_cloud_bottom_Mixed_intervals_Average",
                              "Total_precipitation_surface_Mixed_intervals_Accumulation",
                              "Categorical_Freezing_Rain_surface_Mixed_intervals_Average",
                              "Pressure_low_cloud_bottom_Mixed_intervals_Average"]}}
        return model_F_hr_offset
    
    def make_map(self,var_data,time_index,lats,lons,font,
                 variable,
                 filename_var,
                 contourfill=True,
                 level=None):
        '''
        Plotting method for the THREDDS model data!
        -------------------------------------------
        
        Arguments:
            * var_data - variable data to plot ie mslp
            * time_index - time step index for variable ie 0,1,2, etc.
            * lats/lons - latitude and longitude variable from dataset
            * font - dictionary for font attributes for plots and labels
            * variable - string name of variable plotting, used for title
            * filename_var - string value for variable used for filename
            * contour_fill - plots filled contours when assigned True
            
        -------------------------------------------
        There is still a lot to be done in commenting and cleaning up this method.
        Please stay tuned! 
        '''
        import cartopy.crs as ccrs
        import matplotlib.pyplot as plt
        from metpy.plots import add_metpy_logo
        import cartopy.feature as cfeature
        
        # Set Projection of Data
        datacrs = ccrs.PlateCarree()

        # Set Projection of Plot
        plotcrs = ccrs.LambertConformal(central_latitude=[30, 60], central_longitude=-100)

        # Colorbar Axis Placement (under figure)
        colorbar_axis = [0.183, 0.09, 0.659, 0.03] # [left, bottom, width, height]

        # Lat/Lon Extents [lon0,lon1,lat0,lat1]
        
        
                                         # Setup Contour Label Options
    #---------------------------------------------------------------------------------------------------    
        kw_clabels = {'fontsize': 11, 'inline': True, 'inline_spacing': 5, 'fmt': '%i',
                  'rightside_up': True, 'use_clabeltext': True}

                                         # Setup Figure
    #---------------------------------------------------------------------------------------------------    
        fig = plt.figure(figsize=(17., 11.))

        add_metpy_logo(fig, 25, 950, size='small')

                                         # Add the Map 
    #---------------------------------------------------------------------------------------------------
        ax = plt.subplot(111, projection=plotcrs)

    # Set extent and plot map lines
        print(self.extent)
        ax.set_extent(self.extent, datacrs)

        ax.coastlines(resolution='50m')

                                          # Add State/Country Boundaries to Plot
    #---------------------------------------------------------------------------------------------------    
        state_borders = cfeature.NaturalEarthFeature(
                    category='cultural', name='admin_1_states_provinces_lines',
                    scale='50m', facecolor='none')
        ax.add_feature(state_borders, edgecolor='b', linewidth=1, zorder=3)

        country_borders = cfeature.NaturalEarthFeature(category='cultural',
                    name='admin_0_countries',scale='50m', facecolor='none')
        ax.add_feature(country_borders,edgecolor='b',linewidth=0.2)


                                          # File and Title Times
    #---------------------------------------------------------------------------------------------------
       
        if self.model == "RAP":
            time_step = time_index
            
        if self.model == "GFS":
            time_step = time_index*3
            
        if self.model == "NAM":
            time_step = time_index*3
            
        if self.model == "GEFS":
            time_step = time_index*6
            
        # Set forecast date and hour  
        forecast_date = "{}".format(self.today_year)+'-'+self.time_strings[time_index].replace("/","-")[:-5]
        forecast_hour = self.time_strings[time_index][-5:]+"Z"
        
        print(self.time_strings[time_index])
        
        if self.time_strings[0][-5:].replace(":","") != self.init_hour:
            print("THREDDS done messed up! The base hour and given init hour are not the same!!!!")
            print(f"Base hour = {self.time_strings[0][-5:].replace(':','')}\nInit hour = {self.init_hour}")


                                            # Plot Title
    #---------------------------------------------------------------------------------------------------
    
        ax.set_title(f'{self.model}: {self.title_prod.replace("_"," ")}\n{variable}', size=16, loc='left',fontdict=font)
        
        ax.set_title(f"Init Hour: {self.init_date_title} {self.init_hour_title}\nForecast Hour: F{time_step:02d} {forecast_date}{forecast_hour}",
                     size=16, loc='right',fontdict=font)


                                            # Variable Plot
    #---------------------------------------------------------------------------------------------------
        
        print(var_data.ndim)
        if contourfill == True:
            #if data.ndim == 4:
            if var_data.ndim == 4:
                
                #cs2 = ax.contourf(lons, lats, var_data, self.clevs, cmap=cmap,
                #          transform=datacrs)
                
                cs2 = ax.contourf(lons, lats, var_data[time_index,level,:,:][:], self.clevs, cmap=self.cmap,
                         transform=datacrs)
                
                cbaxes = fig.add_axes(colorbar_axis) # [left, bottom, width, height]
    
                plt.colorbar(cs2, orientation='horizontal',cax=cbaxes)
            
            #if data.ndim == 3:
            if var_data.ndim == 3:
                #cs2 = ax.contourf(lons, lats, var_data, self.clevs, cmap=cmap,
                #          transform=datacrs)
                
                cs2 = ax.contourf(lons, lats, var_data[time_index,:,:][:], self.clevs, cmap=self.cmap,
                          transform=datacrs)
                
                cbaxes = fig.add_axes(colorbar_axis) # [left, bottom, width, height]
    
                plt.colorbar(cs2, orientation='horizontal',cax=cbaxes)
            
        if contourfill == False:
            #if data.ndim == 4:
            if var_data.ndim == 4:
                #cs2 = ax.contour(lons, lats, var_data, self.clevs, colors=self.colors,
                #      transform=datacrs)
                
                cs2 = ax.contour(lons, lats, var_data[time_index,level,:,:][:], self.clevs, colors=self.colors,cmap=self.cmap,
                      transform=datacrs)
                plt.clabel(cs2,colors='k', **kw_clabels)
            
            #if data.ndim == 3:
            if var_data.ndim == 3:
                #cs2 = ax.contour(lons, lats, var_data, self.clevs, colors=self.colors,
                #      transform=datacrs)
                
                cs2 = ax.contour(lons, lats, var_data[time_index,:,:][:], self.clevs, colors=self.colors,cmap=self.cmap,
                      transform=datacrs)
                plt.clabel(cs2,colors='k', **kw_clabels)
            
        plt.show()
                                            # Save Figure
    #---------------------------------------------------------------------------------------------------    
     
        outfile = f"{self.model}_{self.title_prod}_{filename_var}_{self.file_time}_F{time_step:02d}.png"
        fig.savefig(self.im_save_path+outfile,bbox_inches='tight',dpi=120)
        
        
        
