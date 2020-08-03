#!/usr/bin/env python
# coding: utf-8

# For each file, remove punctuation and stop words​<br>
# 
# Produce a single .dat file containing the name of each file in quotes, a colon, then a list of words separated by commas​. The list of words per file should be unique for that file. Do not include URLs or phone numbers. Words should be made lowercase. <br>
# 
# Example output:<br>
# 
# "File 1.txt" : word1, word2, word3, word7​<br>
# "name of file.docx" : word8, word2, word1, word10​<br>
# "another file.doc" : word1, word12, word6​<br>
# 

# In[1]:


import pandas as pd
import nltk
import math
import os
import fnmatch
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
import string
import re
from docx import Document


# URL Regular Expression reference from stackoverflow <br>
# https://stackoverflow.com/questions/3809401/what-is-a-good-regular-expression-to-match-a-url

# In[2]:


regxUrl="https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|http?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,}"


# Phone number Regular Expression reference from regexlib <br>
# http://regexlib.com/REDetails.aspx?regexp_id=283

# In[3]:


regxPhoneNumber="\(?[\d]{3}\)?[\s-]?[\d]{3}[\s-]?[\d]{4}"


# Creating the list of punctualtion marks and adding some more to it

# In[4]:


punctuation=list(string.punctuation)
punctuation.append('--')
punctuation.append('“')
punctuation.append('”')
punctuation.append('’')
punctuation.append('‘')
punctuation.append('-')
punctuation.append('—')
punctuation.append('``')


# In[5]:


file= open("AssignmentFile.dat","w+") # output file
en_stops = set(stopwords.words('english')) # Stope Words taken
foldr='week_10_txt_and_docx/' # folder in which the files are kept


# Working on txt file

# In[6]:


for file_name in os.listdir(foldr):
    if fnmatch.fnmatch(file_name, '*.txt'):# Matching the txt file
        file.write('"'+file_name+'" : ')# writing file name to output file
        with open(foldr+file_name,'r', encoding="utf-8-sig") as fil: # Opening the file
            fileContent=fil.read().lower() # set to lower case
            fileContent=(" ".join(sorted(set(fileContent.split()), key=fileContent.split().index))) # removing repetative strings
            urlRemoved=re.sub(regxUrl, "", fileContent) # removing URL using reqx
            phoneNumberRemoved=re.sub(regxPhoneNumber, "", urlRemoved) # removing Phone number using regx
            sent_tokenize_list = sent_tokenize(phoneNumberRemoved) # forming sentance
            for this_sent in sent_tokenize_list: 
                word_tokens=word_tokenize(this_sent) # forming words
                for w in word_tokens:
                    if w not in en_stops:  # excluding stop words
                        if w not in list(punctuation): #excluding punctuation marks
                            file.write(w+',') # writing the filtered words to file
        file.write('\r\n')


# Working on docx

# In[7]:


for file_name in os.listdir(foldr):
    if fnmatch.fnmatch(file_name, '*.docx'):# Matching the docx file
        file.write('"'+file_name+'" : ')# writing file name to output file
        document = Document(foldr+file_name)
        indx=0
        docFileContent=[]
        fileContent1=''
        for para in document.paragraphs:
            if (len(para.text)>0):
                indx+=1
                docFileContent.append(para.text.lower()) # storing each text to list
        fileContent1=fileContent1.join(docFileContent) # converting list to string
        fileContent=(" ".join(sorted(set(fileContent1.split()), key=fileContent1.split().index)))# removing repetative strings
        urlRemoved=re.sub(regxUrl, "", fileContent) # removing URL using reqx
        phoneNumberRemoved=re.sub(regxPhoneNumber, "", urlRemoved)  # removing Phone number using reqx
        sent_tokenize_list = sent_tokenize(phoneNumberRemoved)# forming sentance
        for this_sent in sent_tokenize_list:
            word_tokens=word_tokenize(this_sent)# forming words
            for w in word_tokens:
                if w not in en_stops:  # excluding stop words
                    if w not in list(punctuation):#excluding punctuation marks
                        file.write(w+',')# writing the filtered words to file
        file.write('\r\n') 


# In[8]:


file.close() # closing the file after write

