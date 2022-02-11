
# ## Exercises

# Answer the questions or complete the tasks outlined in bold below.


def power(a,b):
    return a**b
    
    
    # ** What is 7 to the power of 4?**
    
    



def split_str(s):
    return  s.split(' ')
    
    
    # ** Split this string:**
# 
#     s = "Hi there Sam!"
#     
# **into a list. **

    


def format(planet,diameter):
     planetary_info = "The diameter of {one} is {two} kilometers."
     info = planetary_info.format(one=planet,two=diameter)
     return info
    
    
# ** Given the variables:**
# 
#     planet = "Earth"
#     diameter = 12742
# 
# ** Use .format() to print the following string: **
# 
#     The diameter of Earth is 12742 kilometers.

    



def indexing(lst):
    a = lst[3][1][2][0]
    return a
      
      
    
# ** Given this nested list, use indexing to grab the word "hello" **

#lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]

    


def dictionary(d):
    info1 = d['k1']
    info2=info1[3]
    info3=info2['tricky']
    info4=info3[3]
    info5=info4['target']
    info6=info5[3]
    return info6
    
# ** Given this nested dictionary grab the word "hello". Be prepared, this will be annoying/tricky **

# d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}


    


def subjective():
     reult = "immutable"
     return reult
    
# ** What is the main difference between a tuple and a list? **
# Tuple is _______

    




def domainGet(email):
    result = email.split('@')[1]
    return str(result)
    
    # ** Create a function that grabs the email website domain from a string in the form: **
# 
#     user@domain.com
#     
# **So for example, passing "user@domain.com" would return: domain.com**

    


def findDog(st):
     keyword = 'dog'
     if keyword in st:
       return True
       
    
# ** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **

    


def countDog(st):
    times = st.count('dog')
    return times

# ** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **

    



def lambdafunc(seq):
     a=list(filter(lambda x: x.startswith("s"), seq)) 
     return a
    
    # ** Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:**
# 
#     seq = ['soup','dog','salad','cat','great']
# 
# **should be filtered down to:**
# 
#     ['soup','salad']

    


def caught_speeding(speed, is_birthday):
     if is_birthday == True:
        if speed <= 65:
           a ="No Ticket"
           return a
        elif speed <= 85:
            a1 = "Small Ticket"
            return a1
        elif speed>= 86:
           a2 = "Big Ticket"
     else:        
          if speed <= 60:
             a ="No ticket"
             return a
          elif  speed <= 80:
                  a1 = "Small Ticket"
                  return a1
          elif speed>= 81:
              a2 = "Big Ticket"
              return a2  
      
    
    
# **You are driving a little too fast, and a police officer stops you. Write a function
#   to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". 
#   If your speed is 60 or less, the result is "No Ticket". If speed is between 61 
#   and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big    Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all 
#   cases. **

    


## Numpy Exercises

import numpy as np


def create_arr_of_fives():
     arr=np.ones(10)*5
     return list(arr)

    
  #### Create an array of 10 fives
  #### Convert your output into list 
  #### e.g return list(arr) 

  



def even_num():
     arr=np.arange(10,52,2)
     return list(arr)

    
  ### Create an array of all the even integers from 10 to 50
  ### Convert your output into list 
  ### e.g return list(arr) 

  



def create_matrix():
    arr=np.arange(0,9).reshape(3,3)
    return arr.tolist()

  ### Create a 3x3 matrix with values ranging from 0 to 8
  ### Convert your output into list 
  ### e.g return (arr).tolist()

  



def linear_space():
     arr=np.linspace(0,1,20)
     return list(arr)
    
  ### Create an array of 20 linearly spaced points between 0 and 1
  ### Convert your output into list 
  ### e.g return list(arr) 




def decimal_mat():
    arr=np.linspace(1,100,100).reshape(10,10)/100
    return arr.tolist()
    
  ### Create an array of size 10*10 consisting of numbers from 0.01 to 1
  ### Convert your output into list 
  ### e.g return (arr).tolist()

  



def slices_1():
    arr = np.arange(1,26).reshape(5,5)[2:,1:]
    return (arr).tolist()

    
  # This is a given array
  
  # array([[ 1,  2,  3,  4,  5],
  #      [ 6,  7,  8,  9, 10],
  #      [11, 12, 13, 14, 15],
  #      [16, 17, 18, 19, 20],
  #      [21, 22, 23, 24, 25]])

  # Write a code to slice this given array
  ### Convert your output into list 
  ### e.g return (arr).tolist()
  # array([[12, 13, 14, 15],
  #      [17, 18, 19, 20],
  #      [22, 23, 24, 25]])

  



def slices_2():
     arr = np.arange(1,26).reshape(5,5)[0:3,1:2]
     return (arr).tolist()

    
  # This is a given array
  
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

   



def slices_3():
     arr = np.arange(1,26).reshape(5,5)[3:]
     return (arr).tolist()

    
  # This is a given array
  
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
    
 


# Great job!
