#!/usr/bin/env python
# coding: utf-8

# #### I provide you with a compressed XML file. Some of the fields contain HTML. <br>
# 
# #### 1. Extract the XML from the .zip file. In Python, use a module to parse the XML (do not write an XML parser)<br>
# #### 2. Using Python, extract the HTML from the XML. Then use BeautifulSoup4 to parse the HTML <br>
# #### 3. For each HTML page, report the number of links (URLs with the tag < a href="URL">text) in each HTML page <br>
# #### 4. Submit a single Jupyter notebook that parses the XML file and produces the count of links per HTML file<br>

# In[1]:


import xml.etree.ElementTree as ET
import xmltodict
from bs4 import BeautifulSoup


# #### Takin a look of xml

# In[2]:


with open('xml_containing_html.xml') as fd:
    xml = xmltodict.parse(fd.read())


# #### hmm, HTML data is in the content tag

# In[3]:


xml


# #### Parsing the xml

# In[4]:


root = ET.parse('xml_containing_html.xml').getroot()


# #### lets look for all the tags

# In[5]:


elemList=[]
for elem in root.iter():
    elemList.append(elem.tag)
#print(elemList)


# #### Verifing  that the "html" is in the content tag only

# In[6]:


allpages=[]
for con in root.iter('all_pages'):
    allpages.append(con.text)


# In[7]:


print(allpages)


# In[8]:


dv=[]
for con in root.iter('dvtahsakkl'):
    dv.append(con.text)
print(dv)


# #### getting all the html pages into a list

# In[9]:


content=[]
for con in root.iter('content'):
    content.append(con.text)
#print(content)


# #### Getting the seprate page link into "thisPageLink" list and combine all the links will be in "totalLink" list

# In[10]:


totalLinks=[]
count=0
for text in content:
    thisPageLink=[]
    count=count+1
    soup = BeautifulSoup(text, 'html.parser')
    for link in soup.find_all('a'):
        totalLinks.append(link.get('href'))
        thisPageLink.append(link.get('href'))
    print("Number of links in page "+str(count)+":" + str(len(thisPageLink)))


# In[11]:


print("Total number of links :"+ str(len(totalLinks)))


# In[12]:


print("List of all the links:")
totalLinks


# In[ ]:




