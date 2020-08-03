#!/usr/bin/env python
# coding: utf-8

# In[1]:


# https://kolesnikov.ga/Testing_and_Debugging_Jupyter_Notebooks/
import doctest
import calendar
import datetime
import pytz


# In[2]:


def convert_datetime_to_dayofweek(datetime_string):
    """
    This function takes date in the format MON DAY YEAR  HH:MM(PM/AM)
    and returns the day of the week
    Assume input string is UTC
    
    >>> convert_datetime_to_dayofweek('Jun 1 2005  1:33PM')
    'Wednesday'
    >>> convert_datetime_to_dayofweek('Oct 25 2012  2:17AM')
    'Thursday'
    """
    # your code goes herecalendar.day_name[my_date.weekday()] 
    dayofweek=calendar.day_name[(datetime.datetime.strptime(datetime_string, "%b %d %Y  %I:%M%p")).weekday()]
    return dayofweek


# #### Testing the code

# In[3]:


convert_datetime_to_dayofweek('Oct 25 2012  2:17AM')


# In[4]:


convert_datetime_to_dayofweek('Jun 1 2005  1:33PM')


# #### Running the Doctest

# In[5]:


doctest.testmod(verbose=True)

