from array import *

arr = []
n = int(input("enter the length of array :"))

for i in range(n):
    x = int(input("next value :"))
    arr.append(x)

print(arr)

val = int(input("enter the value for search : "))

k = 0

for e in arr:
    if e == val:
        print("postion : ",k)
        break
    k+=1

