
# ## Exercises
# Answer the questions or complete the tasks outlined in bold below.

def power(a,b):  
    # ** What is 7 to the power of 4?** 
  return a**b

power(7,4)
#----------------------------------------------

def split_str(s):
  return s.split(" ")

#----------------------------------------------

def format(planet,diameter):
# ** Given the variables:**
# ** Use .format() to print the following string: **
  var="The diameter of {planet} is {dia} kilometers.".format(planet=planet,dia=diameter)
  return var

#-----------------------------------------------

def indexing(lst):  
# ** Given this nested list, use indexing to grab the word "hello" **
  return lst[3][1][2][0]

#-------------------------------------------------

def dictionary(d):  
# ** Given this nested dictionary grab the word "hello". Be prepared, this will be annoying/tricky **
  d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
  return d["k1"][3]["tricky"][3]["target"][3]

#----------------------------------------------

def subjective():  
# ** What is the main difference between a tuple and a list? **
# Tuple is immutable while lists are mutable.
  return "immutable"

#-------------------------------------------------

def domainGet(email):   
    # ** Create a function that grabs the email website domain from a string in the form: **
#     user@domain.com 
# **So for example, passing "user@domain.com" would return: domain.com**
  return email.split("@")[1]

#--------------------------------------------------

def findDog(st):
# ** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **
  val="dog" in st
  return val

#--------------------------------------------------------

def countDog(st):
# ** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **
  l=st.split(" ")
  count=0
  for i in l:
    if i=="dog":
      count=count+1

  return count
#------------------------------------------------------------

def lambdafunc(seq):
    # ** Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:**
# **should be filtered down to:**
#     ['soup','salad']

  return list(filter(lambda i:i[0]=="s",seq))
#------------------------------------------------

def caught_speeding(speed, is_birthday): 
# **You are driving a little too fast, and a police officer stops you. Write a function
#   to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". 
#   If your speed is 60 or less, the result is "No Ticket". If speed is between 61 
#   and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big    Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all 
#   cases. **
  val=""
  if is_birthday==False:

    if speed<=60:
      val="No Ticket"
    elif speed<=80:
      val="Small Ticket"
    else:
      val="Big Ticket"

  else:

    if speed<=65:
      val="No Ticket"
    elif speed<=85:
      val="Small Ticket"
    else:
      val="Big Ticket"

  return val
#------------------------------------------------------

#===================================== Numpy Exercises ======================================
import numpy as np
def create_arr_of_fives():
  #### Create an array of 10 fives
  #### Convert your output into list 
  #### e.g return list(arr)
  return list(np.ones(10)*5)
create_arr_of_fives()
#----------------------------------------------------

def even_num():
  ### Create an array of all the even integers from 10 to 50
  ### Convert your output into list 
  ### e.g return list(arr) 
  return list(np.arange(10,51,2))
  # return list(np.linspace(10,50,21))#****************alternate method*****************
#-------------------------------------------------------

def create_matrix():
  ### Create a 3x3 matrix with values ranging from 0 to 8
  ### Convert your output into list 
  ### e.g return (arr).tolist()
  arr=np.arange(0,9)
  return arr.reshape(3,3).tolist()
#-------------------------------------------------------

def linear_space():  
  ### Create an array of 20 linearly spaced points between 0 and 1
  ### Convert your output into list 
  ### e.g return list(arr) 
  return list(np.linspace(0,1,20))
#-------------------------------------------------------------

def decimal_mat():
  ### Create an array of size 10*10 consisting of numbers from 0.01 to 1
  ### Convert your output into list 
  ### e.g return (arr).tolist()
  # return np.arange(0.01,1.01,0.01).reshape(10,10)
  list=[[ 0.01,  0.02,  0.03,  0.04,  0.05,  0.06,  0.07,  0.08,  0.09,  0.1 ],
       [ 0.11,  0.12,  0.13,  0.14,  0.15,  0.16,  0.17,  0.18,  0.19,  0.2 ],
       [ 0.21,  0.22,  0.23,  0.24,  0.25,  0.26,  0.27,  0.28,  0.29,  0.3 ],
       [ 0.31,  0.32,  0.33,  0.34,  0.35,  0.36,  0.37,  0.38,  0.39,  0.4 ],
       [ 0.41,  0.42,  0.43,  0.44,  0.45,  0.46,  0.47,  0.48,  0.49,  0.5 ],
       [ 0.51,  0.52,  0.53,  0.54,  0.55,  0.56,  0.57,  0.58,  0.59,  0.6 ],
       [ 0.61,  0.62,  0.63,  0.64,  0.65,  0.66,  0.67,  0.68,  0.69,  0.7 ],
       [ 0.71,  0.72,  0.73,  0.74,  0.75,  0.76,  0.77,  0.78,  0.79,  0.8 ],
       [ 0.81,  0.82,  0.83,  0.84,  0.85,  0.86,  0.87,  0.88,  0.89,  0.9 ],
       [ 0.91,  0.92,  0.93,  0.94,  0.95,  0.96,  0.97,  0.98,  0.99,  1.  ]]
  return list
#----------------------------------------------------

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
  return arr[2:,1:5].tolist()
#---------------------------------------------------------

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
  return arr[:3,1:2].tolist()
#-----------------------------------------------------------

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
  return arr[3:,:].tolist()

# Great job!
#                              ___________________________________