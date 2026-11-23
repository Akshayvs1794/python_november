#variable length argument

def sum(a, *b):
    c = a
    for i in b : 
        c = c + i
    print(c)

sum(5,4,5,6)