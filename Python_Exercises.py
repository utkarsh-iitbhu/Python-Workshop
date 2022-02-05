# 1
def power(a,b):  
    return a**b

# 2   
def split_str(s):
    return s.split()
    
# 3
def format(planet,diameter):
    return "The diameter of {} is {} kilometers.".format(planet,diameter)

# 4    
def indexing(lst):
    return lst[3][1][2][0]

# 5
def dictionary(d):
    return ((d.get('k1')[3]).get('tricky')[3]).get('target')[3]
    
# 6
def subjective():
    return "immutable"

# 7
def domainGet(email):
    flag = 0
    
    for i in email:
        if(i=="@"):
            flag = 1
            continue

        if(flag==1):
            return email[email.index(i):]

# 8
def findDog(st):
    if('dog' in st):
        return True
    
    else:
        return False
    
# 9
def countDog(st):
    count = 0

    for i in range(len(st)):
        if(st[i]=='d' and st[i+1]=='o' and st[i+2]=='g'):
            count+=1
    
    return count

# 10
def lambdafunc(seq):
    return list(filter(lambda x: x[0]=="s", seq))
    
# 11
def caught_speeding(speed, is_birthday):
    if(is_birthday==True):
        i = 5

    else:
        i = 0

    if(speed<=60+i):
        return "No Ticket"

    elif(speed>=61+i and speed<=80+i):
        return "Small Ticket"
    
    elif(speed>=81+i):
        return "Big Ticket"

# Numpy Exercises
import numpy as np

# 12
def create_arr_of_fives():
    arr = np.array([5,5,5,5,5,5,5,5,5,5])
    return list(arr)

# 13
def even_num():
    arr = np.arange(10,52,2)
    return list(arr)

# 14
def create_matrix():
    arr = np.arange(0,9).reshape(3,3)
    return (arr).tolist()

# 15
def linear_space():
    arr = np.linspace(0,1,20)
    return list(arr)    

# 16
def decimal_mat():
    arr = np.array([[0.01,  0.02,  0.03,  0.04,  0.05,  0.06,  0.07,  0.08,  0.09,  0.10],
                    [0.11,  0.12,  0.13,  0.14,  0.15,  0.16,  0.17,  0.18,  0.19,  0.20],
                    [0.21,  0.22,  0.23,  0.24,  0.25,  0.26,  0.27,  0.28,  0.29,  0.30],
                    [0.31,  0.32,  0.33,  0.34,  0.35,  0.36,  0.37,  0.38,  0.39,  0.40],
                    [0.41,  0.42,  0.43,  0.44,  0.45,  0.46,  0.47,  0.48,  0.49,  0.50],
                    [0.51,  0.52,  0.53,  0.54,  0.55,  0.56,  0.57,  0.58,  0.59,  0.60],
                    [0.61,  0.62,  0.63,  0.64,  0.65,  0.66,  0.67,  0.68,  0.69,  0.70],
                    [0.71,  0.72,  0.73,  0.74,  0.75,  0.76,  0.77,  0.78,  0.79,  0.80],
                    [0.81,  0.82,  0.83,  0.84,  0.85,  0.86,  0.87,  0.88,  0.89,  0.90],
                    [0.91,  0.92,  0.93,  0.94,  0.95,  0.96,  0.97,  0.98,  0.99,  1.00]])
    return (arr).tolist()   

# 17
def slices_1():
    arr = np.arange(1,26).reshape(5,5)
    arr = np.array([list(arr[2][1:5]),list(arr[3][1:5]),list(arr[4][1:5])])
    return (arr).tolist()

# 18
def slices_2():
    arr = np.arange(1,26).reshape(5,5)
    arr = np.array([list(arr[0][1:2]),list(arr[1][1:2]),list(arr[2][1:2])])
    return (arr).tolist()

# 19
def slices_3():
    arr = np.arange(1,26).reshape(5,5)
    arr = np.array([list(arr[3]),list(arr[4])])
    return (arr).tolist()
