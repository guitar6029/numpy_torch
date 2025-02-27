import numpy as np

arr = np.array([11,12,13])

for x in arr:
    print("Index value : ", x)
    
    
#example 2d array
arr2d = np.array([[1,2,3], [4,5,6]])
for row in arr2d:
    print("Row values : ", row)
    for y in row:
        print("Index value : ", y)    
        
#example 3d array
arr3d = np.array([[[1,2,3], [7,8,9]]])
print("arr3d dim : ", arr3d.ndim)  
for row in arr3d:
    for col in row:
        for x in col:
            print("Index value : ", x)      
            
            
# as you coul see the more dimensions , the more for loop
# are required, so lets try using a helper function
# call nditer
arr5d = np.array([[[[[1,2,3], [7,8,9], [10,11,12]]]]])            
print("arr dim :", arr5d.ndim)

for x in np.nditer(arr5d):
    print("Index value : ", x)
    
# as you can see, its so much easier to access the nested arrays    
        
#lets try another example, this time 
# it skips 1 element
arr = np.array([[1,2,3], [5,6,7]])
for x in np.nditer(arr[:, :: 2]):
    print("Index value : ", x)        
    
"""
Enumeration means mentioning sequence number of somethings one by one.

Sometimes we require corresponding index of the element while iterating, the ndenumerate() method can be used for those usecases.
"""    

arr = np.array([[[1,2,3], [3,4,5], [5,6,7]]])
for idx, x in np.ndenumerate(arr):
    print("idx : ", idx, " value : ", x)