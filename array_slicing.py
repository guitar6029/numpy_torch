import numpy as np
#print array 0 to 10 inclusive
arr = np.array(range(11))
print("arr : ", arr)

#print items 3:5
print("arr[3:5] : ", arr[3:5] )

#slice from beginning to index 4 included
print("arr[:5] : ", arr[:5])

#negative slicing , example
# from last one - 2, and last one excluded
print("arr[-2:] : ", arr[-3: -1])

#step by 2 example
print("arr[::2] :", arr[::2])


#slicing 2d array

arr2d = np.array([[1,2,3,4], [5,6,7,8]])
print("arr2d.ndim",arr2d.ndim)
#example
print(arr2d[1, :-1])