#!/usr/bin/env python
# coding: utf-8

# "user_input"

# In[3]:


# Ask user to enter their name
print("what is your name human?")
name = input()
print(f"it is nice to meet you human {name}")


# In[20]:


# Read in user's name
name = input ("what is your name human?")


# Data Type

# In[22]:


# user input for name, age, weight, and height
name = input("Enter your name: ")
age = int(input("Enter your age (in years): "))
weight = float(input("Enter your weight (in kilograms): "))
height = float(input("Enter your height (in meters): "))

#  bmi calculations
bmi = weight / (height ** 2)

# bmi calculation result
bmi_result = f"Hello, {name}! You are {age} years old, and your BMI is {bmi:.2f}."
print(bmi_result)


# In[ ]:




