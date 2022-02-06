
# ## Exercises

# Answer the questions or complete the tasks outlined in bold below.

#Q1
def power(a,b):

    # take input 'a' and 'b' where 'a' is the number and 'b' is it's power
    c = a**b
    print(c)
    
    return None


#Q2
def split_str(s):

    #.split() splits a string into a list
    print(s.split())

    return None

#Q3
def format(planet,diameter):

     # .format() replaces '{}' with another word/number
    str = "The diameter of {planet} is {diameter} kilometers.".format(planet = a, diameter = b)
    print(str)

    return None


#Q4 
def indexing(lst):
    
# ** Given this nested list, use indexing to grab the word "hello" **

#lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
    print(lst[3][1][2][0])

    return None

#Q5 
def dictionary(d):
    
# ** Given this nested dictionary grab the word "hello". Be prepared, this will be annoying/tricky **

# d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
    print(d['k1'][3]['tricky'][3]['target'][3])


    return None


#Q6
def subjective():
    
# ** What is the main difference between a tuple and a list? **
# A Tuple is just like a list except that it's contents can not be changed, whereas a list's contents can be changed.

    return "A tuple is immutable"



#Q7 
def domainGet(email):
    email.split("@")
    return None


#Q8
def findDog(st):
    # removing punctuations from the string
    puncs = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for e in st:
        if e in puncs:
            st = st.replace(e,"")

    list = st.split()
    if "dog" in list:
        bool = True
    else:
        bool = False
        
    if bool == True:
        a = "Given string contains the word 'dog'."
    else:
        a = "Given string does not contains the word 'dog'."
    
    print(a)
    return None


#Q9
def countDog(st):
    # removing punctuations from the string
    puncs = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for e in st:
        if e in puncs:
            st = st.replace(e,"")

    list = st.split()
    count = list.count("dog")
    print(count)   
    return None


#Q10
def lambdafunc(seq):
    
    print(list(filter(lambda element: element[0] == 's', l)))
    
    return None


#Q11
def caught_speeding(speed, is_birthday):
    if bday == True:
        if speed <= 65:
            a = "No ticket"
        elif speed > 65 and speed <=85:
            a = "Small Ticket"
        elif speed > 85:
            a = "Big ticket"
    else:
        if speed <= 60:
            a = "No ticket"
        elif speed > 60 and speed <=80:
            a = "Small Ticket"
        elif speed > 80:
            a = "Big ticket"
    
    print(a) 
    return None


## Numpy Exercises

import numpy as np

#Q11
def create_arr_of_fives():
    matrix = np.ones(10)*5 
    return list(matrix)


#Q12
def even_num():
    matrix = np.arrange(10,51,2)
    return list(matrix)


#Q13
def create_matrix():
    matrix = np.arrange(0,9).reshape(3,3)
    return (matrix).tolist()


#Q14
def linear_space():
    matrix = np.linspace(0,1,20)
    return list(matrix)


#Q15
def decimal_mat():
    matrix = np.around(np.linspace(0.01,1,100),decimals = 2).reshape(10*10)
    return (matrix).tolist()



def slices_1():
    
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
  # array([[12, 13, 14, 15],
  #      [17, 18, 19, 20],
  #      [22, 23, 24, 25]])

  return None



def slices_2():
    
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
  # array([[ 2],
  #      [ 7],
  #      [12]])

  return None 



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
