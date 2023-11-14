#!/usr/bin/env python
# coding: utf-8

# # Practice 1: Salaries

# Utilising the file named 'Salaries.csv,' which holds data regarding the salaries of academic staff members across different positions, perform a series of tasks to extract information according to particular requirements or answer the questions.

# Import pandas

# In[1]:


import pandas as pd


# Read this csv into a dataframe called df

# In[5]:


df=pd.read_csv("Data/Salaries.csv")


# What are the columns names?

# In[6]:


df.columns


# What are data types of columns we have in this data frame?

# In[10]:


df.dtypes


# Select rank, gender and salary columns and display the results on screen

# In[16]:


df[['rank','gender','salary']]


# Write the selected columns from the previous task to a new csv file called selected_salaries.csv

# In[19]:


df =('selected_salaries.csv')


# -------------------------------End of Practice 1 --------------------------------------
