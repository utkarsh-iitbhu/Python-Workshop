
# ## Exercises

# Answer the questions or complete the tasks outlined in bold below.

#Task 1
# ** What is 7 to the power of 4?**

#Solution 1:
def power(a,b):
    c = a**b
    return c
d = power(7,4)
print(d)

print()

#Task 2
# ** Split this string:**
#     s = "Hi there Sam!"
# **into a list. **

#Solution 2:
def split_str(s):
    r = s.split()
    return r
t = "Hi there Sam!"
print(split_str(t))

print()

#Task 3
# ** Given the variables:**
#     planet = "Earth"
#     diameter = 12742
# ** Use .format() to print the following string: ** 
#     The diameter of Earth is 12742 kilometers.

#Solution 3:
def format(planet,diameter):
    toprint = "The diameter of {var1} is {var2} kilometers.".format(var1 = planet, var2 = diameter)
    return toprint
print(format("Earth", "12742"))

print()

#Task 4
# ** Given this nested list, use indexing to grab the word "hello" **
#lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]

#Solution 4:
def indexing(lst):
    word = lst[3][1][2][0]
    return word
l = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(indexing(l))

print()

#Task 5
# ** Given this nested dictionary grab the word "hello". Be prepared, this will be annoying/tricky **
# d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}

#Solution 5:
def dictionary(d):
    word = d['k1'][3]['tricky'][3]['target'][3]
    return word
e = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
print(dictionary(e))

print()

#Task 6
# ** What is the main difference between a tuple and a list? **
# Tuple is _______

#Solution 6:
def subjective():
    tupledef = "immutable"
    print(tupledef)
    return tupledef
subjective()

#Task 7:
#** Create a function that grabs the email website domain from a string in the form: **
# 
#     user@domain.com
#     
# **So for example, passing "user@domain.com" would return: domain.com**

#Solution 7:
def domainGet(email):
    emailid = email.split("@")
    domain = emailid[1]
    return domain
emailaddress = 'user@domain.com'
print(domainGet(emailaddress))

print()

#Task 8:
# ** Create a basic function that returns True if the word 'dog' is contained in the input string.
#Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **

#Solution 8:
def findDog(st):
    dogcheck = st.lower().split()
    if 'dog' in dogcheck:
        return True
    else:
        return False

print()

#Task 9:
# ** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **

#Solution 9:
def countDog(st):
    cd = 0
    dogcheck = st.lower().split()
    for i in dogcheck:
        if i == 'dog':
            cd += 1
    return cd

print()

#Task 10:
# ** Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:**
#     seq = ['soup','dog','salad','cat','great']
# **should be filtered down to:**
#     ['soup','salad']

#Solution 10:
def lambdafunc(seq):
    result = list(filter(lambda s: s.lower().startswith("s"), seq))
    return result

sequence = ['soup','dog','salad','cat','great']
print(lambdafunc(sequence))

print()

#Task 11:
# **You are driving a little too fast, and a police officer stops you. Write a function
#   to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". 
#   If your speed is 60 or less, the result is "No Ticket". If speed is between 61 
#   and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big Ticket".
#Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all 
#   cases. **

#Solution 11:
def caught_speeding(speed, is_birthday):
    if is_birthday:
        if speed <= 65:
            ticket = "No Ticket"
            return ticket
        elif speed > 65 and speed <= 85:
            ticket = "Small Ticket"
            return ticket
        else:
            ticket = "Big Ticket"
            return ticket
    else:
        if speed <= 60:
            ticket = "No Ticket"
            return ticket
        elif speed > 60 and speed <= 80:
            ticket = "Small Ticket"
            return ticket
        else:
            ticket = "Big Ticket"
            return ticket

print()

## Numpy Exercises

import numpy as np

#Task 12:
# Create an array of 10 fives
# Convert your output into list 
# e.g return list(arr)

#Solution 12:
def create_arr_of_fives():
    arr = np.ones(10)
    arr[ : ] = 5
    lst = list(arr)
    return lst
print(create_arr_of_fives())

print()

#Task 13
# Create an array of all the even integers from 10 to 50
# Convert your output into list 
# e.g return list(arr)

#Solution 13:
def even_num():   
    arr = np.arange(10, 51, 2)
    lst = list(arr)
    return lst
print(even_num())

print()

#Task 14:
# Create a 3x3 matrix with values ranging from 0 to 8
# Convert your output into list 
# e.g return (arr).tolist()

#Solution 14:
def create_matrix():
    arr = np.random.randint(0,9,9)
    narr = arr.reshape(3,3)
    lst = narr.tolist()
    return lst
print(create_matrix())

print()

#Task 15:
# Create an array of 20 linearly spaced points between 0 and 1
# Convert your output into list 
# e.g return list(arr)

#Solution 15:
def linear_space():
    arr = np.linspace(0,1,20)
    lst = arr.tolist()
    return lst
print(linear_space())

print()

#Task 16:
# Create an array of size 10*10 consisting of numbers from 0.01 to 1
# Convert your output into list 
# e.g return (arr).tolist()
#Solution 16:
def decimal_mat():
    narr = np.linspace(0.01, 1, 100)
    arr = narr.reshape(10, 10)
    lst = arr.tolist()
    return lst
print(decimal_mat())

print()

#Task 17:
#Solution 17:
# This is a given array
# array([[ 1,  2,  3,  4,  5],
#      [ 6,  7,  8,  9, 10],
#      [11, 12, 13, 14, 15],
#      [16, 17, 18, 19, 20],
#      [21, 22, 23, 24, 25]])
# Write a code to slice this given array
# Convert your output into list 
# e.g return (arr).tolist()
# array([[12, 13, 14, 15],
#      [17, 18, 19, 20],
#      [22, 23, 24, 25]])
def slices_1():
    arr = np.arange(1,26).reshape(5,5)
    slicedarr = arr[2: ,1: ]
    lst = slicedarr.tolist()
    return lst
print(slices_1())

print()

#Task 18:
# This is a given array
# array([[ 1,  2,  3,  4,  5],
#      [ 6,  7,  8,  9, 10],
#      [11, 12, 13, 14, 15],
#      [16, 17, 18, 19, 20],
#      [21, 22, 23, 24, 25]])
# Write a code to slice this given array
# Convert your output into list 
# e.g return (arr).tolist()
# array([[ 2],
#      [ 7],
#      [12]])
  
#Solution 18:
def slices_2():
    arr = np.arange(1,26).reshape(5,5)
    slicedarr = arr[ :3, 1:2]
    lst = slicedarr.tolist()
    return lst
print(slices_2())

print()

#Task 19:
# This is a given array
# array([[ 1,  2,  3,  4,  5],
#      [ 6,  7,  8,  9, 10],
#      [11, 12, 13, 14, 15],
#      [16, 17, 18, 19, 20],
#      [21, 22, 23, 24, 25]])
# Write a code to slice this given array
# Convert your output into list 
# e.g return (arr).tolist()
# array([[16, 17, 18, 19, 20],
#      [21, 22, 23, 24, 25]])
  
#Solution 19:
def slices_3():
    arr = np.arange(1,26).reshape(5,5)
    slicedarr = arr[3: ]
    lst = slicedarr.tolist()
    return lst
print(slices_3())

print()

# Great job!
