#!/usr/bin/env python
# coding: utf-8

# Acquire power data from this source for at least 10 days and not more than 40 days. The website limits the window size, so you will need to download multiple files. Load the data into a Jupyter Notebook
# Combine the multiple input files to create a single dataframe. <br>
# Create two bar graphs of the power consumption per hour. <br>
# One bar graph has 24 bars; each bar is the average across all days for that hour<br>
# one bar graph has 24*(number of days) bars.  Your choice of average or sum for each hour. Label the y-axis appropriately.<br>
# Submit the .ipynb file containing the analysis and the generated pictures.
# 

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[3]:


import seaborn as sns
sns.set(style="whitegrid")
tips = sns.load_dataset("tips")


# #### Reading data from two files 

# In[12]:


data1=pd.read_csv('Electricity Data\RollingSystemDemand_20191013_0451.csv')
data2=pd.read_csv('Electricity Data\RollingSystemDemand_20191013_0452.csv')


# #### Taking dataset from Oct-01-2019 to Oct-10-2019 ie 10 days of data

# In[13]:


data1.shape


# In[14]:


data1.head()


# In[15]:


data1.tail()


# In[16]:


data2.tail()


# #### The last value of the data is the count of number of rows so dropping it otherwise it will affect the dte conversion

# In[17]:


data1.drop(data1.tail(1).index,inplace=True)
data2.drop(data2.tail(1).index,inplace=True)


# In[18]:


data1.tail()


# #### Combining the two data set

# In[19]:


frames=[data1, data2]


# In[20]:


data=pd.concat(frames)


# In[21]:


len(data)


# In[22]:


data.head()


# In[23]:


data.tail()


# #### Let us format the date

# In[24]:


data['HDR']=data['HDR'].astype('str')


# In[25]:


data['HDR']=pd.to_datetime(data['HDR'],format='%Y%m%d%H%M%S')


# In[26]:


data


# #### Letus make a new column and put the values of hour from the HDR column

# In[27]:


hours=[]
for i in data['HDR']:
    hours.append(i.hour)


# In[28]:


data['Hours'] = hours


# In[29]:


data.head()


# #### Groupby hours so that we can get the average based on hours

# In[30]:


dataGroupByHours=data.groupby("Hours")


# #### Got the average/mean data of ROLLING SYSTEM DEMAND column and storing it into a list

# In[42]:


averageSupply=list(dataGroupByHours['ROLLING SYSTEM DEMAND'].mean())
hours=np.arange(len(averageSupply))


# #### Plotting the data as a bar graph

# In[32]:


f, ax = plt.subplots(figsize=(18,5))
ax = sns.barplot(x=np.arange(len(averageSupply)), y=averageSupply, data=tips,palette="Blues_d")
ax.set(xlabel='Hours', ylabel='Power Supply(MegaWatt)', title='Average Power supply for each hour from 1-Oct to 10-Oct 2019')
plt.show()


# #### Creating the list which contains only date and hour, converting minutes and seconds as 0. and making a new column out of it.

# In[43]:


date_hour=[]
for i in data['HDR']:
    date_hour.append(i.replace(minute=0, second=0))


# In[44]:


date_hour


# In[36]:


data['Date_Hour']=date_hour


# #### Grouping by the Date_Hour and columns

# In[45]:


dataGroupByDateHour=data.groupby("Date_Hour")


# #### so getting the sum of supply for each hour and each day

# In[46]:


supplyHourPerDay=list(dataGroupByDateHour['ROLLING SYSTEM DEMAND'].sum())


# In[ ]:


#### Plotting 24*10 bars representing sum of power supply for each hour in 10 days


# In[41]:


f, ax = plt.subplots(figsize=(30,10))
ax = sns.barplot(x=np.arange(len(dataGroupByDateHour)), y=supplyHourPerDay, data=tips,palette="Blues_d")
ax.set_xlabel("Hours for 10 days",fontsize=30)
ax.set_ylabel("Sum of Power Supply(MegaWatt) per hour",fontsize=20)
ax.set_title("Power supply in 10 days",fontsize=30)
plt.show()

