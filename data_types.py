'''
Data Types in NumPy
NumPy has some extra data types, and refer to data types with one character, like i for integers, u for unsigned integers etc.

Below is a list of all data types in NumPy and the characters used to represent them.

i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
'''

import numpy as np

arr = np.array([1,2,3,4])

print("arr.dtype", arr.dtype)

fruits = np.array(["apple", "banana", "cherry"])
print("fruits.dtype", fruits.dtype)

#creating array with data type string
arr_string = np.array(['apple', 'watermelon', 'chery'], dtype='S')

person = {
    "name": "John",
    "age": 36,
    "country": "Norway"
}

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}


#creating array with object data type

arr_object = np.array([person, car], dtype='O')


#change the exisiting arr to int type
my_arr_example = np.array([1,2,3,4])
my_arr_int = my_arr_example.astype(int)
print("my_arr_int.dtype", my_arr_int.dtype)