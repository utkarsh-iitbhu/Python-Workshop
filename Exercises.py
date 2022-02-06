# Exercises.py
def power(a,b):
    return(a**b)


def split_str(s):
    return(s.split())


def format(planet,diameter):
    return("The diameter of {} is {}.".format(planet,diameter))


def indexing(lst):
    return(lst[3][1][2][0])


def dictionary(d):
    return((((d.get('k1')[3]).get('tricky')[3]).get('target')[3]))


def subjective():
    return('Immutable')


def domainGet(email):
    str=''
      for i in range(len(email)):
        if email[i]=='@':
            for j in range(i+1,len(email)):
                str+=email[j]
      return(str)


def findDog(st):
    if 'dog' in st:
        return True
    else:
        return False
    
def countDog(st):
    c=0
      for i in range(len(st)):
        if(st[i]=="d" and st[i+1]=="o" and st[i+2]=="g"):
            c+=1
      return(c)

def lambdafunc(seq):
    seq=list(filter(lambda x: x[0]=='s',seq))
    return(seq)


def caught_speeding(speed, is_birthday):
    if(is_birthday==True):
        if(speed<=65):
            return("No ticket")
        elif(speed>=66 and speed<=85):
            return("Small ticket")
        elif(speed>=86):
            return("Big ticket")
    else:
        if(speed<=60):
            return("No ticket")
        elif(speed>=61 and speed<=80):
            return("Small ticket")
        elif(speed>=81):
            return("Big ticket")

        
import numpy as np
def create_arr_of_fives():
    arr=np.array([5,5,5,5,5,5,5,5,5,5])
    return(list(arr))


import numpy as np
def even_num():
    arr=np.arange(10,51,2)
    return(arr.tolist())


import numpy as np
def create_matrix():
    matrix=[[0,1,2],[3,4,5],[6,7,8]]
    arr=np.array(matrix)
    return(arr.tolist())


import numpy as np
def linear_space():
    arr=np.linspace(0,1,20)
    return(list(arr))


import numpy as np
def decimal_mat():
    arr=np.arange(1,101).reshape(10,10)
    arr1=arr/100
    return(arr1.tolist())


import numpy as np
def slices_1(): 
    arr=np.arange(1,26).reshape(5,5)
    arr1=arr[2:5,1:5]
    return(arr1.tolist())


import numpy as np
def slices_2():
    arr = np.arange(1,26).reshape(5,5)
    arr1=arr[0:3,1:2]
    return(arr1.tolist())


import numpy as np
def slices_3():
    arr = np.arange(1,26).reshape(5,5)
    arr1=arr[3:5,0:5]
    return(arr1.tolist())
