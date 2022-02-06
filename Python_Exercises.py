# ## Exercises

# Answer the questions or complete the tasks outlined in bold below.


def power(a,b):
    return(a**b)
    # ** What is 7 to the power of 4?**
    



def split_str(s):
    return(s.split())
    # ** Split this string:**
# 
#     s = "Hi there Sam!"
#     
# **into a list. **



def format(planet,diameter):
    return("The diameter of {} is {} kilometers.".format(planet,diameter))
# ** Given the variables:**
# 
#     planet = "Earth"
#     diameter = 12742
# 
# ** Use .format() to print the following string: **
# 
#     The diameter of Earth is 12742 kilometers.




def indexing(lst):
    return(lst[3][1][2][0])
# ** Given this nested list, use indexing to grab the word "hello" **

#lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]



def dictionary(d):
    return((((d.get('k1')[3]).get('tricky')[3]).get('target')[3]))
# ** Given this nested dictionary grab the word "hello". Be prepared, this will be annoying/tricky **

# d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}



def subjective():
    return('immutable')
# ** What is the main difference between a tuple and a list? **
# Tuple is _______





def domainGet(email):
    str=''
    for i in range(len(email)):
        if email[i]=='@':
            for j in range(i+1,len(email)):
                str+=email[j]
    return(str)            
    # ** Create a function that grabs the email website domain from a string in the form: **
# 
#     user@domain.com
#     
# **So for example, passing "user@domain.com" would return: domain.com**



def findDog(st):
    if 'dog' in st:
        return True
    else:
        return False
# ** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **

  

def countDog(st):
    c=0
    for i in range(len(st)):
        if(st[i]=="d" and st[i+1]=="o" and st[i+2]=="g"):
            c+=1
    return(c)       
# ** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **




def lambdafunc(seq):
    seq=list(filter(lambda x: x[0]=='s',seq))
    return(seq)
    # ** Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:**
# 
#     seq = ['soup','dog','salad','cat','great']
# 
# **should be filtered down to:**
# 
#     ['soup','salad']

    


def caught_speeding(speed, is_birthday):
    if(is_birthday==True):
        if(speed<=65):
            return("No Ticket")
        elif(speed>=66 and speed<=85):
            return("Small Ticket")
        elif(speed>=86):
            return("Big Ticket")
    else:
        if(speed<=60):
            return("No Ticket")
        elif(speed>=61 and speed<=80):
            return("Small Ticket")
        elif(speed>=81):
            return("Big Ticket")
    
# **You are driving a little too fast, and a police officer stops you. Write a function
#   to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". 
#   If your speed is 60 or less, the result is "No Ticket". If speed is between 61 
#   and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big    Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all 
#   cases. **

    


## Numpy Exercises

import numpy as np


def create_arr_of_fives():
    arr=np.array([5,5,5,5,5,5,5,5,5,5])
    return(list(arr))
  #### Create an array of 10 fives
  #### Convert your output into list 
  #### e.g return list(arr) 

  



def even_num():
    arr=np.arange(10,51,2)
    return(arr.tolist())
  ### Create an array of all the even integers from 10 to 50
  ### Convert your output into list 
  ### e.g return list(arr) 

  



def create_matrix():
    matrix=[[0,1,2],[3,4,5],[6,7,8]]
    arr=np.array(matrix)
    return(arr.tolist())
  ### Create a 3x3 matrix with values ranging from 0 to 8
  ### Convert your output into list 
  ### e.g return (arr).tolist()

  



def linear_space():
    arr=np.linspace(0,1,20)
    return(list(arr))
  ### Create an array of 20 linearly spaced points between 0 and 1
  ### Convert your output into list 
  ### e.g return list(arr) 

  



def decimal_mat():
    arr=np.arange(1,101).reshape(10,10)
    arr1=arr/100
    return(arr1.tolist())
  ### Create an array of size 10*10 consisting of numbers from 0.01 to 1
  ### Convert your output into list 
  ### e.g return (arr).tolist()




def slices_1():
    arr=np.arange(1,26).reshape(5,5)
    arr1=arr[2:5,1:5]
    return(arr1.tolist())
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
    arr = np.arange(1,26).reshape(5,5)
    arr1=arr[0:3,1:2]
    return(arr1.tolist())
  # This is a given array
  #arr = np.arange(1,26).reshape(5,5)
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
    arr = np.arange(1,26).reshape(5,5)
    arr1=arr[3:5,0:5]
    return(arr1.tolist())
  # This is a given array
  #arr = np.arange(1,26).reshape(5,5)
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
