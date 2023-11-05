#!/usr/bin/env python
# coding: utf-8

# If_else Statement

# In[1]:


# activity by user input

activity = input("Please enter the activity to be performed: ")

#  "calculate" the activity
if activity.lower() == "calculate":
    # If it is "calculate," display a specific message
    print("Performing calculations...")
    
else:
    # general message display
    print("Performing activity...")

# completion message display
print("Activity completed!")


# In[ ]:





#  'if_elif_else statement'

# In[2]:


#  user's input for the direction

direction = input("Towards which direction should I paint (up, down, left, or right)? ")

#  provide a suitable message
if direction.lower() == "up":
    print("I am painting in the upward direction!")
elif direction.lower() == "down":
    print("I am painting in the downward direction!")
elif direction.lower() == "left":
    print("I am painting in the leftward direction!")
elif direction.lower() == "right":
    print("I am painting in the rightward direction!")
else:
    print("Invalid direction. Please choose up, down, left, or right for painting.")


# In[4]:


#user's input for the direction

direction = input("Towards which direction should I paint (up, down, left, or right)? ")

#  provide a suitable message
if direction.lower() == "up":
  print("I am painting in the upward direction!")
elif direction.lower() == "down":
  print("I am painting in the downward direction!")
elif direction.lower() == "left":
  print("I am painting in the leftward direction!")
elif direction.lower() == "right":
  print("I am painting in the rightward direction!")
else:
  print("Invalid direction. Please choose up, down, left, or right for painting.")


# Modulo_Operator

# In[6]:


# input for a whole number
number = int(input("Please enter a whole number: "))

# Check the odd number using the modulo operator (%)
if number % 2 == 0:
    print(f"The number {number} is an even number.")
else:
    print(f"The number {number} is an odd number.")


# Comparison_Operator

# In[7]:


# input for the first number by user

first_number = float(input("Please enter the first number: "))

# input for the second number by user
second_number = float(input("Please enter the second number: "))

# number comparison with  display an appropriate message

if first_number < second_number:
    print("The first number is the smallest!")
elif second_number < first_number:
    print("The second number is the smallest!")
else:
    print("Both are equal!")


# In[ ]:




