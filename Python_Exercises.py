# -*- coding: utf-8 -*-
"""python_solutions.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13L5La0uzN71N5pM1pZdwkboPhkqPRgcA
"""

def power(a,b):
    
    # ** What is 7 to the power of 4?**
    
    return (a**b)

out= power(7,4)
print(out)

def split_str(s):
    
    # ** Split this string:**
     
#     s = "Hi there Sam!"
     
# **into a list. **

    return list(s.split())

s1= split_str( "Hi there Sam!")
print(s1)

def format(planet,diameter):
  return ("The diameter of {} is {} kilometers".format(planet,diameter))

planet="earth"
diameter = 12742
print(format(planet,diameter))

def indexing(lst):

# ** Given this nested list, use indexing to grab the word "hello" **
# solution:
  return lst[3][1][2][0]

lst= [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(indexing(lst))

def dictionary(d):                                                                               
# ** Given this nested dictionary grab the word "hello". Be prepared, this will be annoying/tricky **

 
 # solution :
 return d['k1'][3]['tricky'][3]['target'][3]

d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
print(dictionary(d))

def subjective():

# ** What is the main difference between a tuple and a list? **
# Tuple is immutable 
#whereas list are mutable meaning the items can be changed 

    return None

def domainGet(email):
    
    # ** Create a function that grabs the email website domain from a string in the form: **
# 
#     user@domain.com
#     
# **So for example, passing "user@domain.com" would return: domain.com**
  k = email.index("@")
  return email[k+1:]

s = 'user@domain.com'
print(domainGet(s))

#or another method 
def DomainGet(email):

   
  return  email.split("@")[1]

e = "user@domain.com"
print(DomainGet(e))

def findDog(st):
    
# ** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **
  
  if("dog" in st):
    return True
  else:
    return False

findDog("this is cute dog")

def countDog(st):

  return(len(list(filter(lambda item: item == "dog" , st.split()))))
      
    # ** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **

st = " the  dog car is dog cool  is the full dog"
print(countDog(st))

# Another method 
#for Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases
def CountDog(pt):
      m=0
      for i in range(len(pt)):
    # ** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **
         if (pt[i] == 'd'and pt [i+1]== 'o'and pt [i+2]=='g'):
          m+=1
      return m

pt = "this is   a cute dog, i love this dog "
print(CountDog(pt))

def lambdafunc(seq):
    
    # ** Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:**
# 
#     seq = ['soup','dog','salad','cat','great']
  l =list(filter(lambda item: item[0] == "s",seq))
  return (l)
# **should be filtered down to:**
# 
#     ['soup','salad']

seq = ['soup','dog','salad','cat','great']
print(lambdafunc(seq))

def caught_speeding(speed, is_birthday):
  if(is_birthday==True):
        i = 5

  else:
        i = 0

  if(speed<=60+i):
        return "No Ticket"

  elif(speed>=61+i and speed<=80+i):
        return "Small Ticket"

  elif(speed>=81+i):
        return "Big Ticket"

#example
print(caught_speeding(62, True))

"""# numpy part

"""

!pip install numpy
import numpy as np

def create_arr_of_fives():

  #### Create an array of 10 fives
  #### Convert your output into list 
  arr = np.array([5,5,5,5,5,5,5,5,5,5])
  #### e.g return list(arr) 

  return list(arr)

print(create_arr_of_fives())

def even_num(p):

  ### Create an array of all the even integers from 10 to 50
  ### Convert your output into list 
  ### e.g return list(arr) 
  p= (np.arange(10,51))
  arr= filter(lambda item: item%2 == 0,p)
  return list(arr)

print( even_num(p))

def create_matrix():

  ### Create a 3x3 matrix with values ranging from 0 to 8
  ### Convert your output into list 
  ### e.g return (arr).tolist()
  arr = np.arange(0,9).reshape(3,3)

  return (arr).tolist()

print(create_matrix())

def linear_space():

  ### Create an array of 20 linearly spaced points between 0 and 1
  ### Convert your output into list 
  ### e.g return list(arr) 
  arr = np.linspace(0,1,20)
  return list(arr)

print(linear_space())

def decimal_mat():

  ### Create an array of size 10*10 consisting of numbers from 0.01 to 1
  ### Convert your output into list 
  ### e.g return (arr).tolist()
  arr= np.linspace(0.01,1,100).reshape(10,10)
  return arr.tolist()

print(decimal_mat())

def slices_1():

  # This is a given array
  arr = np.arange(1,26).reshape(5,5)
  # array([[ 1,  2,  3,  4,  5],
  #      [ 6,  7,  8,  9, 10],
  #      [11, 12, 13, 14, 15],
  #      [16, 17, 18, 19, 20],
  #      [21, 22, 23, 24, 25]])

  # Write a code to slice this given array
  ### Convert your output into list 
  q = arr[ 2: , 1: ]
  ### e.g return (arr).tolist()
  # array([[12, 13, 14, 15],
  #      [17, 18, 19, 20],
  #      [22, 23, 24, 25]])

  return (q).tolist()

print(slices_1())

def slices_2():

  # This is a given array
  arr = np.arange(1,26).reshape(5,5)
  # array([[ 1,  2,  3,  4,  5],
  #      [ 6,  7,  8,  9, 10],
  #      [11, 12, 13, 14, 15],
  #      [16, 17, 18, 19, 20],
  #      [21, 22, 23, 24, 25]])
  r = arr[ :3 , 1:2 ]
  # Write a code to slice this given array
  ### Convert your output into list 
  ### e.g return (arr).tolist()
  # array([[ 2],
  #      [ 7],
  #      [12]])

  return (r).tolist()

print(slices_2())

def slices_3():

  # This is a given array
  arr = np.arange(1,26).reshape(5,5)
  # array([[ 1,  2,  3,  4,  5],
  #      [ 6,  7,  8,  9, 10],
  #      [11, 12, 13, 14, 15],
  #      [16, 17, 18, 19, 20],
  #      [21, 22, 23, 24, 25]])
  w = arr[ 3: , :5 ]
  # Write a code to slice this given array
  ### Convert your output into list 
  ### e.g return (arr).tolist()
  # array([[16, 17, 18, 19, 20],
  #      [21, 22, 23, 24, 25]])

  return (w).tolist()


# Great job!

print(slices_3())

# it was fun really enjoyed !! :))