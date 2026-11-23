#keyword variable argument
def person(name, **data):
    print(name)
    for i,j in data.items():
        print(i," => ",j)

person('Akshay', age=30,city="Kalyan", mob=7021181993)