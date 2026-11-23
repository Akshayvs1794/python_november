#global keyword
a = 10

def show():
    a = 9
    x = globals()['a']
    print(id(x))
    print("local a : ",a)

    globals()['a'] = 15

print(id(a))
show()

print("outside a : ",a)