#!/usr/bin/env python
# coding: utf-8

# In[1]:


from datetime import date


# In[2]:


YYYY = input("Year: ")
MM = input("Month: ")
DD = input("Day: ")


# In[3]:


# Start of year for reference
d0 = date(int(YYYY), 1, 1)

# Set the date you want to convert
d1 = date(int(YYYY), int(MM), int(DD))

# 
delta = d1 - d0
Day = delta.days+1
print("Julian Day Number:",Day)

