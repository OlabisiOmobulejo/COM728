#!/usr/bin/env python
# coding: utf-8

# IMPORTING CSV FILES

# In[4]:


import csv
file_name = "songs.csv"

with open(file_name, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        
        headings = next(csv_reader)
        print(headings)

# this code is to extract the headings from the csv file


# ACTIVITY VALUES

# In[6]:


import csv
file_name =  "songs.csv'

with open(file_name, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
    headings = next(csv_reader)
    print("Headings:", headings)
    
for row in csv_reader:
        print("Values:", row)
        


# In[9]:


import csv

file_name = 'songs.csv'

with open(file_name, 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    headings = next(csv_reader)
    print("Headings:", headings)
    
    for row in csv_reader:
        print("Values:", row)
        
        
        # importing the rows from the csv file


# Song_titles

# In[10]:


import csv

file_name = 'songs.csv'

with open(file_name, 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # headings from the file
    
    headings = next(csv_reader)
    song_heading = headings.index('Song')
    print("Heading: Song")
    
 # using loop to read and display song
        
    for row in csv_reader:
        print("Song Title:", row[song_heading])
        
        


# Formatted_Values

# In[17]:



import csv

 
file_name = 'songs.csv'

# reading and creating a reading file
with open(file_name, 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # Read only to skip headings
    headings = next(csv_reader)
    
    #  display of specific values with format
    
    for row in csv_reader:
        year = row[0]
        song_title = row[1]
        artist = row[2]
        formatted_output = f"[{year}] {song_title} (by {artist})"
        print(formatted_output)


# In[ ]:




