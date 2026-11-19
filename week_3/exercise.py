#1. print all odd numbers from 1 to 20

# for i in range(1,21,2):
#     #if i%2!=0:
#         print(i)

#2. print table of 57

# for i in range(1,11):
#     print(i*57)

#3.Print all multiple of 3 from 1 to 50 but skip 15
# for i in range(1,51):
#     if i==15:
#         continue
#     if i%3==0:
#         print(i)

#4. take 2 integers as input a and b 
# find and print the first number between 1 and 1000 
# that is divisible by both numbers

a = int(input("a : ")) 
b = int(input("b : "))

found = False

for i in range(1,1001):
    if i%a==0 and i%b==0:
        print("The first number divisible by both is :",i)
        found = True
        break   

if not found:
    print("No number between 1 to 1000 is divisible by both ..")