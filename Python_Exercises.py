
# ## Exercises

# Answer the questions or complete the tasks outlined in bold below.


def power(a,b):
    return a**b  
power(7,4)
    # ** What is 7 to the power of 4?**
    #answer will be 2401
def split_str(s):
    
    # ** Split this string:**
    #  s = "Hi there Sam!"
    s=s.split()
    s=list(s)
    # **into a list. **
def format(planet,diameter):
    print('the diameter of {} is {} kilometers'.format(planet,diameter))
    return None
format('earth',12742)_

# ** Given the variables:**
# 
#     planet = "Earth"
#     diameter = 12742
# 
# ** Use .format() to print the following string: **
#     The diameter of Earth is 12742 kilometers.

def indexing(lst):
    return lst[3][1][2]
    
# ** Given this nested list, use indexing to grab the word "hello" **
indexing([1,2,[3,4],[5,[100,200,['hello']],23,11],1,7])  #calling function
#lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
def dictionary(d):
    return d['k1'][3]['tricky'][3]['target'][3]

dictionary({'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]})
    
# ** Given this nested dictionary grab the word "hello". Be prepared, this will be annoying/tricky **

# d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}

def subjective():
    
# ** What is the main difference between a tuple and a list? **
# Tuple is _______immutable so basically once the data inside tuple is set it can't be changed,whereas the data in list is mutable ,elements can be changed later while programming
#list can be modified using various built-in methods but tuples don't have these built-in methods

def domainGet(email):
    mail=email.split('@')
    return mail[-1]
    # ** Create a function that grabs the email website domain from a string in the form: **
# 
#     user@domain.com
#     
# **So for example, passing "user@domain.com" would return: domain.com**

def findDog(st):
    
# ** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **
def countDog(st):
    number=0
    for i in st.split():
        if i== 'dog':
            number += 1
    return number

# ** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **
countDog('hi dog, you are a dog')

def lambdafunc(seq):
    new_list=list(filter(lambda word: word[0]=='s',seq))
    return new_list

lambdafunc(['soup','dog','salad','cat','great'])
    
    
    # ** Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:**
# 
#     seq = ['soup','dog','salad','cat','great']
# 
# **should be filtered down to:**
# 
#     ['soup','salad']

def caught_speeding(speed, is_birthday):
    if is_birthday:
        allowed=speed+5
    else:
        allowed=speed
    if allowed<=60:
        return 'No Ticket'
    elif allowed>=61 and allowed<=80:
        return 'Small Ticket'
    elif allowed>=81
        return 'Big Ticket'

    
caught_speed()#calling function
    
# **You are driving a little too fast, and a police officer stops you. Write a function
#   to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". 
#   If your speed is 60 or less, the result is "No Ticket". If speed is between 61 
#   and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big    Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all 
#   cases. **

## Numpy Exercises

import numpy as np


def create_arr_of_fives():
    arr=['5','5','5','5','5','5','5','5','5','5']
    return list(arr)
    
  #### Create an array of 10 fives
  #### Convert your output into list 
  #### e.g return list(arr) 
create_arr_of_fives()



def even_num():
    lis=[]
    for i in range(10,51):
        if i%2==0:
            lis.append(i)
    return list(lis)
even_num()

### Create an array of all the even integers from 10 to 50
  ### Convert your output into list 
  ### e.g return list(arr) 
def create_matrix():
    matrix=np.arange(2,11).reshape(3,3)
    return (matrix).tolist()
create_matrix()
    
  ### Create a 3x3 matrix with values ranging from 0 to 8
  ### Convert your output into list 
  ### e.g return (arr).tolist()

def linear_space():
  arr=np.linspace(0,1,20)
  return list(arr)

linear_space()
  ### Create an array of 20 linearly spaced points between 0 and 1
  ### Convert your output into list 
  ### e.g return list(arr) 

def decimal_mat():
    arr=np.linspace(0.01,1.00,100)
    arr=arr.reshape(10,10)
    return (arr).tolist()

decimal_mat()
    
  ### Create an array of size 10*10 consisting of numbers from 0.01 to 1
  ### Convert your output into list 
  ### e.g return (arr).tolist()

def slices_1():
    
  # This is a given array
  # array([[ 1,  2,  3,  4,  5],
  #      [ 6,  7,  8,  9, 10],
  #      [11, 12, 13, 14, 15],
  #      [16, 17, 18, 19, 20],
  #      [21, 22, 23, 24, 25]])
    arr = np.arange(1,26).reshape(5,5)
    return (arr).tolist()

  # Write a code to slice this given array
  ### Convert your output into list 
  ### e.g return (arr).tolist()
  # array([[12, 13, 14, 15],
  #      [17, 18, 19, 20],
  #      [22, 23, 24, 25]])


def slices_2():
    
  # This is a given array
  arr = np.arange(1,26).reshape(5,5)
  arr=arr[:3,1:2]
  return (arr).tolist()
          
slices_2()    
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
  #      [12]]]

def slices_3():
    
  # This is a given array
  arr = np.arange(1,26).reshape(5,5)
  arr=arr[3:,:]
  return (arr).tolist()


slices_3()
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
