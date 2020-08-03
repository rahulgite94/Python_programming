#!/usr/bin/env python
# coding: utf-8

# Simulate a fair die and a biased 6-sided die.<br>
# The biased die has probabilities {0.15, 0.15, 0.15, 0.15, 0.15, 0.25}. <br>
# Create a visualization that compares outcomes of multiple rolls of a fair die and this biased die.<br>
# You can use a single visualization or multiple visualizations to demonstrate the difference in outcomes for the dice. <br>
# The user of your notebook should be able to alter the number of simulations as an argument to a function.​<br>

# In[1]:


import random
import matplotlib.pyplot as plt
import numpy as np


# #### User entry for number of  times adice needs to be rolled

# In[2]:


numOfRolls=int(input("Please enter number of times you want to roll a dice: "))


# #### Fair Dice rolls and storing the outcomes in a list

# In[3]:


dice=['one','two','three','four','five','six']
def fairDieRolls(numOfRolls,lst):
    fairRolls=[]
    for _ in range(0,numOfRolls):
        outcome=random.choice(lst)
        fairRolls.append(outcome)
    return fairRolls


# In[4]:


fairRolls=fairDieRolls(numOfRolls,dice)


# #### Biased dice rolls with the respective weight 

# In[5]:


def biasedDieRolls(numOfRolls,lst):
    return random.choices(lst, [0.15, 0.15, 0.15, 0.15, 0.15, 0.25], k=numOfRolls)


# #### storing biased outcomes in a list

# In[6]:


biasedRolls=biasedDieRolls(numOfRolls,dice)


# #### Plotting the outcomes of  FairDice rolls

# In[7]:


plt.hist(fairRolls)
plt.xlabel("Dice Value")
plt.ylabel("Number of counts")
plt.title("Fair Dice Roll")
plt.show()


# #### Plotting the outcomes of  Biased dice rolls, and observing that the probability of the number "six" was greater so as plot says.

# In[8]:


plt.hist(biasedRolls);
plt.xlabel("Dice Value")
plt.ylabel("Number of counts")
plt.title("Biased Dice Roll")
plt.show()

