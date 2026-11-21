from numpy import *

#ways of creating array
arr = array([ 1, 2, 3, 4, 5 ])

print(arr.dtype)
print(arr)

arr2 = linspace(0,15,20)
print(arr2.dtype)
print(arr2)

arr3 = arange(1,15,2)
print(arr3)
print(arr3)

arr4 = logspace(1,40,5)
print('%2f' %arr4[4])

arr5 = ones(5,int)
print(arr5)

arr6 = zeros(5, int)
print(arr6)