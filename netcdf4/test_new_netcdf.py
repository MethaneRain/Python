#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 00:11:32 2020

@author: chowdahead
"""

                            # Test new netcdf file
#-----------------------------------------------------------------------------#
import netCDF4 as nc
import numpy as np
new_ds = nc.Dataset("new_nectdf_file_example.nc")

print(list(new_ds.variables))

