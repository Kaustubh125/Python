#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Python program to convert kilometers to miles
kilo=int(input("Enter the value in Kilometer:"))
#Formula
mile=0.621371*kilo
print("The value in miles is",mile)


# In[3]:


# Python program to convert Celsius to Fahrenheit
#Taking input from user
cels=int(input("Enter the value in Celsius to convert in Fahrenheit:"))
#Formula
fah=(cels*9/5)+32
print("The value in Fahrenheit is ",fah)


# In[7]:


# Python program to display calendar
import calendar

# To take month and year input from the user
yy = int(input("Enter year: "))
mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy, mm))


# In[3]:


# Python program to solve quadratic equation
# The quadratic equation ax**2 + bx + c = 0

a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
#the solution of Quadratic equation is given by
#(-b ± (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-(d))/(2*a)
sol2 = (-b+(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))


# In[6]:


#Python program to swap two variables without temp variable
a=input("a=")
b=input("b=")
print ("Before swapping: ")
print("Value of a : ", a, " and b : ", b)

a, b = b, a
 
print ("After swapping: ")
print("Value of a : ", a, " and b : ", b)

