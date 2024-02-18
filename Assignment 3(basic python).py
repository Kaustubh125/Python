#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Q1. Write a Python Program to Check if a Number is Positive, Negative or Zero

num=int(input("Enter the number:"))
if num > 0:
    print("The number ",num," is Positive Number.")
elif num == 0:
    print("The number is Zero.")
else:
    print("The number ",num," is Negative Number.")


# In[6]:


# Q2. Write a Python Program to Check if a Number is Odd or Even

num = int(input("Enter the Number:"))

if num % 2 == 0 :
    print("The number",num,"is EVEN.")
else:
    print("The number",num,"is ODD.")


# In[10]:


# Q3. Write a Python Program to Check Leap Year
year=int(input("Enter the Year:"))
if (year % 400 == 0) and (year % 100 == 0):
    print(year,"is leap year")
elif (year % 4 == 0) and (year % 100 != 0):
    print(year,"is leap year")
else:
    print(year,"is not is leap Year")


# In[1]:


# Q4. Write a Python Program to Check Prime Number.

num = int(input("Enter the number:"))
if num > 1:
    for i in range(2,num):
        if num % i == 0 :
            print(num,"is not a prime number.")
            break
        else:
            print(num,"is a prime number.")
            break
elif num == 1:
    print(num,"is not a prime number.")
else:
    print(num,"is not a prime number")


# In[9]:


# Q5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000

start = 1 
end = 10000

print("Prime numbers between", start, "and", end, "are:")

for num in range(1,10001):
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                break
        else:
            print(num)

        
            


# In[4]:


print(1,10)


# In[ ]:




