
# ## Exercises

# Answer the questions or complete the tasks outlined in bold below.
import numpy as np

def power(a,b):
  a,b=tuple(map(int,input().split()))
  return a**b



def split_str(s):
 s=input()
  

 return s.split()


def format(planet,diameter):
 planet,diameter=tuple(input().split())



 return "The diameter of {} is {} kilometers.".format(planet,diameter)



def indexing(lst):
    
# ** Given this nested list, use indexing to grab the word "hello" **

#lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
 lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]


 return lst[3][1][2]


def dictionary(d):
    
# ** Given this nested dictionary grab the word "hello". Be prepared, this will be annoying/tricky **

# d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
 d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}



 return d['k1'][3]['tricky'][3]['target'][3]


def subjective():
    
# ** What is the main difference between a tuple and a list? **
# Tuple is _______

    return "Tuple is immutable whereas List is mutable"
subjective()



def domainGet(email):
    
    # ** Create a function that grabs the email website domain from a string in the form: **
# 
#     user@domain.com
#     
# **So for example, passing "user@domain.com" would return: domain.com**
 email="user@domain.com" 

 return email[email.index('@')+1:]


def findDog(st):
    
# ** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **
 st=input()

 return "dog" in st


def countDog(st):

# ** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **


    return st.count("dog")
222


def lambdafunc(seq):

 f = lambda x:

seq=list(input().split())

return f(seq)


def caught_speeding(speed, is_birthday):

 if is_birthday:
    if speed<=60:
       return "No Ticket"
    elif speed>60 and speed<=80:
      return "Small Ticket"
    else:
     return "Big Ticket"  
 else:
    if speed<=65:
        return "No Ticket"
    elif speed>65 and speed<=85:
        return "Small Ticket"
    else:
      return "Big Ticket"
print(caught_speeding(int(input()),bool(input())))

## Numpy Exercises

import numpy as np


def create_arr_of_fives():
    
  #### Create an array of 10 fives
  #### Convert your output into list 
  #### e.g return list(arr) 
 arr=np.random.normal(5,0,10).astype(int)
    
  
return type(arr)


 ### Create an array of all the even integers from 10 to 50
  ### Convert your output into list 
  ### e.g return list(arr) 

def even_num():
  arr=np.array(range(10,51,2))
  arr=arr.tolist()
  
  return arr



def create_matrix():
    
  ### Create a 3x3 matrix with values ranging from 0 to 8
  ### Convert your output into list 
  ### e.g return (arr).tolist()
  arr=np.arange(0,9).reshape(3,3)
  arr=arr.tolist()
  


  return arr



def linear_space():
    
  ### Create an array of 20 linearly spaced points between 0 and 1
  ### Convert your output into list 
  ### e.g return list(arr) 
  arr=np.linspace(0,1,20)
  

  return arr.tolist()



def decimal_mat():
    
  ### Create an array of size 10*10 consisting of numbers from 0.01 to 1
  ### Convert your output into list 
  ### e.g return (arr).tolist()

  return None



def slices_1():
    
  # This is a given array
  arr = np.arange(1,26).reshape(5,5)
  # array([[ 1,  2,  3,  4,  5],
  #      [ 6,  7,  8,  9, 10],
  #      [11, 12, 13, 14, 15],
  #      [16, 17, 18, 19, 20],
  #      [21, 22, 23, 24, 25]])
 li=[" "]
 li.extend(list(tuple(arr[[2,1]:])))
  ### Convert your output into list 
  ### e.g return (arr).tolist()
  # array([[12, 13, 14, 15],
  #      [17, 18, 19, 20],
  #      [22, 23, 24, 25]])

  return None



def slices_2():
    
  # This is a given array
  arr = np.arange(1,26).reshape(5,5)
  # array([[ 1,  2,  3,  4,  5],
  #      [ 6,  7,  8,  9, 10],
  #      [11, 12, 13, 14, 15],
  #      [16, 17, 18, 19, 20],
  #      [21, 22, 23, 24, 25]])

  # Write a code to slice this given array
  ### Convert your output into list 
  ### e.g return (arr).tolist()
  # array([[ 2],
  #      [ 7],
  #      [12]])

  return None 



def slices_3():
    
  # This is a given array
  arr = np.arange(1,26).reshape(5,5)
  # array([[ 1,  2,  3,  4,  5],
  #      [ 6,  7,  8,  9, 10],
  #      [11, 12, 13, 14, 15],
  #      [16, 17, 18, 19, 20],
  #      [21, 22, 23, 24, 25]])

  # Write a code to slice this given array
  ### Convert your output into list 
  ### e.g return (arr).tolist()
  # array([[16, 17, 18, 19, 20],
  #      [21, 22, 23, 24, 25]])
    
  return None 


# Great job!
