import numpy as np

arr = np.array(range(1,13))
print("arr : ", arr)

#convert to 2d with 4 rows
reshaped_arr = arr.reshape(4,3)

print("reshaped_arr : \n", reshaped_arr)

#another example of reshape , and flatten array
arr = np.array([[[[1,2], [2,3], [4,5]]]])
print("arr : \n", arr)
print("arr ndim : \n", arr.ndim)

#reshape to 1D array
dim1_arr = arr.reshape(-1)
print("dim1_arr : \n", dim1_arr)