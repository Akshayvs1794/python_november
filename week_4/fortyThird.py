#image handling in python

f = open('hritik.jpg','rb')

f2 = open('HR.jpg','wb')

for i in f:
    f2.write(i)