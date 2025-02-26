import numpy as np

arr = np.array([1,2,3,4])

#get first element
print("arr[0] is : ", arr[0])

#get first and last element
print("arr[0] is ", arr[0], " and arr[-1] is : ", arr[-1])

#getting index from a 2d array
arr2d = np.array([[1,2,3], [6,7,8]])

print("get 2 row , 2nd column, 2nd value : ", arr2d[1, 1])

print("get 1st value from 2nd row , 2nd column", arr2d[1,0])


arr3d = np.array([[[1,2,3], [5,6,7], [6,7,1]]])

print("arr3d : \n", arr3d)
#getting last value from the last col and last row
print(arr3d[0, -1, -1])