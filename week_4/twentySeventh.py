#oops in python

class Computer:
    def config(self):
        print("i5, 16GB, 1TB")

# x = 9

# print(type(x))

# a = '8'
# print(type(a))

com = Computer()
print(type(com))

com2 = Computer()
print(type(com2))

Computer.config(com)
# com2.config()

a = 5
print(a.bit_length())