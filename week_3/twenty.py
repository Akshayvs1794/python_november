from numpy import *

#copying in array


arr1 = array([ 1,2,3,4,5 ])
arr2 = arr1.view() #shallow copy
#arr2 = arr1.copy() #deep copy

print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))