import numpy as np


#join two arrays 

arr1 = np.array([[1,2], [7,8]])
arr2 = np.array([[3,4], [5,6]])
arr3 = np.concatenate((arr1, arr2), axis=1)

print("arr3 : \n", arr3)

#joining arrays using stack functions
arr4 = np.stack((arr1, arr2), axis=1)
print("arr4 : \n", arr4)