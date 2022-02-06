

# Answer the questions or complete the tasks outlined in bold below.


def power(a, b):
    # ** What is 7 to the power of 4?**
    x = a ** b
    return x


y = power(7, 4)
print(y)


def split_str(s):
    # ** Split this string:**
    #
    #     s = "Hi there Sam!"
    #
    # **into a list. **
    list = s.split()
    print(list)
    return None


split_str(s="Hi there Sam !")


def format(planet, diameter):
    # ** Given the variables:**
    #
    #     planet = "Earth"
    #     diameter = 12742
    #
    # ** Use .format() to print the following string: **
    #
    #     The diameter of Earth is 12742 kilometers.
    print("The diameter of {a} is {b} kilometers.".format(a=planet, b=diameter))



format(planet="Earth", diameter=12742)


def indexing(list):
    # ** Given this nested list, use indexing to grab the word "hello" **

    # lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
    print(list[3][1][2][0])
    return None


indexing(lst=[1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7])


def dictionary(d):
    # ** Given this nested dictionary grab the word "hello". Be prepared, this will be annoying/tricky **

    # d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
    print(d['k1'][3]['tricky'][3]['target'][3])
    return None


dictionary(d={'k1': [1, 2, 3, {'tricky': ['oh', 'man', 'inception', {'target': [1, 2, 3, 'hello']}]}]})


def subjective():
    # ** What is the main difference between a tuple and a list? **
    # Tuple is immutable and list is mutable
    return None


subjective()


def domainGet():
    # ** Create a function that grabs the email website domain from a string in the form: **
    #
    #     user@domain.com
    #
    # **So for example, passing "user@domain.com" would return: domain.com**
    email = "mehulsharma@india.in"
    x = email.split("@")
    print(x[1])
    return None


domainGet()


def findDog(st="there are 2 dog in the colony"):
    # ** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **
    st.lower()
    lst2 = st.split()
    if 'dog' or 'Dog' or 'dOg' or 'DOG' or 'doG' or 'DoG' in lst2:
        print('true')
    else:
        print('false')
    return None


findDog()


def countDog(st='a dog is present there'):
    # ** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **
    counting = st.count('dog')
    print(counting)
    return None


countDog()


def lambdafunc(seq=['soup', 'dog', 'salad', 'cat', 'great']):
    # ** Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:**
    #
    #     seq = ['soup','dog','salad','cat','great']
    #
    # **should be filtered down to:**
    #
    #     ['soup','salad']
    print(list(filter(lambda x: x[0] in 's', seq)))

    return None


lambdafunc()


def caught_speeding():
    # **You are driving a little too fast, and a police officer stops you. Write a function
    #   to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket".
    #   If your speed is 60 or less, the result is "No Ticket". If speed is between 61
    #   and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big    Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all
    #   cases. **
    speed = int(input('Enter the speed of the driver'))
    if speed <= 60:
        print('no ticket')
    if speed > 60 and speed =< 80:
        print('small ticket')
    if speed > 80:
        print('big ticket')
    return None


caught_speeding()

## Numpy Exercises

import numpy as np


def create_arr_of_fives():
    #### Create an array of 10 fives
    #### Convert your output into list
    #### e.g return list(arr)
    a = np.array([5, 5, 5, 5, 5, 5, 5, 5, 5, 5])
    print(list(a))
    return None


create_arr_of_fives()


def even_num():
    ### Create an array of all the even integers from 10 to 50
    ### Convert your output into list
    ### e.g return list(arr)
    arr = np.arange(10, 51, 2)
    print(list(arr))
    return None


even_num()


def create_matrix():
    ### Create a 3x3 matrix with values ranging from 0 to 8
    ### Convert your output into list
    ### e.g return (arr).tolist()
    arr1 = np.random.randint(1, 9, 9)
    arr1 = arr1.reshape(3, 3)
    print(arr1)  # This will print a 3*3 matrix
    arr1 = arr1.tolist()  # Converted that matrix into list
    
    return None


create_matrix()


def linear_space():
    ### Create an array of 20 linearly spaced points between 0 and 1
    ### Convert your output into list
    ### e.g return list(arr)
    arr2 = np.arange(0, 1, 0.05)
    print(arr2)
    return None


linear_space()




def decimal_mat():
    ### Create an array of size 10*10 consisting of numbers from 0.01 to 1
    ### Convert your output into list
    ### e.g return (arr).tolist()
    arr3 = np.arange(0.01, 1.0001, 0.01).reshape(10, 10)
    print(arr3)
    return None


decimal_mat()


def slices_1():
    # This is a given array
    arr4 = np.arange(1, 26).reshape(5, 5)
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
    arr4 = arr4[2:, 1:]
    print(arr4)
    return None


slices_1()


def slices_2():
    # This is a given array
    arr5 = np.arange(1, 26).reshape(5, 5)
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
    arr5 = arr5[:3, 1]
    arr5 = arr5.reshape(3, 1)
    print(arr5)
    return None


slices_2()


def slices_3():
    # This is a given array
    arr6 = np.arange(1, 26).reshape(5, 5)
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
    arr6 = arr6[3:, :]
    print(arr6)
    return None


slices_3()

# Great job!

