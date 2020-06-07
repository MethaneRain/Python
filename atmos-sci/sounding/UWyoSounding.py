#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 00:52:49 2020

@author: Justin Richling

University of Wyoming and MetPy Soundings (non Siphon)
"""

class UWyoSound:
    
    def __init__(self):
        '''
        Default values
        
        * date -> current date
        * launch hour -> 12
        * image save path -> cwd

        '''
        from datetime import datetime
        now = datetime.utcnow()
        self.today_day = int('{0:%d}'.format(now))
        self.today_year = int('{0:%Y}'.format(now))
        self.today_month = int('{0:%m}'.format(now))
        print(self.today_day,self.today_year,self.today_month)
        
        # initialization hour for model forecast
        self.launch_hour = 12
        
        # current working drive for saved images
        self.im_save_path = "./"
        
        self.station_num = 72469
        self.station_name = "DNR"
        
        