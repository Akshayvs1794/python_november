a = float(input("Enter 1st number : "))
b = float(input("Enter 2nd number : "))

op = input("enter operator(+,-,*,/,%,**) : ")

if op == '+':
    print(a+b)
elif op == '-':
    print(a-b)
elif op == '*':
    print(a*b)
elif op == '/':
    print(a/b)
elif op == '%':
    print(a%b)
elif op == '**':
    print(a**b)

else:
    print("Invalid operations ..")    