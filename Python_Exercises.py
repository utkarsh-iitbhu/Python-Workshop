
# ## Exercises

# Answer the questions or complete the tasks outlined in bold below.


def power(a,b):
    return a**b
out =  power(7,4)
print(out)


def split_str(s):
    x = s.split()
    return x
out = split_str("Hi there Sam!")
print(out)


def format(planet,diameter):
     print("The diameter of {} is {} kilometers.".format(planet,diameter))
out = format("Earth",12742)


def indexing(lst):
    return lst[3][1][2][0]
out = indexing([1,2,[3,4],[5,[100,200,['hello']],23,11],1,7])
print(out)


import numpy as np
def dictionary(d):
  d={'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
  a=d['k1']
  b=a[3]
  x=b['tricky'][3]['target'][3]
  return x
out = dictionary({'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]})
print(out)


def subjective():
  return "Tuple is immutable"
out = subjective()
print(out)


def domainGet(email):
  spl_word = '@'
  res = email.partition(spl_word)[2]
  return res  
out = domainGet("user@domain.com")
print(out)


def findDog(st):
 substring = "dog"
 if substring in st:
    return "True"
 else:
    return "False"
#Test Case :    
out = findDog("My dog is very cute")    
print(out)


def countDog(st):
  test_sub = "dog" 
  res = st.count(test_sub)
  return str(res)
out = countDog("dog is a tupid dogs of dogs creatures among dogs of dog")
print(out)


def lambdafunc(seq): 
 filtered = list(filter (lambda test: test[0] == "s",seq))
 return filtered
out = lambdafunc(['soup', 'dog','salad', 'cat', 'great'])
print(out)

def caught_speeding(speed, is_birthday):
if(speed<=60 and is_birthday=="False"):
print("No ticket")
elif(speed>=61 and speed<=80 and is_birthday=="False"):
print("Small ticket")
elif(speed>=81 and is_birthday=="False"):
print("Big ticket")
elif(speed<=65 and is_birthday=="True"):
print("No ticket")
elif(speed>=66 and speed<=85 and is_birthday=="True"):
print("Small ticket")
elif(speed>=86 and is_birthday=="True"):
print("Big ticket")


## Numpy Exercises

import numpy as np


def create_arr_of_fives():
  my_list = [5,5,5,5,5,5,5,5,5,5]
  ar = np.array(my_list)
  return list(ar)
out = create_arr_of_fives()
print(out)


def even_num():
  array=np.arange(10,50,2)
  return list(array) 
out = even_num()
print(out)


def create_matrix():
   my_matrix = [[0,1,2] , [3,4,5] , [6,7,8]]
   arr = np.array(my_matrix)
   return arr.tolist()
out = create_matrix()
print(out)


def linear_space():
   arr = np.linspace(0,1,20)
   return list(arr)
out = linear_space()
print(out)


def decimal_mat():
  arr = np.linspace(0.01,1,100)
  return (arr).tolist()
out = decimal_mat()
print(out)


def slices_1():   
  arr = np.arange(1,26).reshape(5,5)
  store = arr[2:5,1:5]
  return store.tolist()
out = slices_1()
print(out)


def slices_2():   
  arr = np.arange(1,26).reshape(5,5)
  store = arr[0:3,1:2]
  return store.tolist()
out = slices_1()
print(out)


def slices_3():   
  arr = np.arange(1,26).reshape(5,5)
  store = arr[3:5,0:5]
  return store.tolist()
out = slices_1()
print(out) 


# Great job!
