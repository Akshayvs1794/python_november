#file handling in python

try:

    file = open ('textFile','r')

    # for data in file:
    #     print(data)

    #print(f.read())
    #print(f.readline(),end="")
    #print(f.readline())

    file2 = open('textFile2','w')


    for data in file:
        file2.write(data)
#    file2.write("Something")

#    print(file2)

except FileNotFoundError as fe:
    print("FileNotFoundError : ",fe)