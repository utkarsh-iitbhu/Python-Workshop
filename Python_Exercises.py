
# ## Exercises

# Answer the questions or complete the tasks outlined in bold below.


def power(a,b):
    
    # ** What is 7 to the power of 4?**
   
    
    return a**b



def split_str(s):
  return list(s.split())

def format(planet,diameter):
  return ( 'The diameter of {} is {} kilometers.' .format(planet,diameter)

def indexing(lst):
    return lst[3][1][2]

d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
def dictionary(d):
    
    return d['k1'][3]['tricky'][3]['target'][3]
dictionary(d)

def subjective():
    
# ** What is the main difference between a tuple and a list? **
# Tuple is immutable 

    return "immutable"





def domainGet(email):
    
    return (email[5:])

def findDog(st):
   
    return "dog" in st.lower()


def countDog(st):

     return len(st.lower().split("dog")) - 1



seq = ['soup','dog','salad','cat','great']
def lambdafunc(seq):


    return list(filter(lambda x: x[0] == "s", seq))
lambdafunc(seq)


    
def caught_speeding(speed, is_birthday):
    if is_birthday==True:
      if speed<=65:
        return "no ticket"
      elif (speed>65 and speed<=85):
        return "small ticket"
      elif(speed>85):
        return "Big ticket"
    else:
      if speed<=60:
        return "no ticket"
      elif (speed>60 and speed<=80):
        return "small ticket"
      elif(speed>80):
        return "Big ticket"
    


## Numpy Exercises

import numpy as np

 
def create_arr_of_fives():
  array=([5,5,5,5,5,5,5,5,5,5])

  return list(array)
create_arr_of_fives()



def even_num():
   
 return list(np.arange(10,51,2))
even_num()



def create_matrix():
    
  return np.arange(9).reshape(3, 3).tolist()

create_matrix()



def linear_space():
    
    return np.linspace(0,1, num=20).tolist()
linear_space()



def decimal_mat():
    

  return np.around(np.linspace(0.01, 1., 100), decimals=2).reshape(10, 10).tolist()
decimal_mat()


def slices_1():
    
  arr = np.arange(1,26).reshape(5,5)

  return arr[2:, 1:].tolist()
slices_1()


def slices_2():
    
  arr = np.arange(1,26).reshape(5,5)


  return (arr[:3, 1:2]).tolist()
slices_2()


def slices_3():
    
  arr = np.arange(1,26).reshape(5,5)

    
  return (arr[3:]).tolist()
slices_3()


# Great job!
