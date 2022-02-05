### Manepalli Deepika
### Civil 21064018
# ## Exercises

# Answer the questions or complete the tasks outlined in bold below.


def power(a,b):
    print(a**b)
  



def split_str(s):
    ans=s.split()
    print(ans)
    return None


def format(planet,diameter):
    
    ans="The diameter of {planet_name} is {Dia} kilometers.".format(planet_name=planet,Dia=diameter)
    print(ans)
    return None


def indexing(lst):
    lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
    print(lst[3][1][2])
    return None


def dictionary(d):
    d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
    print(d['k1'][3]['tricky'][3]['target'][3])
    return None



def subjective():
    print("The tuples are immutable objects the lists are mutable. This means that tuples cannot be changed while the lists can be modified.")
    return None




def domainGet(email):
    x=email.index("@")
    print(email[x+1:],end="")
    print("**")
    return None


def findDog(st):
    if('dog' in st):
        print("True")
    else:
        print("False")
    return None


def countDog(st):
    print(st.count('dog'))
    return None


def lambdafunc(seq):
    result = filter(lambda x: x[0]=='s', seq)
    print(list(result))
    return None


def caught_speeding(speed, is_birthday):
    if(is_birthday):
        if(speed<=65):
            print("No Ticket")
        elif(speed>65 and speed<=85):
            print("Small Ticket")
        else:
            print("Big Ticket")
    else:
        if(speed<=60):
            print("No Ticket")
        elif(speed>60 and speed<=80):
            print("Small Ticket")
        else:
            print("Big Ticket")
    return None
    


## Numpy Exercises

import numpy as np


def create_arr_of_fives():
    ans=np.ones(10)*5;
    print(list(ans))
    return None



def even_num():
    ans=np.arange(10,51,2)
    print(list(ans))
    return None




def create_matrix():
    x =  np.arange(0, 9).reshape(3,3)
    print(list(x))
    return None



def linear_space():
    ans=np.linspace(0,1,20)
    print(list(ans))
    return None



def decimal_mat():
    ans=np.linspace(0.01,1,100).reshape(10,10)
    print(list(ans)



def slices_1():
    arr = np.arange(1,26).reshape(5,5)
    print(list(arr))




def slices_2():
    arr = np.arange(1,26).reshape(5,5)
    ans=arr.tolist()
    print(ans)




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


# Great job!
