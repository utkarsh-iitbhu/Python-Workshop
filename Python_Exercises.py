
# ## Exercises

# Answer the questions or complete the tasks outlined in bold below.


def power(a,b):
    # ** What is 7 to the power of 4?**
  return a**b
print(power(7,4))



def split_str(s):
      # ** Split this string:**
# 
#     s = "Hi there Sam!"
#     
# **into a list. **
  return s.split()
print(split_str("Hi there Sam!"))
 





def format(planet,diameter):
  # ** Given the variables:**
# 
#     planet = "Earth"
#     diameter = 12742
# 
# ** Use .format() to print the following string: **
# 
#     The diameter of Earth is 12742 kilometers.
  return None
planet = "Earth"
diameter = 12742
print("The diameter of {one} is {two} kilometers.".format(one = planet , two = diameter))
    

def indexing(lst):
    
# ** Given this nested list, use indexing to grab the word "hello" **

#lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]

    return None
lst=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(lst[3][1][2][0])



def dictionary(d):
    
# ** Given this nested dictionary grab the word "hello". Be prepared, this will be annoying/tricky **

# d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}



    return None

d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
dic1 = d['k1'][3]
dic2 = (dic1['tricky'][3])
print(dic2['target'][3])


def subjective():
    
# ** What is the main difference between a tuple and a list? **
# Tuple is _immutable_

    return None




def domainGet(email):
    
    # ** Create a function that grabs the email website domain from a string in the form: **
# 
#     user@domain.com
#     
# **So for example, passing "user@domain.com" would return: domain.com**

    return email.split('@')
dom = input("Enter your email website domain ")
print(domainGet(dom)[1])




def findDog(st):
    
# ** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **

    return "dog" in st.lower().split()
stat = input("Enter an input statement ")
print(findDog(stat))



def countDog(st):

# ** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **

    count = 0
    for word in st.lower().split():
        if word == 'dog':
            count = count+1
    return count
stat = input("Enter an input statement ")
print(countDog(stat))



def lambdafunc(seq):
    
    # ** Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:**
# 
#     seq = ['soup','dog','salad','cat','great']
# 
# **should be filtered down to:**
# 
#     ['soup','salad']

    return None
seq = ['soup','dog','salad','cat','great']
output = list(filter(lambda letter: letter[0]=='s',seq))
print(output)


def caught_speeding(speed, is_birthday):
    
# **You are driving a little too fast, and a police officer stops you. Write a function
#   to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". 
#   If your speed is 60 or less, the result is "No Ticket". If speed is between 61 
#   and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big    Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all 
#   cases. **

  if is_birthday:
        fspeed = speed - 5
  else:
        fspeed = speed
    
  if  fspeed > 80:
        return 'Big Ticket'
  elif fspeed > 60:
        return 'Small Ticket'
  else:
        return 'No Ticket'
print(caught_speeding(81,True))
print(caught_speeding(81,False))

## Numpy Exercises

import numpy as np


def create_arr_of_fives():
    
  #### Create an array of 10 fives
  #### Convert your output into list 
  #### e.g return list(arr) 
  return None
array = np.ones(10)*5
print("An array of 10 fives: " )
print(array)
print("List: ")
print(array.tolist())


import numpy as np

def even_num():
    
  ### Create an array of all the even integers from 10 to 50
  ### Convert your output into list 
  ### e.g return list(arr) 

  return None
array=np.arange(10,51,2)
print("Array of all the even integers from 10 to 50: ")
print(array)
print("List: ")
print(array.tolist()) 


import numpy as np

def create_matrix():
    
  ### Create a 3x3 matrix with values ranging from 0 to 8
  ### Convert your output into list 
  ### e.g return (arr).tolist()

  return None
matrix = np.arange(0,9).reshape(3,3)
print("A 3x3 matrix with values ranging from 0 to 8: ")
print(matrix)
print("List: ")
print(matrix.tolist())


import numpy as np

def linear_space():
    
  ### Create an array of 20 linearly spaced points between 0 and 1
  ### Convert your output into list 
  ### e.g return list(arr) 

  return None
array = np.linspace(0,1,20)
print("An array of 20 linearly spaced points between 0 and 1: ")
print(array)
print("List: ")
print(array.tolist())




import numpy as np

def decimal_mat():
    
  ### Create an array of size 10*10 consisting of numbers from 0.01 to 1
  ### Convert your output into list 
  ### e.g return (arr).tolist()

  return None
array = np.linspace(0.01,1,100).reshape(10,10)
print("an array of size 10*10 consisting of numbers from 0.01 to 1: ")
print(array)
print("List: ")
print(array.tolist())




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
  ### e.g return (arr).tolist()
  # array([[12, 13, 14, 15],
  #      [17, 18, 19, 20],
  #      [22, 23, 24, 25]])

  return None
arr = np.arange(1,26).reshape(5,5)
print(arr[2:, 1:])
print("List: ")
print(arr[2:, 1:].tolist())



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
arr = np.arange(1,26).reshape(5,5)
print(arr[:3,1:2])
print("List: ")
print(arr[:3,1:2].tolist())



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
arr = np.arange(1,26).reshape(5,5)
print(arr[3:5, : ])
print("List: ")
print(arr[3:5, : ].tolist())


# Great job!
