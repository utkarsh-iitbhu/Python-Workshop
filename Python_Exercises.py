
# ## Exercises

# Answer the questions or complete the tasks outlined in bold below.


def power(a,b):
    
    a=int(input())
    b=int(input())
    c= a**b
    print(c)
    
    return None



def split_str(s):
    a=str(input("enter your string:"))
    b=a.split()
    print(b)
    
    return None


def format(planet,diameter):
    a=input("enter the name of your planet:")
    b=int(input("enter the diameter:"))
    print("The diameter of ",a," is ",b," kilometres.") 
    
    return None



def indexing(lst):
    lst=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
    print(lst[3][1][2][0])
    
    return None


def dictionary(d):
    d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
    print(d['k1'][3]['tricky'][3]['target'][3])
    
    return None


def subjective():
    immutable
    
    return None




def domainGet(email):
    a=input("enter your email:")
    b=len(a)
    z=-1
    for i in a:
        z+=1
        if i=='@':
            x=a[z+1:b]
            print(x)
        else:
            continue
    
  

    return None


def findDog(st):
    s=input("enter your string:")
    l=s.split()
    for i in l:
        if i=='dog':
            print('true')
        else:
            continue
        
    return None


def countDog(st):
    ctr=0
    s=input("enter your sring:")
    l=s.split()
    for i in l:
        if i=='dog':
            ctr=ctr+1
        else:
            continue
    print("dog occured ",ctr," times.")    

    return None



def lambdafunc(seq):
    a=[]
    b=int(input("how many elements do you want:"))
    for i in range(b):
        c=input("enter your word:")
        a.append(c)
    print(a)
    s=[]
    for j in a:
        d=j
        if d[0]=='s':
            s.append(d)
        else:
            continue
    print(s)
    #or
        a=[]
    b=int(input("how many elements do you want:"))
    for i in range(b):
        c=input("enter your word:")
        a.append(c)
    f=filter(lambda a: a[0]=='s',seq)
    print(list(f))
    
    return None


def caught_speeding(speed, is_birthday):
    speed=int(input("enter the speed:"))
    birthday=input("is it your birthday:")
    if birthday=='yes':
              if speed<=65:
                  print("no ticket")
              elif speed>65 and speed<=85:
                  print("small ticket")
              elif speed<85:
                  print("big ticket")        
    elif birthday=='no':
              if speed<=60:
                  print("no ticket")
              elif speed>60 and speed<=80:
                  print("small ticket")
              elif speed<80:
                  print("big ticket")
    
    return None


## Numpy Exercises

import numpy as np


def create_arr_of_fives():
    a=[]
    for i in range (10):
        a.append(5)
    print(a)
    
  return None



def even_num():
    a=[]
    for i in range(10,51,2):
        a.append(i)
    print(a)  
      
  return None



def create_matrix():
    mat=np.arrange(0,9).reshape(3,3)
    print(mat)
   
  return None



    def linear_space():
        a=1/20
    b=[]
    c=0
    for i in range(20):
        c=c+a
        b.append(c)
    print(b)
    
  return None



def decimal_mat():
    a=0.01
    b=[]
    c=0
    for i in range(100):
        c=c+a
        b.append(c)
    print(b) 
    
  return None



def slices_1():
    
  # This is a given array
  arr = np.arange(1,26).reshape(5,5)
    a=([[ 1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10],
       [11, 12, 13, 14, 15],
       [16, 17, 18, 19, 20],
       [21, 22, 23, 24, 25]])
    x=[]
    b=[]
    c=[]
    d=0
    y=[]
    for i in range (2,5):
        d=d+1
        for j in range (1,5):
            if d==1:
                x.append(a[i][j])
            elif d==2:
                b.append(a[i][j])
            elif d==3:
                c.append(a[i][j])
    y.append(x)
    y.append(b)
    y.append(c)
    print(y)

    
  return None



def slices_2():
    
  # This is a given array
  arr = np.arange(1,26).reshape(5,5)
    a=([[ 1,  2,  3,  4,  5],
        [ 6,  7,  8,  9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]])

    x=[]
    b=[]
    c=[]
    d=[]
    y=0
    for i in range (0,3):
        y=y+1
            b.append(a[i][1])
        elif y==2:
            c.append(a[i][1])
        elif y==3:
            d.append(a[i][1])
    x.append(b)
    x.append(c)
    x.append(d)
    print(x)
    
  return None 



def slices_3():
    
  # This is a given array
  arr = np.arange(1,26).reshape(5,5)
    a=([[ 1,  2,  3,  4,  5],
        [ 6,  7,  8,  9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]])

    x=[]
    b=[]
    c=[]
    d=0
    y=[]
    for i in range (3,5):
        d=d+1
        for j in range (0,5):
            if d==1:
                x.append(a[i][j])
            elif d==2:
                b.append(a[i][j])        
    y.append(x)
    y.append(b)
    print(y)
        
  return None 


# Great job!
