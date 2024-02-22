#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Q1. Write a Python Program to Find the Factorial of a Number.
num = int(input("Enter the number:"))
facto = 1

if num < 1:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("The Factorial of 0 is 1.")
else:
    for i in range(1,num + 1):
        facto = facto * i
print("The factorial of",num,"is",facto)


# In[11]:


# Q2. Write a Python Program to Display the multiplication Table

num = int(input("Enter the Multiplication Table Number:"))

for i in range(1,11):
        table = num * i 
        print(num,"x",i,"=",table)


# In[7]:


# Q3. Write a Python Program to Print the Fibonacci sequence.
times = int(input("Enter the terms:"))

n1=0
n2=1
count = 0

if times <= 0:
    print("Enter positive value.")
elif times == 1:
    print("The Fibonacci Sequence:",n1)
else:
    while count < times:
        print(n1)
        nth = n1 +n2
        n1 = n2
        n2 = nth
        count = count + 1
        


# In[2]:


# Q4. Write a Python Program to Check Armstrong Number.
num=int(input("Enter the number to check Armstrong number:"))
temp = num
sum = 0
length = len(str(num))
while temp > 0:
    digit = temp % 10
    sum += digit ** length
    temp//=10
if sum == num:
    print("The Number",num,"is Armstrong Number")
else:
    print("The Number",num,"is not a Armstrong Number")


# In[6]:


# Q5. Write a Python Program to Find the Sum of Natural Numbers.

num1 = int(input("Enter the Natural Number1:"))
num2 = int(input("Enter the Natural Number2:"))
if num1 <= 0 or num2 <= 0:
    print("The enter numbers is not a natural number.")
else:
    sum = num1 + num2
    print("The sum of",num1,"+",num2,"=",sum)

