#tuple in python
tup = ( 21, 36, 14, 21, 25, 67,21 )

print(tup)

for i in tup:
    print(i)

print(tup[3])
#tup[0] = 100 #TypeError: 'tuple' object does not support item assignment
print(tup.count(21))
print(tup.index(25))