
# ## Exercises

# Answer the questions or complete the tasks outlined in bold below.


import numpy as np


def power(a, b):

    # ** What is 7 to the power of 4?**

    return a**b


def split_str(s):

    # ** Split this string:**
    #
    #     s = "Hi there Sam!"
    #
    # **into a list. **

    array = s.split()

    return list(array)


def format(planet, diameter):

    # ** Given the variables:**
    #
    #     planet = "Earth"
    #     diameter = 12742
    #
    # ** Use .format() to print the following string: **
    #
    #     The diameter of Earth is 12742 kilometers.
    result = "The diameter of {one} is {two} kilometers.".format(
        one=planet, two=diameter)

    return result


def indexing(lst):

    # ** Given this nested list, use indexing to grab the word "hello" **

    #lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
    arr = lst[3][1][2][0]
    return arr


def dictionary(d):

    # ** Given this nested dictionary grab the word "hello". Be prepared, this will be annoying/tricky **

    # d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}

    arr = d['k1'][3]['tricky'][3]['target'][3]
    return arr


def subjective():

    # ** What is the main difference between a tuple and a list? **
    # Tuple is _______
   
    return 'immutable'

 def domainGet(email):

    # ** Create a function that grabs the email website domain from a string in the form: **
    #
    #     user@domain.com
    #
    # **So for example, passing "user@domain.com" would return: domain.com**
    str = email.split('@')[1]
    return str


def findDog(st):

    # ** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **
    arr='dog' in st.lower().split()
    return arr


def countDog(st):

    # ** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **
   count = 0
   for word in st.lower().split():
        if word == 'dog':
            count= count + 1
   return count
    


def lambdafunc(seq):

    # ** Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:**
    #
    #     seq = ['soup','dog','salad','cat','great']
    #
    # **should be filtered down to:**
    #
    #     ['soup','salad']
    arr=list(filter(lambda word: word[0]=='s',seq))
    return arr


def caught_speeding(speed, is_birthday):

    # **You are driving a little too fast, and a police officer stops you. Write a function
    #   to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket".
    #   If your speed is 60 or less, the result is "No Ticket". If speed is between 61
    #   and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big    Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all
    #   cases. **
     if is_birthday:
        appspeed = speed - 5
     else:
        appspeed = speed
    
     if appspeed > 80:
        return 'Big Ticket'
     elif appspeed > 60:
        return 'Small Ticket'
     else:
        return 'No Ticket'

     


# Numpy Exercises


def create_arr_of_fives():

    # Create an array of 10 fives
    # Convert your output into list
    # e.g return list(arr)
     arr=np.ones(10)*5
     answer=list(arr)
     return answer
 


def even_num():

    # Create an array of all the even integers from 10 to 50
    # Convert your output into list
    # e.g return list(arr)
   arr=np.arange(10,51,2)
   answer=list(arr)
   return answer
    


def create_matrix():

    # Create a 3x3 matrix with values ranging from 0 to 8
    # Convert your output into list
    # e.g return (arr).tolist()
    arr=np.arange(0,9).reshape(3,3)
    answer=(arr).tolist()
    return answer
    


def linear_space():

    # Create an array of 20 linearly spaced points between 0 and 1
    # Convert your output into list
    # e.g return list(arr)
    arr=np.linspace(0, 1, num=20)
    answer=list(arr)
    return answer
    


def decimal_mat():

    # Create an array of size 10*10 consisting of numbers from 0.01 to 1
    # Convert your output into list
    # e.g return (arr).tolist()
    arr1= np.arange(1,101).reshape(10,10)
    int = 100
    arr2=arr1/int
    answer=(arr2).tolist()
    return answer
    


def slices_1():

    # This is a given array
    arr = np.arange(1, 26).reshape(5, 5)
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
    a=arr[2:,1:]
    b =(a).tolist()
    return b
    


def slices_2():

    # This is a given array
    arr = np.arange(1, 26).reshape(5, 5)
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
    a=arr[0:3,1:2]
    b =(a).tolist()
    return b
  


def slices_3():

    # This is a given array
    arr = np.arange(1, 26).reshape(5, 5)
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
    a=arr[3:0,0:0]
    b =(a).tolist()
    return b
   


# Great job!
