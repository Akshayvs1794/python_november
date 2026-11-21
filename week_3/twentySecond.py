#function argument : mutable and immutable argument
# def update(x):
#     print('x : ',x)
#     print(id(x))

#     x = 8
#     print('x : ',x)
#     print(id(x))

# a = 10
# print("a : ", a)
# print(id(a))

# update(a)

# print("a : ", a)
# print(id(a))

#passing list to an function : 

def update(lst):
    print('list : ',lst)
    print(id(lst))

    lst[1] = 25
    print('lst : ',lst)
    print(id(lst))

lst = [ 10,20,30,40 ]
print("list : ", lst)
print(id(lst))

update(lst)

print("list : ", lst)
print(id(lst))