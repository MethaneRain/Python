#!/usr/bin/env python
# coding: utf-8

# In[2]:


import calendar

def JulianDate_to_MMDDYYY(y,jd):
    month = 1
    day = 0
    while jd - calendar.monthrange(y,month)[1] > 0 and month <= 12:
        jd = jd - calendar.monthrange(y,month)[1]
        month = month + 1
    print(month,jd,y)


# In[6]:


YYYY = input("Year: ")
DD = input("Julian Day: ")


# In[9]:


print("Datetime:")
JulianDate_to_MMDDYYY(int(YYYY),int(DD))


# In[ ]:




