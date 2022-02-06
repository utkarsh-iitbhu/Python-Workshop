# ## Exercises

# Answer the questions or complete the tasks outlined in bold below.


def power(a,b):
  return a**b
print(power(7,4))  
# ** What is 7 to the power of 4?**
    



def split_str(s):
  sl=s.split()
  return list(sl)
# ** Split this string:**
s = "Hi there Sam!"
print(split_str(s))
# **into a list. **



def format(planet,diameter):
    
# ** Given the variables:**
# 
# 
# ** Use .format() to print the following string: **
# 
#     The diameter of Earth is 12742 kilometers.
  return 'The diameter of {name} is {num} kilometers.'.format(name=planet,num=diameter)
# planet = "Earth"
# diameter = 12742
# format(planet,diameter)




def indexing(lst):
  return lst[3][1][2][0]
    # ** Given this nested list, use indexing to grab the word "hello" **
#lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(indexing(lst))



def dictionary(d):
# ** Given this nested dictionary grab the word "hello". Be prepared, this will be annoying/tricky **
# d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
   return d["k1"][3]["tricky"][3]["target"][3]
d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
print(dictionary(d))



def subjective():
# ** What is the main difference between a tuple and a list? **
# Tuple is _______
  return 'immutable'
    




def domainGet(email):
  jj=email.split("@")
# ** Create a function that grabs the email website domain from a string in the form: **
# 
# user@domain.com
#     
# **So for example, passing "user@domain.com" would return: domain.com**
  return jj[1]
email="user@domain.com"
print(domainGet(email))



def findDog(st):
  st=st.lower()
  st00="dog" in st
  return st00
# ** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **




def countDog(st):
  st=st.lower()
  return st.count("dog")
# ** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **




def lambdafunc(seq):
  seqa=list(filter(lambda item:item[0] =='s',seq))
  return seqa
seq = ['soup','dog','salad','cat','great']
print(lambdafunc(seq))
# ** Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:**
# **should be filtered down to:** 
#     ['soup','salad']



def caught_speeding(speed, is_birthday):
    if(is_birthday == 'true'):
      speed = speed-5
    else:
      speed=speed
    if(speed<61):
      return "No ticket"
    elif(speed>81):
      return "Big Ticket"
    else:
      return 'Small Ticket'
     
speed = 81
is_birthday = 'true'
print(caught_speeding(speed,is_birthday))
    
# **You are driving a little too fast, and a police officer stops you. Write a function
#   to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". 
#   If your speed is 60 or less, the result is "No Ticket". If speed is between 61 
#   and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big    Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all 
#   cases. **



## Numpy Exercises

import numpy as np


def create_arr_of_fives():
  aap=np.ones(10)
  aapp=aap.tolist()
  aaap=list(map(lambda var: var*5,aapp))
  return aaap
print(create_arr_of_fives())
  #### Create an array of 10 fives
  #### Convert your output into list 
  #### e.g return list(arr) 




def even_num():
    even=np.arange(51)
    even=even[10:]
    ev=list(filter(lambda var: var%2==0 , even))
    even2=np.array(ev)

    return list(even2)
print(even_num())
  ### Create an array of all the even integers from 10 to 50
  ### Convert your output into list 
  ### e.g return list(arr) 



def create_matrix():
  mat=np.arange(9)
  mat2=mat.reshape(3,3)
  return mat2.tolist()
  ### Create a 3x3 matrix with values ranging from 0 to 8
  ### Convert your output into list 
  ### e.g return (arr).tolist()





def linear_space():
  arr=np.linspace(0, 1, 20)
  return list(arr)
  ### Create an array of 20 linearly spaced points between 0 and 1
  ### Convert your output into list 
  ### e.g return list(arr) 



def decimal_mat():
  dec=np.arange(1,101)
  dec2=dec/100
  dec3=dec2.reshape(10,10)
  return (dec3).tolist()
print(decimal_mat())   
  ### Create an array of size 10*10 consisting of numbers from 0.01 to 1
  ### Convert your output into list 
  ### e.g return (arr).tolist()



def slices_1():
    
  # This is a given array
  arr = np.arange(1,26).reshape(5,5)
  arr2=arr[2:,1:]
  return (arr2).tolist()
print(slices_1()) 
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
    
  # This is a given array
  arr = np.arange(1,26).reshape(5,5)
  arr2= arr[:3,1:2]
  return (arr2).tolist()
print(slices_2())
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
    
  # This is a given array
  arr = np.arange(1,26).reshape(5,5)
  arr2= arr[3:]
  return (arr2).tolist()
print(slices_3())
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
