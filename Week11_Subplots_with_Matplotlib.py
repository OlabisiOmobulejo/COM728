#!/usr/bin/env python
# coding: utf-8

# # Week 11 Subplots with Matplotlib

# - Chapter 4. Visualization with Matplotlib by VanderPlas. J, 2016. Python Data Science Handbook. O'Reilly Media, Inc.
# - [Feldman, J.](http://jake-feldman.squarespace.com/data-science-python-oscm400c) Data Science - Python, Intro to Matplotlib
# - [Engineering for Data Science](https://engineeringfordatascience.com/posts/matplotlib_subplots/) Matplotlib: Plotting Subplots in a Loop

# ***

# # Recap from previous class

# - <font size=3>Importing matplotlib: import matplotlib.pyplot as plt</font>
# - <font size=3>Line chart uses .plot() function</font>
# - <font size=3>Scatter plot uses .scatter() function</font>
# - <font size=3>Bar chart uses .bar() function</font>
# - <font size=3>Pie chart uses .pie() function</font>

# ***

# <font size="5">**Learning Objectives**</font><br>
# <font size="3">After this session, you should be able to:</font>
# - <font size="3">create subplot</font>
# - <font size="3">customise subplot</font>

# ***

# # Part 1: Create Subplots

# # Simple Grids of Subplots

# - <font size=3>We can use function <span style="color:blue;"><b>subplot()</b></span> to creates a single subplot within a grid <font>
# - <font size="3"><b>Syntax:</b></font><br>
# &emsp;&emsp;&emsp;&emsp;<font size="3"> plt.<span style="color: blue;">subplot(nrows, ncols, index of the plot)</span>
#     - <font size=3>The index runs from the upper left postion to the bottom right</font>

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plt

# create a figure 
fig = plt.figure()

'''Generate subplots arranged in a matrix with one row and three columns, 
and draw the first subplot in the leftmost column.'''
plt.subplot(1, 3, 1)

#show the plot
plt.show()


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plt

fig = plt.figure()

'''Generate subplots arranged in a matrix with one row and three columns, 
and draw the first subplot in the leftmost column.'''
plt.subplot(1, 3, 1)

'''Generate subplots arranged in a matrix with one row and three columns, 
and draw the second subplot in the middle column.'''
plt.subplot(1, 3, 2)

plt.show()


# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plt

fig = plt.figure()

'''Generate subplots arranged in a matrix with one row and three columns, 
and draw the first subplot in the leftmost column.'''
plt.subplot(1, 3, 1)

'''Generate subplots arranged in a matrix with one row and three columns, 
and draw the second subplot in the middle column.'''
plt.subplot(1, 3, 2)

'''Generate subplots arranged in a matrix with one row and three columns, 
and draw the third subplot in the rightmost column.'''
plt.subplot(1, 3, 3)

plt.show()


# In[4]:


get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plt

fig = plt.figure()

'''Arrange subplots in a 2x3 matrix. Place the first subplot 
in the top-left corner, the second to its right, and the last 
in the top-right. Continue to the next row, arranging subplots 
from left to right.'''
plt.subplot(2, 3, 1)

plt.subplot(2, 3, 2)

plt.subplot(2, 3, 3)

plt.subplot(2, 3, 4)

plt.subplot(2, 3, 5)

plt.subplot(2, 3, 6)


plt.show()


# In[5]:


get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plt

fig = plt.figure()

#Use a for loop to incrementally generate subplots on the figure.
for i in range(1, 7):
    plt.subplot(2, 3, i)
    
plt.show()


# <font size=3>The command `subplots_adjust` can be used to adjust the spacing between these plots.</font>
# - <font size="3"><b>Syntax:</b></font><br>
# &emsp;&emsp;&emsp;&emsp;<font size="3">fig.subplots_adjust(hspace=None, wspace=None)</font>

# In[6]:


get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plt
fig = plt.figure()

#adjust the spacing between subplots
#the space is 50% of the subplot width and height
fig.subplots_adjust(hspace=0.5, wspace=0.5) 

#Use a for loop to incrementally generate subplots on the figure.
for i in range(1, 7):
    plt.subplot(2, 3, i)

plt.show()


# <div class="alert alert-block alert-info">
# <b>Note: </b>
#     <ul>
#         <li><b>hspace:</b> specify the spacing along the height of the figure</li>
#         <li><b>wspace:</b> specify the spacing along the width of the figure</li>
#     </ul>
# </div>

# # The Whole Grid in One Go

# - <font size=3>One convenient way to create subplots is to use the function <span style="color:blue;"><b>subplots()</b></span><font>
# - <font size="3"><b>Syntax:</b></font><br>
# &emsp;&emsp;&emsp;&emsp;<font size="3"> plt.<span style="color: blue;">subplots(nrows, ncols, figsize)</span>
# - <font size="3">The size of this grid is determined by what you specify for figsize, which takes a list where the first entry specifies the horizontal length and the second entry specifies the vertical length</font>
# - <font size=3>With this function, we can populate a figure with a number of <span style="color:blue;"><b>Axes ("plots")</b></span> and arrange these into a grid of rows and columns</font>

# In[7]:


get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plt

#create a figure (fig) with a 2x2 grid of subplots
#axs is a 2D array of subplot axes
fig, axs = plt.subplots(2,2,figsize=(15,11))

plt.show()


# In[8]:


get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plt

#create a figure (fig) with a 4x1 grid of subplots
#ax1, ax2, ax3, and ax4 represent the individual subplot axes
fig, (ax1,ax2,ax3,ax4) = plt.subplots(4,1,figsize=(15,11))

plt.show()


# In[9]:


get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plt

#create a figure (fig) with a 1x4 grid of subplots
#ax1, ax2, ax3, and ax4 represent the individual subplot axes
fig, (ax1,ax2,ax3,ax4) = plt.subplots(1,4,figsize=(15,11))

plt.show()


# In[10]:


get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plt

#create a figure (fig) with a 2x3 grid of subplots, arranged in a nested structure. 
#The nested structure in the unpacking, ((ax1,ax2,ax3),(ax4,ax5,ax6)), 
#reflects the organisation of the subplots in the grid. 
fig, ((ax1,ax2,ax3),(ax4,ax5,ax6)) = plt.subplots(2,3,figsize=(15,11))

plt.show()


# - <font size=3>Alternatively, we can use the method <span style="color:blue;"><b>add_subplot</b></span> of a Figure to add an individual subplot<font>  
# - <font size=3>The location of the subplot in the grid is specified by providing the dimensions of the grid and the location of the subplot in that grid</font>

# In[11]:


get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(15,11))

#add an individual subplot
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

plt.show()


# In[12]:


get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plt
plt.subplots_adjust(wspace=0.3,hspace=0.5)

fig = plt.figure(figsize=(10,12))

#add an individual subplot
ax1 = fig.add_subplot(4,1,1)
ax2 = fig.add_subplot(4,2,3)
ax3 = fig.add_subplot(4,2,4)
ax4 = fig.add_subplot(4,1,3)
ax5 = fig.add_subplot(4,2,7)
ax6 = fig.add_subplot(4,2,8)

plt.show()


# # Set title, xlabel, ylabel for subplot

#  <font size=3>We can use function <span style="color:blue;"><b>set()</b></span> to add titles and axes lables to a given axis.<font>
# - <font size="3"><b>Syntax:</b></font><br>
# &emsp;&emsp;&emsp;&emsp;<font size="3"> ax.<span style="color: blue;">set(title='title',xlabel='x-label',ylabel='y-label')</span>

# In[15]:


get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plt

#create a figure (fig) with a 2x2 grid of subplots
#unpacks the individual subplot axes into a nested structure
fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2,figsize=(15,11))

#sets labels for the subplot in the top-left position (0,0)
ax1.set(title="Axis[0,0]", xlabel='x-label',ylabel='y-label')
#sets labels for subplot in the top-right position (0,1)
ax2.set(title="Axis[0,1]", xlabel='x-label',ylabel='y-label')
#sets labels subplot in the bottom-left position (1,0)
ax3.set(title="Axis[1,0]", xlabel='x-label',ylabel='y-label')
#sets labels subplot in the bottom-right position (1,1)
ax4.set(title="Axis[1,1]", xlabel='x-label',ylabel='y-label')

plt.show()


# ***

# # Part 2: Create subplots from a dataframe

# - <font size=3>Now, we will work with a data set in "sales_data_sample.csv" that contains information on the record sales.</font> 
# - <font size=3>We will create a collection of charts/graphs for the customer analysis</font> 

# ## Prepare a dataframe

# In[13]:


get_ipython().run_line_magic('matplotlib', 'inline')

import pandas as pd
import matplotlib.pyplot as plt


#Read in data frame
df_sales = pd.read_csv("Data/sales_data_sample.csv",encoding='Latin-1')
df_sales


# In[14]:


#check data types
df_sales.dtypes


# ### Change String to Date in DataFrame

# In[17]:


#convert ORDERDate column to datetime

df_sales['ORDERDATE'] = pd.to_datetime(df_sales['ORDERDATE'], dayfirst=True)


# In[18]:


df_sales


# In[19]:


#Extract values from the 'ORDERDATE' column and convert them into a list.
print(list(df_sales['ORDERDATE']))


# In[20]:


#Extract the month component from each date in the column and create 
#a list with these month values.
print(list(df_sales['ORDERDATE'].dt.month))


# In[21]:


#Extract the year component from each date in the column and create 
#a list with these year values.
print(list(df_sales['ORDERDATE'].dt.year))


# ### Create a subplots: 3 x 1 

# In[22]:


#Create figure and get the axes

fig , (ax1,ax2,ax3) = plt.subplots(3,1, figsize = (7,15))

#Add title for entire figure
fig.suptitle("The customer analysis")
plt.show()


# ### First axis: Product Line Sale for each year

# ### Product Sale for each year

# In[23]:


#Check number of order per year
record_per_year = df_sales.groupby(df_sales.ORDERDATE.dt.year).size()
record_per_year


# In[24]:


# Filter the order detial of year 2003
filtered_record_per_year_2003 = df_sales.loc[df_sales.ORDERDATE.dt.year==2003,:]
filtered_record_per_year_2003


# In[25]:


# Filter the order detial of year 2004
filtered_record_per_year_2004 = df_sales.loc[df_sales.ORDERDATE.dt.year==2004,:]
filtered_record_per_year_2004


# In[26]:


# Filter the order detial of year 2005
filtered_record_per_year_2005 = df_sales.loc[df_sales.ORDERDATE.dt.year==2005,:]
filtered_record_per_year_2005


# In[ ]:


#Retrieve product line sale in 2003
products_line2003 = filtered_record_per_year_2003.groupby('PRODUCTLINE').size()


#Create figure and get the axes

fig , (ax1,ax2,ax3) = plt.subplots(3,1, figsize = (12,15))

#Add title for entire figure
fig.suptitle("The customer analysis")

#plot a chart
ax1.bar(products_line2003.index.tolist(), products_line2003.tolist(),width=0.2)
ax1.set(title="Product Sale", xlabel='Product Line',ylabel='Number of Sales')


plt.show()


# In[27]:


#Retrieve product line sale in 2003
products_line2003 = filtered_record_per_year_2003.groupby('PRODUCTLINE').size()

#Retrieve product line sale in 2004
products_line2004 = filtered_record_per_year_2004.groupby('PRODUCTLINE').size()

#Create figure and get the axes

fig , (ax1,ax2,ax3) = plt.subplots(3,1, figsize = (12,15))

#Add title for entire figure
fig.suptitle("The customer analysis")

#Set the range of x-axis
X_axis = [1,2,3,4,5,6,7]
width1=0.20

#plot a chart
ax1.bar(X_axis, products_line2003.tolist(),width=0.2,label="2003")

ax1.bar([x+width1 for x in X_axis], products_line2004.tolist(),width=0.2,label="2004")

ax1.set(title="Product Sale", xlabel='Product Line',ylabel='Number of Sales')
ax1.set_xticks(X_axis, products_line2003.index.tolist())
ax1.legend()

plt.show()


# In[28]:


#Retrieve product line sale in 2003
products_line2003 = filtered_record_per_year_2003.groupby('PRODUCTLINE').size()

#Retrieve product line sale in 2004
products_line2004 = filtered_record_per_year_2004.groupby('PRODUCTLINE').size()

#Retrieve product line sale in 2005
products_line2005 = filtered_record_per_year_2005.groupby('PRODUCTLINE').size()

#Create figure and get the axes

fig , (ax1,ax2,ax3) = plt.subplots(3,1, figsize = (12,15))

#Add title for entire figure
fig.suptitle("The customer analysis")

#Set the range of x-axis
X_axis = [1,2,3,4,5,6,7]
width1=0.20
width2=0.40

#plot a chart
ax1.bar(X_axis, products_line2003.tolist(),width=0.2,label="2003")

ax1.bar([x+width1 for x in X_axis], products_line2004.tolist(),width=0.2,label="2004")

ax1.bar([x+width2 for x in X_axis], products_line2005.tolist(),width=0.2,label="2005")

ax1.set(title="Product Sale", xlabel='Product Line',ylabel='Number of Sales')
ax1.set_xticks(X_axis, products_line2003.index.tolist())
ax1.legend()


plt.show()


# In[29]:


#Retrieve product line sale in 2003
products_line2003 = filtered_record_per_year_2003.groupby('PRODUCTLINE').size()

#Retrieve product line sale in 2004
products_line2004 = filtered_record_per_year_2004.groupby('PRODUCTLINE').size()

#Retrieve product line sale in 2005
products_line2005 = filtered_record_per_year_2005.groupby('PRODUCTLINE').size()

#Create figure and get the axes

fig , (ax1,ax2,ax3) = plt.subplots(3,1, figsize = (12,15))

#Add title for entire figure
fig.suptitle("The customer analysis")

#Set the range of x-axis
X_axis = [1,2,3,4,5,6,7]
width=0.20

#plot a bar chart where the year 2004 is positioned at the center 
#of the x-axis for each product line
ax1.bar([x-width for x in X_axis], products_line2003.tolist(),width=0.2,label="2003")

ax1.bar(X_axis, products_line2004.tolist(),width=0.2,label="2004")

ax1.bar([x+width for x in X_axis], products_line2005.tolist(),width=0.2,label="2005")

ax1.set(title="Product Sale", xlabel='Product Line',ylabel='Number of Sales')
ax1.set_xticks(X_axis, products_line2003.index.tolist())
ax1.legend()


plt.show()


# ### First axis: customised subplots
# - <font size=3>ax.grid()- set the present of the horizontal an vertical lines that create a grid on top of the plot.</font>
#     - <font size=3>False: removes the horizontal an vertical lines.</font>
#     - <font size=3>True: shows the horizontal an vertical lines.</font>
# - <font size=3>ax.set_facecolor("color"): Changes background color of the plot.</font>

# In[30]:


#Retrieve product line sale in 2003
products_line2003 = filtered_record_per_year_2003.groupby('PRODUCTLINE').size()

#Retrieve product line sale in 2004
products_line2004 = filtered_record_per_year_2004.groupby('PRODUCTLINE').size()

#Retrieve product line sale in 2005
products_line2005 = filtered_record_per_year_2005.groupby('PRODUCTLINE').size()

#Create figure and get the axes

fig , (ax1,ax2,ax3) = plt.subplots(3,1, figsize = (12,15))

#Add title for entire figure
fig.suptitle("The customer analysis")

#Set the range of x-axis
X_axis = [1,2,3,4,5,6,7]
width=0.20

#plot a bar chart where the year 2004 is positioned at the center 
#of the x-axis for each product line
ax1.bar([x-width for x in X_axis], products_line2003.tolist(),width=0.2,label="2003")

ax1.bar(X_axis, products_line2004.tolist(),width=0.2,label="2004")

ax1.bar([x+width for x in X_axis], products_line2005.tolist(),width=0.2,label="2005")


ax1.set(title="Product Sale", xlabel='Product Line',ylabel='Number of Sales')
ax1.set_xticks(X_axis, products_line2003.index.tolist())
ax1.legend()

#Add grid lines
ax1.grid(True)

#Change the background color


plt.show()


# ### Second axis: Deal Size for each year

# In[31]:


#Retrieve product line sale in 2003
products_line2003 = filtered_record_per_year_2003.groupby('PRODUCTLINE').size()

#Retrieve product line sale in 2004
products_line2004 = filtered_record_per_year_2004.groupby('PRODUCTLINE').size()

#Retrieve product line sale in 2005
products_line2005 = filtered_record_per_year_2005.groupby('PRODUCTLINE').size()

#Create figure and get the axes

fig , (ax1,ax2,ax3) = plt.subplots(3,1, figsize = (12,15))

#Add title for entire figure
fig.suptitle("The customer analysis")

#Set the range of x-axis
X_axis = [1,2,3,4,5,6,7]
width=0.20

#plot a bar chart where the year 2004 is positioned at the center 
#of the x-axis for each product line
ax1.bar([x-width for x in X_axis], products_line2003.tolist(),width=0.2,label="2003")

ax1.bar(X_axis, products_line2004.tolist(),width=0.2,label="2004")

ax1.bar([x+width for x in X_axis], products_line2005.tolist(),width=0.2,label="2005")


ax1.set(title="Product Sale", xlabel='Product Line',ylabel='Number of Sales')
ax1.set_xticks(X_axis, products_line2003.index.tolist())
ax1.legend()


#Second Axis
#Retrieve Deal Size in 2003
deal_size2003 = filtered_record_per_year_2003.groupby('DEALSIZE').size()

#Retrieve Deal Size in 2004
deal_size2004 = filtered_record_per_year_2004.groupby('DEALSIZE').size()

#Retrieve Deal Size in 2004
deal_size2005 = filtered_record_per_year_2005.groupby('DEALSIZE').size()

#Set the range of x-axis
X2_axis = [1,2,3]
width=0.20

# plot a subplot in a 2nd chart
ax2.bar([x-width for x in X2_axis], deal_size2003.tolist(),width=0.2,label="2003")

ax2.bar(X2_axis, deal_size2004.tolist(),width=0.2,label="2004")

ax2.bar([x+width for x in X2_axis], deal_size2005.tolist(),width=0.2,label="2005")

ax2.set(title="Deal Size", xlabel='Deal Size',ylabel='Number of Sales')
ax2.set_xticks(X2_axis, deal_size2003.index.tolist())
ax2.legend()


plt.show()


# ### Third axis: Proportion of Country

# In[32]:


#Retrieve product line sale in 2003
products_line2003 = filtered_record_per_year_2003.groupby('PRODUCTLINE').size()

#Retrieve product line sale in 2004
products_line2004 = filtered_record_per_year_2004.groupby('PRODUCTLINE').size()

#Retrieve product line sale in 2005
products_line2005 = filtered_record_per_year_2005.groupby('PRODUCTLINE').size()

#Create figure and get the axes

fig , (ax1,ax2,ax3) = plt.subplots(3,1, figsize = (12,15))

#Add title for entire figure
fig.suptitle("The customer analysis")

#Set the range of x-axis
X_axis = [1,2,3,4,5,6,7]
width=0.20

#plot a bar chart where the year 2004 is positioned at the center 
#of the x-axis for each product line
ax1.bar([x-width for x in X_axis], products_line2003.tolist(),width=0.2,label="2003")

ax1.bar(X_axis, products_line2004.tolist(),width=0.2,label="2004")

ax1.bar([x+width for x in X_axis], products_line2005.tolist(),width=0.2,label="2005")
ax1.set(title="Product Sale", xlabel='Product Line',ylabel='Number of Sales')
ax1.set_xticks(X_axis, products_line2003.index.tolist())
ax1.legend()


#Second Axis
#Retrieve Deal Size in 2003
deal_size2003 = filtered_record_per_year_2003.groupby('DEALSIZE').size()

#Retrieve Deal Size in 2004
deal_size2004 = filtered_record_per_year_2004.groupby('DEALSIZE').size()

#Retrieve Deal Size in 2004
deal_size2005 = filtered_record_per_year_2005.groupby('DEALSIZE').size()


#Set the range of x-axis
X2_axis = [1,2,3]
width=0.20

# plot a subplot in a 2nd chart
ax2.bar([x-width for x in X2_axis], deal_size2003.tolist(),width=0.2,label="2003")

ax2.bar(X2_axis, deal_size2004.tolist(),width=0.2,label="2004")

ax2.bar([x+width for x in X2_axis], deal_size2005.tolist(),width=0.2,label="2005")

ax2.set(title="Deal Size", xlabel='Deal Size',ylabel='Number of Sales')
ax2.set_xticks(X2_axis, deal_size2003.index.tolist())
ax2.legend()

#Third Axis
# plot a subplot in a 3rd chart
countrys=df_sales.groupby('COUNTRY').size()
ax3.pie(countrys.tolist(),labels=countrys.index.tolist(),autopct='%.2f%%')
ax3.set(title="Country")

plt.legend(bbox_to_anchor=(1.2,1))


plt.show()


# ## Save subplot

# <font size=3>We can save the figure as follows. The bbox_inches = "tight" will eliminate the white space around the saved image.</font>

# In[33]:


#Saving the figure to png
fig.savefig("Customer_Analysis.png", bbox_inches = "tight")


# ***

# # Summary

# - <font size=3>Subplots mean a group of smaller axes (where each axis is a plot) that can exist together within a single figure.</font>
# - <font size=3>Function <span style="color:blue;"><b>subplot()</b></span> is used to creates a single subplot within a grid</font>
# - <font size=3>Function <span style="color:blue;"><b>subplots()</b></span> is used to creates a figure and a grid of subplots with a single call</font>
# 

# ***
