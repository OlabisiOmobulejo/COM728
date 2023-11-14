#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import the pandas library and aliasing as pd
import pandas as pd

age = ["adult","adult","child","child"]
print(age)

#load the list as data into a Series function
s = pd.Series(age)

#display the Series
print(f"\nSeries:\n{s}")


# In[2]:


#import the pandas library and aliasing as pd
import pandas as pd

age = ["adult","adult","child","child"]

#load the list as data into a Series function
s = pd.Series(age, index=[100,101,102,103])

#display the Series
print(f"Series:\n{s}")


# In[3]:


#import the pandas library and aliasing as pd
import pandas as pd

data = {'a' : 0., 'b' : 1., 'c' : 2.}
print(data)

# load the dictionary as data into a Series function
s = pd.Series(data)

#display the Series
print(f"Series:\n{s}")


# In[4]:


#import the pandas library and aliasing as pd
import pandas as pd

age = ["adult","adult","child","child"]
data = {'a' : 0., 'b' : 1., 'c' : 2.}

#load the list as data into a Series function
s1 = pd.Series(age)

#load the dictionary as data into a Series function
s2 = pd.Series(data)

#get the element by index number
print(f"An element of index 1 in a series-s1: {s1[1]}")

#get the element by  label
print(f"An element of label b in a series-s2: {s2['b']}")


# In[7]:


import pandas as pd
data = [['Alex',10,22.5],['Bob',12,8.9],['Clarke',13,34.6]]

#load data into a DataFrame object with specify column name
df = pd.DataFrame(data,columns=['Name','Age','weight'])

#display the DataFrame
df


# In[6]:


import pandas as pd

#create a data object
data = {
    "colors": ['red', 'green', 'blue', 'orange', 'purple', 'yellow'],
    "votes": [3, 6, 2, 3, 1, 4],
    "cars": [1, 2, 1, 1, 2, 1]
}

#load data into a DataFrame object
df = pd.DataFrame(data)

#display the DataFrame
df 


# In[8]:


import pandas as pd

# Load data from a csv to dataframe and set the first row to be column names
df=pd.read_csv("Data/Grades.csv", header=0, encoding='utf-8')

# display a dataframe
df


# In[9]:


import pandas as pd

# Load data from a csv to dataframe and set the first row to be column names and first column to be an index
df_set_index =pd.read_csv("Data/Grades.csv", header=0, encoding='utf-8', index_col='Name')

# display a dataframe
df_set_index


# In[10]:


import pandas as pd

# Load data from a csv to dataframe and set the first row to be column names
grade_df=pd.read_csv("Data/Grades.csv", header=0, encoding='utf-8')


# In[11]:


#Get the dimensions of the data frame
dimensions = grade_df.shape
print(f"DataFrame dimensions: {dimensions}")

numRows = dimensions[0]
numCols = dimensions[1]
print(f"Number of rows: {numRows}")
print(f"Number of columns: {numCols}")


# In[13]:


#Get the data type of each column
# object = string
# float64 = decimal
# int64 = integer
grade_df.dtypes


# In[14]:


#Display row names = index
grade_df.index


# In[15]:


#Display row names = index
grade_df.index


# In[16]:


import pandas as pd

# Load data from a csv to dataframe and set the first row to be column names
grade_df=pd.read_csv("Data/Grades.csv", header=0, encoding='utf-8')

#Extract a column: We can pick out a column by referencing its name (a string). 
#The result is a series or one dimensional data frame
grade_df['Name']


# In[17]:


print(type(grade_df['Name']))


# In[18]:


#You can similarly pick out columns as attributes with the '.'
grade_df.Name


# In[19]:


print(type(grade_df.Name))


# In[20]:


#You can pick out multiple columns by specifying a list of column names
#Column don’t have to be contiguous
df[['Name', 'Grade']]


# In[21]:


print(type(df [['Name', 'Grade']]))


# In[22]:


print(df[['Name', 'Grade']])


# In[23]:


student_grade = df[['Name', 'Grade']]
student_grade


# In[26]:


#Select Name, Final score and Grade
student_results = df[['Name','Final','Grade']]

#Here is how we write a dataframe
student_results.to_csv("Student_FinalScore_Grade.csv")


# In[27]:


import pandas as pd

#Read in a dataframe
grade_df=pd.read_csv("Data/Grades.csv", header=0, encoding='utf-8')

#Let's look at the data 
grade_df


# In[28]:


#Pick out a single entry from row index=3 and column name as Name
grade_df.loc[3,"Name"]


# In[29]:


#Pick out an entire row for specific row of index 0
grade_df.loc[0,:]


# In[30]:


#Select range of contiguous rows from row index 2 to 5 and columns name Mini_Exam3 to Grade
grade_df.loc[2:5, "Mini_Exam3":"Grade"]


# In[31]:


#Select none contiguous rows and  columns
grade_df.loc[[0,2,4], ['Previous_Part','Grade']]


# In[32]:


# Select first row of dataframe
grade_df.iloc[0]


# In[33]:


# Get the row number of value based on column
row_num = grade_df[grade_df['Name'] == 'Chris'].index.tolist()
print(row_num)

grade_df.iloc[row_num]


# In[34]:


# The dataframe is printed as markdown without the index column.
final_score_grade = grade_df.loc[:,['Name','Final','Grade']]

print(final_score_grade.to_string())


# In[35]:


# The dataframe is printed as markdown without the index column.
final_score_grade = grade_df.loc[:,['Name','Final','Grade']]

print(final_score_grade.to_markdown(index=False))


# In[37]:


# styling of whole table with the colour on the column name
final_score_grade.style.set_table_styles([{
                                            "selector":"thead",
                                            "props":"background-color:lightblue; color:white; border:3px"
                                            },])


# In[ ]:




