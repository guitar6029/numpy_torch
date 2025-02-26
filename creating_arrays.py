import numpy as np

# arr = np.array([[1,2,3],[4,5,6], [2,6, 12]])

# print("arr : ", arr)
# print(" arr shape : ", arr.shape)

# #size of arr
# print("arr size : ", arr.size)

# #print version of numpy
# print("numpy version : ", np.__version__)

#np tuple example
tup = np.array([(1,2,3), (4,5,6)])
print("tup : ", tup)

#0-d arrays
zero_d_arr = np.array(22)
print("zero_d_arr : ", zero_d_arr)

#1-d arrays
one_d_arr = np.array([1,2,3])
print("one_d_arr : ", one_d_arr)

#2-d arrays
two_d_arr = np.array([[1,2], [4,5]])
print("two_d_arr : ", two_d_arr)

#3d arrays
three_d_arr = np.array([ [4,5,6], [6,7,8], [7,2,1]])
print("three_d_arr : ", three_d_arr)

# longer way of creating a 5d array
dim_5 = np.array([[[[[1,2], [2,3]]]]])

#check the dimensions of the array(s)
print("three_d_arr.ndim : ", three_d_arr.ndim)
print("two_d_arr.ndim : ", two_d_arr.ndim)

print("dim_5.ndim : ", dim_5.ndim)

#shorter / easier way to create 5 dimensional array
dim5 = np.array([6,7,8], ndmin=5)
print("dim5 : ", dim5.ndim)