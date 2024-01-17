#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Python program to print "Hello Python"
print("Hello World")


# In[5]:


#Python program to do arithmetical operations addition and division.
a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
add = a+b
div = a/b
print(add)
print(div)


# In[7]:


#Python program to find the area of a triangle
base = int(input("Enter the value of base of triangle:"))
height = int(input("Enter the value of height of triangle:"))
area = 0.5*(base*height)
print("The Area of triangle=",area)


# In[11]:


#Python program to swap two variables
first_var=input("Enter any value:")
second_var=input("Enter any value to swap with first:")
temp=first_var
first_var=second_var
second_var=temp
print("The value of first variable after swapping:",first_var)
print("The value of second variable after swapping:",second_var)


# In[18]:


#Python program to generate a random number
import random
a=int(input("Enter the starting point:"))
b=int(input("Enter the ending point:"))
print(random.randint(a,b))




