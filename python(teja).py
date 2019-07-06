#!/usr/bin/env python
# coding: utf-8

# In[2]:


n='100'
print(len(n))


# In[3]:


# find the greater of three numbers
a1=int(input("enter first number"))
a2=int(input("enter second number"))
a3=int(input("enter third number"))
if a1>a2 and a1>a3:
    print(a1,"is the large number")
if a2>a1 and a2>a3: 
    print(a2,"is the large number")
if a3>a1 and a3>a2:
    print(a3,"is the large nbumber")


# In[4]:


#check if a year is leap year or not
year=int(input("enter year"))
if (year%4==0 and year!=0):
    print("leap year")
else:
    print("it is not a leap year")


# # itteration 
# -while
# -for
# syntax:while boolean_condition:
#         statements
#         increment/decrement

# In[5]:


# Need to print "gitam "for five times
i=0
while i<5:
    print("gitam")
    i=i+1


# In[6]:


# Print N natural numbers using while loop
#input -10
n=int(input("enter the number"))
i=1
while i<=n:
    print(i,end = " ")
    i=i+1


# In[7]:


# REad a number  n
#add only even numbers between 1 to n
#input  10
#output  30
n=int(input("enter n value"))
i=1
sum=0
while i<=n:
    if i%2==0:
        sum=sum+i
    i=i+1
print(sum)
      
    


# In[8]:


# Number as a Number   123
#print the digits of gven number : 321
n=int(input("enter the number"))
while n!= 0:
    r=n%10
    print(r,end = " ")
    n=n//10


# # functional programming
# -simple
# -easy read
# -lengthy progrm divides into sub programs

# def nameoffunction(<parameters>):
#     satement
#     return
# nameofunction()

# In[ ]:


#read a number  1234
#output  6(2+4)
def add(n):
    #statements to compute the out piut of the program
    while n!=0
    return
add()


# In[10]:


n='5'
print(type(n))


# In[11]:


n=1+2**3/4*5
print(n)


# In[14]:


# read a nmber input
#output reverse of the given number
#123   ---   321
def reversenumber(n):
    rev=0
    while n!=0:
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev
reversenumber(123)


# In[ ]:




