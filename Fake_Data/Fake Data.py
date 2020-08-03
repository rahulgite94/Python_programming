#!/usr/bin/env python
# coding: utf-8

# Write a Python notebook that generates a file containing the following data:​ ​
# 
# Email addresses​. Must have an "@"
# Phone numbers <br>
# Home Address​<br>
# Person's name​<br>
# Year born. Use realistic values.​<br>
# Number of kids. Use realistic values.​<br>
# Categorical variable: rent or own?​<br>
# Annual income. Optional challenge: Use a non-uniform distribution​<br>
# Number of speeding tickets in past year. Optional challenge: Use a non-uniform distribution​<br>
# The user of your notebook should be able to specify how many entities are to be generated.​ <br>
# 
# ​Do not include the .csv output file in your submission -- the file should be generated dynamically.
# 
# Order of columns in CSV is not relevant.

# ### Limitaions: This program can generate upto 20 rows of fakedata

# #### Importing required Libraries

# In[1]:


#from bs4 import BeautifulSoup as bs
import requests as rq
import pandas as pd
import numpy as np
import itertools as itr
from faker import Faker
import glob


# #### Every function returns specific count of records which will be requested by the user.
# #### Scraping the names from the https://www.ssa.gov/oact/babynames/ and maintaining it in a list.

# In[2]:


def getNames(count):
    webTable=pd.read_html('https://www.ssa.gov/oact/babynames/')
    arr= webTable[0].values
    names=[]
    for listt in arr:
        for name in listt :
            if isinstance(name, str):
                names.append(name)
    return names[:count]


# #### Appending the "@gmail.com" on every name in the list and creating there email

# In[3]:


def getEmail(count):
    names= getNames(count)
    emails=[]
    for i in names:
        emails.append(i+'@gmail.com')
    return emails[:count]


# #### Testing above functions

# In[4]:


print(getNames(5))
print(getEmail(5))


# #### Randomly generating the phone number with formating

# In[5]:


def phoneNumber():
    l1=str(np.random.randint(1,9,3)).strip("[]")
    l2=str(np.random.randint(0,9,3)).strip("[]")
    l3=str(np.random.randint(0,9,4)).strip("[]")
    return '{}-{}-{}'.format(l1,l2,l3)


# #### Calling the above function based on count

# In[6]:


def getPhoneNumber(count):
    phoneNumbers=[]
    for _ in range(count):
        phoneNumbers.append(phoneNumber()) 
    return phoneNumbers


# #### Sample run

# In[7]:


getPhoneNumber(10)


# #### While researching about the assignment found an interesting approach through Faker library. Which allows you to direclty generate the fake data in a proper format.
# source: https://www.geeksforgeeks.org/python-faker-library/

# In[8]:


def getAddress(count):
    addresses=[]
    for _ in range(count):
        addresses.append(Faker().address())
    return addresses


# In[9]:


getAddress(8)


# #### Randomly generating the birth year from 1970 to 2000, to make it realistic

# In[10]:


def getBirthYear(count):
    return list(np.random.randint(1970,2000,count))


# In[11]:


getBirthYear(8)


# #### Randomly generating the number of kids

# In[12]:


def getNumberOfKids(count):
    return list(np.random.randint(0,5,count))


# #### Randomly choosing from the Rent or own 

# In[13]:


def getRentorOwn(count):
    RoN=[]
    for _ in range(count):
        RoN.append(np.random.choice(['Rent','Own']))
    return RoN


# In[14]:


getRentorOwn(5)


# #### Tried to achieve the non uniform distribution.
# #### Took half of count, below the average salary of a US citizen (poor) and half of count above the average salary (rich)

# In[15]:


#averageIncome=59039
def getIncome(count):
    poor=list(np.random.randint(1000,59039,int(count/2)))
    rich=list(np.random.randint(59039,90000,(count-len(poor))))
    return poor+rich


# In[16]:


getIncome(9)


# #### Generating random numbers of tickets issued

# In[17]:


def getTicket(count):
    return list(np.random.randint(0,5,count))


# In[21]:


getTicket(5)


# #### Accululating all the results of above funcation into a data frame and writing it to a csv file

# In[18]:


def createCSV(fileName,count):
    df2 = pd.DataFrame({'Names':getNames(count),
                        'Email':getEmail(count),
                        'Phone Number':getPhoneNumber(count),
                        'Address':getAddress(count),
                        'Birth Year':getBirthYear(count),
                        'Annual Income':getIncome(count),
                        'Speeding Tickets':getTicket(count)
                       })
    df2.to_csv(fileName, index = None, header=True)


# In[19]:


#### getting the file name and asking to reenter in file name already present
#### Getting the count from the user for number of entries


# In[20]:


fileName=input('Enter file name:')
files_present = glob.glob(fileName)
if  files_present:
    fileName=input('File name already exist enter another file name:')
count= int(input('Please enter the number of counts:'))
createCSV(fileName,count)


# In[ ]:




