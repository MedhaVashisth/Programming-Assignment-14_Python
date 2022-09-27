#!/usr/bin/env python
# coding: utf-8

# In[1]:


n = int(input())
divBy7 = [i for i in range(0, n) if (i % 7 == 0)]
print(divBy7)

def divChecker(n):
    for i in range(n):
        if i % 7 == 0:
            value = True
        else:
            value = False
        print(i, value)

divChecker(n)


# In[4]:


import operator

text_line = input("Type in: ")

freq_dict = {}

for i in text_line.split(' '):
    if i.isalpha():
        if i not in freq_dict:
            freq_dict[i] = 1
        elif i in freq_dict:
            freq_dict[i] = freq_dict[i] + 1
    else:
        pass

sorted_freq_dict = sorted(freq_dict.items(), key = operator.itemgetter(0))
print(sorted_freq_dict)

for i in sorted_freq_dict:
    print(i[0], i[1])


# In[7]:


class Person(object):
    def getGender( self ):
        return "Unknown"

class Male( Person ):
    def getGender( self ):
        return "Male"

class Female( Person ):
    def getGender( self ):
        return "Female"

aMale = Male()
aFemale= Female()
print aMale.getGender()
print aFemale.getGender()


# In[8]:


"""
Problem Statement​ ​1:
Implement a Python program to generate all sentences where subject is in
["Americans", "Indians"] and verb is in ["Play", "watch"] and the object is in
["Baseball","cricket"].
Hint: Subject,Verb and Object should be declared in the program as shown below.
subjects=["Americans ","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]
Output should come as below:
Americans play Baseball.
Americans play Cricket.
Americans watch Baseball.
Americans watch Cricket.
Indians play Baseball.
Indians play Cricket.
Indians watch Baseball.
Indians watch Cricket.
"""

subject=["Americans", "Indians"]
verb=["Play", "watch"]
obj=["Baseball","cricket"]

# Use list comprehension instead of looping over each of the predicates
sentence_list = [(sub+" "+ vb + " " + ob) for sub in subject for vb in verb for ob in obj]
for sentence in sentence_list:
 print (sentence)


# In[12]:


import zlib
s = 'hello world!hello world!hello world!hello world!'
t = zlib.compress(s)
print (t)
print zlib.decompress(t)


# In[16]:


# import gzip and decompress
import gzip
s = 'hello world!hello world!hello world!hello world!'
s = zip.compress(s)

# using gzip.decompress(s) method
t = zip.decompress(s)
print(t)


# In[20]:


def binary_search(lst, item):
    low = 0
    high = len(lst) - 1
    
    while low <= high:
        mid = round((low + high) / 2)
        
        if lst[mid] == item:
            return mid
        elif lst[mid] > item:
            high = mid - 1
        else:
            low = mid + 1
    return None
    
lst = [1,3,5,7,]
print(binary_search(lst, 9))   


# In[ ]:




