import numpy as np
# copy example
arr = np.array([1,2,3,4])
copy_arr = arr.copy()

arr[0] = 32
print("arr : ", arr)
print("copy_arr : ", copy_arr)


#view example
arr = np.array([5,6,7,8])
view_arr = arr.view()
arr[-1] = 130
print("arr : ", arr)
print("view_arr :", view_arr)


#check if array owns its data
arr = np.array([22,24,26,28])
x = arr.copy()
y = arr.view()

#print the base 
print("x base :", x.base)
print("y base :", y.base)