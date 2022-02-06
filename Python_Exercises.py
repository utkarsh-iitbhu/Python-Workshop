
# ## Exercises

# Answer the questions or complete the tasks outlined in bold below.


from this import s
from tkinter import N


def power(a,b):
    return a**b
    # ** What is 7 to the power of 4?**
a=7
b=4    
print(power(a,b))   


def split_str(s):
    return s.split()
    # ** Split this string:**
# 
s = "Hi there Sam!"
a=split_str(s)
print(a)


def format(planet,diameter):
    return format(planet,diameter)

# ** Given the variables:**
# 
planet = "Earth"
diameter = 12742
# 
# ** Use .format() to print the following string: **
# 
print("The diameter of {} is {} kilometers.".format(planet,diameter))

     



def indexing(lst):
    return lst[3,1,2,0]
# ** Given this nested list, use indexing to grab the word "hello" **

lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(lst[3][1][2][0])
    


def dictionary(d):
    return dictionary(d)
# ** Given this nested dictionary grab the word "hello". Be prepared, this will be annoying/tricky **

d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
dictionary = d['k1'][3]["tricky"][3]['target'][3]
print(dictionary)

   



def subjective():
    return s
# ** What is the main difference between a tuple and a list? **
s = "Tuple is immutable whereas list is mutable"
print(s)
   




def domainGet(email):
    print(email.split('@')[-1])
    # ** Create a function that grabs the email website domain from a string in the form: **
# 
#     user@domain.com
#     
# **So for example, passing "user@domain.com" would return: domain.com**
email = input(" enter your email: ")
domainGet(email)



    


def findDog(st):
    if "dog" in st.lower() :
     print("True")
    else : 
     print("false")
# ** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **

    return None
st = input("enter string : ")
findDog(st)

def countDog(st):

# ** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **
 st = input("Please enter your string: ")


 count = 0
 for string in st.lower().split():
        if string == 'dog':
            count = count + 1
            
 print(count)
countDog(st)
    
          
    

def lambdafunc(seq):
    return lambdafunc
    # ** Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:**
seq = ['soup','dog','salad','cat','great']
lambdafunc = list(filter(lambda word : word[0]=='s',seq))
print(lambdafunc)
# **should be filtered down to:**
# 
#     ['soup','salad']



    



    
# **You are driving a little too fast, and a police officer stops you. Write a function
#   to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". 
#   If your speed is 60 or less, the result is "No Ticket". If speed is between 61 
#   and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big    Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all 
#   cases. **
print("speed : ")
speed = int(input())
print("birthday : ")
is_birthday = str(input())
def caught_speeding(speed, is_birthday):
     
            
     if is_birthday == '6/2/2022':
      sp=speed-5
      print("True")
     else :
       sp = speed
       print("False")
     if sp<=60:
      
      print("No Ticket")
     elif sp>60 and sp<=80:
      print("Small Ticket")
     else :
      print("Big Ticket")

caught_speeding(speed,is_birthday)

    


## Numpy Exercises
 

import numpy as np


def create_arr_of_fives(a):
    
  #### Create an array of 10 fives
  #### Convert your output into list 
  #### e.g return list(arr) 
  
    return create_arr_of_fives
arr = np.ones(10)*5
create_arr_of_fives =list(arr)
print(create_arr_of_fives)




def even_num():
    
  ### Create an array of all the even integers from 10 to 50
  ### Convert your output into list 
  ### e.g return list(arr) 


  return even_num
arr = np.arange(5,25)*2
even_num = list(arr)
print(even_num)



def create_matrix():
    
  ### Create a 3x3 matrix with values ranging from 0 to 8
  ### Convert your output into list 
  ### e.g return (arr).tolist()

    return arr.tolist()
arr = np.arange(0,9).reshape(3,3)
create_matrix = arr.tolist()
print(create_matrix)  


def linear_space():
    
  ### Create an array of 20 linearly spaced points between 0 and 1
  ### Convert your output into list 
  ### e.g return list(arr) 

  return linear_space
arr[20][0] = np.linspace(0,1,num=20)
linear_space = arr.tolist() 
print(linear_space)



def decimal_mat():
    
  ### Create an array of size 10*10 consisting of numbers from 0.01 to 1
  ### Convert your output into list 
  ### e.g return (arr).tolist()

  return None
arr=np.arange(0.01,1.01,0.01,dtype=float).reshape(10,10)
decimal_mat = arr.tolist()
print(arr)

def slices_1():
    return (c).tolist()
  # This is a given array
arr = np.arange(1,26).reshape(5,5)
c = arr[2:5,1:5]
slices_1 = c.tolist()
print(slices_1)
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
    return (c).tolist()
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
c=arr[0:3,1]
slices_2 = c.tolist()
print(slices_2)
  



def slices_3():
    return (c).tolist()
  # This is a given array
arr = np.arange(1,26).reshape(5,5)
c=arr[3:5,0:5]
slices_3 = c.tolist()
print(slices_3)
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
