
# ## Exercises

# Answer the questions or complete the tasks outlined in bold below.


def power(a,b):
    
    # ** What is 7 to the power of 4?**
    c=b**a
    print(c)
    
    return None
power(4,7)



def split_str(s):
   data=s.split()
   mylist=[]
   for i in data:
     mylist.append(i)
   print(mylist)

split_str('Hi there Sam!')

def format(planet,diameter):
    
    print("the diameter of the ",planet,"is",diameter,"kilometers")

    return None

format('Earth',12742)

lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
def indexing(lst):
    return lst[3][1][2]
indexing(lst)

d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
def dictionary(d):
    
    return d['k1'][3]['tricky'][3]['target'][3]
dictionary(d)

def subjective():
    
# ** What is the main difference between a tuple and a list? **
# Tuple is immutable 

    return None




email='user@domain.com'
def domainGet(email):
    
    data=email.split('@')
    print(data[1])

    return None
domainGet(email)

st='there is a dog near me'
def findDog(st):
    data=st.split()
    for i in data:
        if i=='dog':
            print("True")
    return None
findDog(st)

st='there is a dog near me'
def countDog(st):
    count=0
    data=st.split()
    for i in data:
        if i=='dog':
            count=count+1
    print(count)
    return None
countDog(st)


seq = ['soup','dog','salad','cat','great']
def lambdafunc(seq):


    return list(filter(lambda x: x[0] == "s", seq))
lambdafunc(seq)


    
def caught_speeding(speed, is_birthday):
    if is_birthday==True:
      if speed<=65:
        print("no ticket")
      elif (speed>65 and speed<=85):
        print("small ticket")
      elif(speed>85):
        print("Big ticket")
    else:
      if speed<=60:
        print("no ticket")
      elif (speed>60 and speed<=80):
        print("small ticket")
      elif(speed>80):
        print("Big ticket")
    return None
caught_speeding(64,True)

    return None


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
