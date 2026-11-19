#Dictionary in python 

marks = { "math" : 99, "physics" : 98, "chemistry" : 92, "biology" : 91 }

print(marks, type(marks))

marks["english"] = 94
marks["marathi"] = 97
# for i in marks:
#     print(i," : ", marks[i])

# for key in marks.keys():
#     print(key," : ", marks.get(key))

#if we want to print only values
for v in marks.values():
    print(v)