### Exercises

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
    lst1 = s.split()
    print(lst1)
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
    print("The diameter of {one} is {two} kilometers.".format(one=planet, two=diameter))



format(planet="Earth", diameter=12742)


def indexing(lst):
    # ** Given this nested list, use indexing to grab the word "hello" **

    # lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
    print(lst[3][1][2][0])
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
    # Tuple is _______
    # Tuple is immutable , the values/strings assigned to it once cannot be changed later
    # Whereas in list we can change the values assigned to it whenever we want
    return None


subjective()


def domainGet():
    # ** Create a function that grabs the email website domain from a string in the form: **
    #
    #     user@domain.com
    #
    # **So for example, passing "user@domain.com" would return: domain.com**
    email = "cops@iitbhu.com"
    x = email.split("@")
    print(x[1])
    return None


domainGet()


def findDog(st="see there is a Dog"):
    # ** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **
    st.lower()
    lst2 = st.split()
    if 'dog' or 'Dog' or 'dOg' or 'DOG' or 'doG' or 'DoG' in lst2:
        print('true')
    else:
        print('false')
    return None


findDog()


def countDog(st='a dog is a dog and dog barks'):
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
        print('No Ticket')
    if speed > 60 and speed < 80:
        print('Small Ticket')
    if speed > 80:
        print('Big Ticket')
    return None


caught_speeding()

## Numpy Exercises

import numpy as np


def create_arr_of_fives():
    #### Create an array of 10 fives
    #### Convert your output into list
    #### e.g return list(arr)
    arr = np.array([5, 5, 5, 5, 5, 5, 5, 5, 5, 5])
    print(list(arr))
    return None


create_arr_of_fives()


def even_num():
    ### Create an array of all the even integers from 10 to 50
    ### Convert your output into list
    ### e.g return list(arr)
    a = np.arange(10, 51, 2)
    print(list(a))
    return None


even_num()


def create_matrix():
    ### Create a 3x3 matrix with values ranging from 0 to 8
    ### Convert your output into list
    ### e.g return (arr).tolist()
    b = np.random.randint(1, 9, 9)
    b = b.reshape(3, 3)
    print(b)  # This will print a 3*3 matrix
    b = b.tolist()  # Converted that matrix into list
    print(type(b))
    return None


create_matrix()


def linear_space():
    ### Create an array of 20 linearly spaced points between 0 and 1
    ### Convert your output into list
    ### e.g return list(arr)
    c = np.arange(0, 1, 0.05)
    print(c)
    return None


linear_space()




def decimal_mat():
    ### Create an array of size 10*10 consisting of numbers from 0.01 to 1
    ### Convert your output into list
    ### e.g return (arr).tolist()
    d = np.arange(0.01, 1.0001, 0.01).reshape(10, 10)
    print(d)
    return None


decimal_mat()


def slices_1():
    # This is a given array
    arr = np.arange(1, 26).reshape(5, 5)
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
    arr = arr[2:, 1:]
    print(arr)
    arr = arr.tolist()
    print(type(arr))
    
    return None


slices_1()


def slices_2():
    # This is a given array
    arr = np.arange(1, 26).reshape(5, 5)
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
    arr = arr[:3, 1]
    arr = arr.reshape(3, 1)
    print(arr)
    arr = arr.tolist()
    print(type(arr))
    return None


slices_2()


def slices_3():
    # This is a given array
    arr = np.arange(1, 26).reshape(5, 5)
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
    arr = arr[3:, :]
    print(arr)
    arr = (arr).tolist()
    print(type(arr))

    return None


slices_3()

# Great job!

