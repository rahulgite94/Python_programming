#!/usr/bin/env python
# coding: utf-8

# <br>
# 
# Look for .ipynb files using the glob module in Python​.<br>
# Your analysis should include at least eight .ipynb files. ​.<br>
# Files used for code other than assignments (eg projects, work from other courses) is acceptable to include ​.<br>
# Create functions that parse the file and find modules.​.<br>
# Use a loop to call the functions on each file.​.<br>
# Look for code cells (ignore Markdown and raw cells)​.<br>
# Look for lines of code that start with either "from" or "import"​​.<br>​
# Look for the keywords only in code input (rather than including cell output content)​.<br>​
# Result is a list of unique modules used. The list doesn't need to include specific functions. For example, in ​.<br>
# 
# from math import pi
# 
# The relevant module is math

# In[1]:


import os
import json
import fnmatch


# This method will find each import from the files and add it to the list

# In[2]:


def fetchImport(file_name):
    data = json.load(open(file_name,"r"))
    for item in data['cells']:
        for code in item['source']:
            if 'import' in code:
                allImports.append(code)


# In[3]:


foldr='HW_files/'
allImports=[]
count=0
for file_name in os.listdir(foldr):
    if fnmatch.fnmatch(file_name, '*.ipynb'):
        print(foldr+file_name)
        fetchImport(foldr+file_name)# method call
        #Code to count lines of code
        data = json.load(open(foldr+file_name,"r"))
        for item in data['cells']:
            # each list represent a noteboo cell and length of list represent the number of line of code in one cell
            count=count+len(item['source']) # final count will be the total line of code written


# In[4]:


releventImports=[]
for imports in allImports:
    if 'from' in imports:# working to remove 'from'
        string=imports.replace('from', '')
        if (string.split( )[0]) not in releventImports:
            releventImports.append(string.split( )[0])
    elif 'import' in imports:# working to remove 'import'
        string=imports.replace('import', '')
        if (string.split( )[0]) not in releventImports:
            releventImports.append(string.split( )[0])


# In[5]:


releventImports #All the imports used 


# 'count' represent the total number of line of code written

# In[6]:


count

