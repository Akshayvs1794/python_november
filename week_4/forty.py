#exception handling in python 
a = int(input("a : "))
b = int(input("b : "))

try:
    print("resource open")
    print(a / b)

except ValueError as e:
    print("ValueError ", e) 

except ZeroDivisionError as e:
     print("ZeroDivisionError :",e)

except Exception as e:
     print("Something went wrong !!")

finally:
        print("resource closed")