#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Question 1
txt = "Hello World"
x = txt[2:5]
x


# In[4]:


#Question 2
txt = " Hello World"
x = txt[1:]
x


# In[5]:


#Question 3
txt = "hello world"
x = txt.upper()
x


# In[14]:


#Question 4
txt = "Hello World"
txt = txt.replace('H','J')
txt


# In[24]:


#Question 5
age = 36
txt = "My name is John and I am {age}" 
print(txt.format(age = age))


# In[25]:


#Quesstion 6
#Answer: True
a = 'coding'
b = 'hero'
print('dingh' in 2 * (a+b))


# In[29]:


#Question 7
s = "Hello"
x = s[-2:]
x


# In[41]:


#Quesiton 8
#Answer: A,B & D
#C is false
s = "Hello"
print(s is s[:]) #A
print(s[::-1][::-1] == s) #b
print(s[::-1][::-1] is s) #c
print(s[:] == s) #d


# In[1]:


#Question 9
#Answer: c
print(
    '$100 $200 $300'.count('$'),
    '$100 $200 $300'.count('$',5, 10),
    '$100 $200 $300'.count('$',5))


# In[6]:


#Question 10
#answer: a,b and d
s = 'coding-hero'
print(s.upper().lower())#a
print(s.strip('-')) #b
print('-'.join(s.partition('-'))) #c
print('-'.join(s.split('-'))) #d


# In[8]:


#question 11
print('coding' 'heroes')
print('coding ' 'hereoes')
print('codng' ' hereos')
print('coding hereos')


# In[9]:


#Question 12
#1. a,b,c,d


# In[17]:


#Question 13 
#Answer: B
a = 'hello world'
print(len(a)) #B


# In[20]:


#Question 14 
#Answer: 3
str = 'C:\Common\TestString.doc'
print(str)


# In[22]:


#Question 15
#Answer: d
str='good-BYE'
print(str.capitalize())


# In[24]:


#Question 16
#Answer: C
str = 'Hello World'
print (str.find('o'))


# In[25]:


#Question 17
str ='Coding Hero'
print(str[4:9])


# In[28]:


#Question 18
str = 'This is orange juice'
print(str.find('orange'))
print('orange' in str)


# In[32]:


#Question 19
#Write a program that takes your full name as input and displays the
#abbreviations of the first and middle names except the last name which is displayed as
#it is. For example, if your name is Robert Bred Rochser, then the output should be
#R.B.Rochser.

a = (input('enter your name'))
b = a.split(" ")
print(b[0][0],b[1][0],b[2])


# In[34]:


#Question 20
#20. Write a program to check if a given string is a Palindrome. A palindrome
#reads same from front and back e.g.- aba, ccaacc, mom, etc
s = "racecar"
a = s[::-1]
 
if a == s:
    print("Yes")
else:
    print("No")


# In[35]:


#Question 21
print(r"\ncodinghero")
print("\ncodinghero")


# In[43]:


#Question 22
#answer: B,c
az = 'an elephant'
print('e'.split(az,2)) #A
print(az.split('e', 2)) #B
print(az.split('e',maxsplit=2)) #C
print('e'.split(az,maxsplit=2)) #D


# In[ ]:


#Question 23. A price such as £3.65 should be saved as what kind of variable?
#Answer: float

