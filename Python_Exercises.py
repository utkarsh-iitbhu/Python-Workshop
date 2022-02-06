def power(a,b):
    return (a**b)



def split_str(s):

    str=s.split()
    return str


def format(planet,diameter):
    s="The diameter of {planet} is {diameter} kilometers.".format(planet=str(planet), diameter=str(diameter))
    return s

def indexing(lst):
    return lst[3][1][2][0]


def dictionary(dic):

    return dic['k1'][3]['tricky'][3]['target'][3]


def subjective():
    return "immutable"




def domainGet(email):
    term=email.split("@")
    return term[1]


def findDog(st):
    if ("dog" or "Dog" in st):
        return True


def countDog(str):


    lst=str.split()
    freq=0
    for i in range(0, len(lst)):
        if ("dog"==lst[i].lower()):
            freq+=1
    return freq



def lambdafunc(seq):
    return list(filter(lambda a: a[0]=="s", seq))


def caught_speeding(speed, is_birthday):
    if (is_birthday==True):
        if (speed<=65):
            return "No Ticket"
        elif (speed>65 and speed<=85):
            return "Small Ticket"
        else:
            return "Big Ticket"
    elif (is_birthday==False):
        if (speed<=60):
            return "No Ticket"
        elif (speed>60 and speed<=80):
            return "Small Ticket"
        else:
            return "Big Ticket"


## Numpy Exercises

import numpy as np


def create_arr_of_fives():
  arr=np.ones(10)*5
  list1=arr.tolist()
  return list1



def even_num():
  arr=np.arange(10, 51, 2)
  lst=arr.tolist()
  return lst



def create_matrix():
  arr=np.arange(0, 9).reshape(3, 3)
  arr2=arr.tolist()
  return arr2



def linear_space():
  arr=np.linspace(0, 1, 20)
  arr3=arr.tolist()
  return arr3



def decimal_mat():
  arr4=np.arange(1, 101).reshape(10, 10)
  arr5=arr4/100
  arr6=arr5.tolist()
  return arr6



def slices_1():
    
  arr = np.arange(1,26).reshape(5,5)

  slice1=arr[2:5, 1:5]
  arr7=slice1.tolist()

  return arr7



def slices_2():
    
  arr = np.arange(1,26).reshape(5,5)

  arr8=[]
  for i in range(0, 3):
      arr9=[]
      arr9.append(arr[i, 1])
      arr8.insert(i, arr9)

  return arr8



def slices_3():
    
  arr = np.arange(1,26).reshape(5,5)
  
  arr10=[]
  for i in range (3, 5):
      arr11=[]
      arr11=arr[i, 0:5].tolist()
      arr10.insert(i, arr11)
    
  return arr10
