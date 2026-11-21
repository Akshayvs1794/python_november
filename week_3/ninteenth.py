from numpy import *

arr = array([ 1, 2, 3, 4, 5 ])
arr = arr + 5  #adding 5 to each element of an array
print(arr)

#vectorinzed operation
arr1 = array([ 1, 2, 3, 4, 5 ])
arr2 = array([ 2, 1, 9, 3, 2 ])

arr3 = arr1 + arr2 # [ 3  5 12  7 11]
print(arr3)

#numpy maths operations

print("max in arr3 : ",max(arr3))
print("min in arr3 : ",min(arr3))
print("sqrt in arr3 : ",sqrt(arr3))
print("sum in arr3", sum(arr3))
print("sort arr3", sort(arr3))
print("unique element in arr3", unique(arr3))