#functions in python

def greet():
    print("Hello")
    print("Have a nice day")

greet()

def add(x,y):
    z = x+y
    return z

result = add(6,5)
print(result)

def add_sub(a,b):
    c = a+b
    d = a-b
    return c,d

result2, result3 = add_sub(10,6)

print("add :", result2, "sub :",result3)