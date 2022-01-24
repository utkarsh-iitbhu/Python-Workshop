#!/usr/bin/env python
# coding: utf-8

# ## Exercises
# 
# Answer the questions or complete the tasks outlined in bold below.

# ** What is 7 to the power of 4?**

# In[ ]:


def power(a,b):
    ans = # a**b
    return ans


# In[1]:





# ** Split this string:**
# 
#     s = "Hi there Sam!"
#     
# **into a list. **

# In[2]:


def split(s):
    l = 
    return l 


# In[3]:





# ** Given the variables:**
# 
#     planet = "Earth"
#     diameter = 12742
# 
# ** Use .format() to print the following string: **
# 
#     The diameter of Earth is 12742 kilometers.

# In[3]:


planet = "Earth"
diameter = 12742


# In[6]:


def format(planet,diameter):
    a = 
    return print(a)


# In[6]:





# ** Given this nested list, use indexing to grab the word "hello" **

# In[7]:


lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]


# In[8]:


def indexing(lst):
    a = 
    return a


# In[14]:





# ** Given this nested dictionary grab the word "hello". Be prepared, this will be annoying/tricky **

# In[9]:


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}


# In[10]:


def dict(d):
    ans = 
    return ans 


# In[22]:





# ** What is the main difference between a tuple and a list? **

# In[23]:


def subjective():
    s = 
    return s
# Tuple is _______


# ** Create a function that grabs the email website domain from a string in the form: **
# 
#     user@domain.com
#     
# **So for example, passing "user@domain.com" would return: domain.com**

# In[ ]:


def domainGet(email):
    ans = 
    return ans


# In[24]:





# In[26]:


domainGet('user@domain.com')


# ** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **

# In[ ]:


def findDog(st):
    ans = 
    return ans


# In[27]:





# In[28]:


findDog('Is there a dog here?')


# ** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **

# In[ ]:


def countDog(st):
    count = 
    return count


# In[30]:





# In[31]:


countDog('This dog runs faster than the other dog dude!')


# ** Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:**
# 
#     seq = ['soup','dog','salad','cat','great']
# 
# **should be filtered down to:**
# 
#     ['soup','salad']

# In[11]:


seq = ['soup','dog','salad','cat','great']


# In[14]:


def lambdafunc(seq):
    ans = 
    return ans


# In[35]:





# ### Final Problem
# **You are driving a little too fast, and a police officer stops you. Write a function
#   to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". 
#   If your speed is 60 or less, the result is "No Ticket". If speed is between 61 
#   and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big    Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all 
#   cases. **

# In[15]:


def caught_speeding(speed, is_birthday):
    ans = 
    return ans 


# In[36]:


# def caught_speeding(speed, is_birthday):
#     pass


# In[42]:


caught_speeding(81,True)


# In[43]:


caught_speeding(81,False)


# # Great job!
