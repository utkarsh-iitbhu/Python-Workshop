
# ## Exercises

# Answer the questions or complete the tasks outlined in bold below.


def power(a,b):
    
    # ** What is 7 to the power of 4?**
    print(a**b)
    
    return None



def split_str(s):
    
    # ** Split this string:**
# 
#     s = "Hi there Sam!"
#     
# **into a list. **
    l=s.split()
    print(l)

    return None


def format(planet,diameter):
    
# ** Given the variables:**
# 
#     planet = "Earth"
#     diameter = 12742
# 
# ** Use .format() to print the following string: **
# 
#     The diameter of Earth is 12742 kilometers.
    print("The diameter of {} is {} kilometers.".format(planet,diameter))

    return None



def indexing(lst):
    
# ** Given this nested list, use indexing to grab the word "hello" **

#lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
    print(lst[3][1][2][0])

    return None


def dictionary(d):
    
# ** Given this nested dictionary grab the word "hello". Be prepared, this will be annoying/tricky **

# d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
    print(d['k1'][3]['tricky'][3]['target'][3])
    
    return None


def subjective():
    
# ** What is the main difference between a tuple and a list? **
# Tuple is _______
    print("The main difference between a tuple and a list is that tuples are immutable while lists are mutable.")
    print("This means that the items of a list can be modified which is not possible in case of tuples.")
    
    return None




def domainGet(email):
    
    # ** Create a function that grabs the email website domain from a string in the form: **
# 
#     user@domain.com
#     
# **So for example, passing "user@domain.com" would return: domain.com**
    print(email.split('@')[1])

    return None


def findDog(st):
    
# ** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **
    if ('dog' in st.lower().split()):
        print("True")
    else:
        print("False")

    return None


def countDog(st):

# ** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **
    count=0
    for item in st.lower().split():
        if (item=='dog'):
            count=count+1
    print(count)

    return None



def lambdafunc(seq):
    
    # ** Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:**
# 
#     seq = ['soup','dog','salad','cat','great']
# 
# **should be filtered down to:**
# 
#     ['soup','salad']
    print(list(filter(lambda item: item[0]=='s',seq)))

    return None


def caught_speeding(speed, is_birthday):
    
    
# **You are driving a little too fast, and a police officer stops you. Write a function
#   to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". 
#   If your speed is 60 or less, the result is "No Ticket". If speed is between 61 
#   and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big    Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all 
#   cases. **
    if(is_birthday==True):
        speed_equivalent=speed-5
    else:
        speed_equivalent=speed
    if(speed_equivalent<=60):
        print("No Ticket")
    elif(speed_equivalent>80):
        print("Big Ticket")
    else:
        print("Small Ticket")

    return None


## Numpy Exercises

import numpy as np


def create_arr_of_fives():
    
  #### Create an array of 10 fives
  #### Convert your output into list 
  #### e.g return list(arr) 
  arr=np.arange(0,10)
  arr[:]=5
  print(list(arr))

  return None



def even_num():
    
  ### Create an array of all the even integers from 10 to 50
  ### Convert your output into list 
  ### e.g return list(arr) 
  arr=np.arange(10,51,2)
  print(list(arr))

  return None



def create_matrix():
    
  ### Create a 3x3 matrix with values ranging from 0 to 8
  ### Convert your output into list 
  ### e.g return (arr).tolist()
  my_matrix = [ [0,1,2] , [3,4,5] , [6,7,8] ]
  arr = np.array(my_matrix)
  print(arr.tolist())

  return None



def linear_space():
    
  ### Create an array of 20 linearly spaced points between 0 and 1
  ### Convert your output into list 
  ### e.g return list(arr) 
  arr=np.linspace(0,1,20)
  print(list(arr))

  return None



def decimal_mat():
    
  ### Create an array of size 10*10 consisting of numbers from 0.01 to 1
  ### Convert your output into list 
  ### e.g return (arr).tolist()
  arr_=np.linspace(0.01,1,100)
  arr=arr_.reshape(10,10)
  print(arr.tolist())

  return None



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
  print(arr[2:,1:].tolist())

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
  print(arr[:3,1:2].tolist())

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
  print(arr[3:].tolist())
    
  return None 


# Great job!
