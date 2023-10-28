#!/usr/bin/env python
# coding: utf-8

# Display Information and personal data

# In[6]:


#display of personal information of users
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
location = input("Enter your location: ")
height_in_inches = float(input("Enter your height (in inches): "))  # Close the parenthesis here
year_of_birth = int(input("Enter your year of birth: "))  # Close the parenthesis here

# user information Display
print(f"First Name: {first_name.rjust(20)}")
print(f"Last Name: {last_name.ljust(20)}")
print(f"Location: {location.center(20)}")
print(f"Height: {height_in_inches:.4f}")
print(f"Year of Birth: {year_of_birth}")

# users greeting with the above information
greeting_message = f"Hello {first_name} {last_name} from {location}! You are {height_in_inches:.4f} inches tall and born in {year_of_birth}."
print(greeting_message)

