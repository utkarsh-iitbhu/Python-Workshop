import numpy as np
def power(7,4):
    return 7**4

import numpy as np
def split_str(s):
    s = "Hi there Sam!"
    x = s.split()
    return x

import numpy as np
def format("Earth",12742):
     print("The diameter of {} is {} kilometers.".format("Earth",12742))

import numpy as np
def indexing(lst):
    lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
    return lst[3][1][2][0]


import numpy as np
def dictionary(d):
  d={'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
  a=d['k1']
  b=a[3]
  x=b['tricky'][3]['target'][3]
  return x

import numpy as np
def subjective():
  return "Tuple is immutable"

import numpy as np
def domainGet(email):
  email = user@domain.com
  spl_word = '@'
  res = email.partition(spl_word)[2]
  return res  

import numpy as np
def findDog(st):
    st = "dog is an animal"
    substring = "dog"
   if substring in st:
    return "True"
   else:
    return "False"

import numpy as np
def countDog(st):
   st = "dog is a cute dog animal"
  test_sub = "dog" 
  res = st.count(test_sub)
  return str(res)

import numpy as np
def lambdafunc(seq): 
 seq = ['soup','dog','salad','cat','great']
 filtered = list(filter (lambda test: test[0] == "s",seq))
 return filtered

import numpy as np
def caught_speeding(65, "True"):
 if(speed<=60 and is_birthday=="False"):
  a = "No ticket"
 elif(speed>=61 and speed<=80 and is_birthday=="False"):
  a = "Small ticket"
 elif(speed>=81 and is_birthday=="False"):
  a = "Big ticket"
 elif(speed<=65 and is_birthday=="True"):
  a = "No ticket"
 elif(speed>=66 and speed<=85 and is_birthday=="True"):
  a = "Small ticket"
 elif(speed>=86 and is_birthday=="True"):
  a = "Big ticket"
return a

import numpy as np
def create_arr_of_fives():
  my_list = [5,5,5,5,5,5,5,5,5,5]
  ar = np.array(my_list)
  return list(ar)

import numpy as np
def even_num():
  array=np.arange(10,50,2)
  return list(array) 

import numpy as np
def create_matrix():
   my_matrix = [[0,1,2] , [3,4,5] , [6,7,8]]
   arr = np.array(my_matrix)
   return arr.tolist()

import numpy as np
def linear_space():
   arr = np.linspace(0,1,20)
   return list(arr)


import numpy as np
def decimal_mat():
  arr = np.linspace(0.01,1,100)
  return (arr).tolist()

import numpy as np
def slices_1():   
  arr = np.arange(1,26).reshape(5,5)
  store = arr[2:5,1:5]
  return store.tolist()


import numpy as np
def slices_2():   
  arr = np.arange(1,26).reshape(5,5)
  store = arr[0:3,1:2]
  return store.tolist()


import numpy as np
def slices_3():   
  arr = np.arange(1,26).reshape(5,5)
  store = arr[3:5,0:5]
  return store.tolist()
