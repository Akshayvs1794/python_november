#constuctor in python, self, object comparision

class Person:
    def __init__(self):
        self.name = "Akshay"
        self.age = 30

        #print("Name : ",self.name,", Age : ",self.age)

    def update(self):
        self.name="Sayali"
        self.age = 27
        #print("Name : ",self.name,", Age : ",self.age)

    def show(self):
         print(f"Person name is {self.name} and person age is {self.age}")


    def compare(self,other):
            if self.age == other.age:
                return True
            else:
                return False
            
p1 = Person()
p2 = Person()

p2.update()
p2.show();
print(p1.name, p1.age)
print(p2.name, p2.age)


if p1.compare(p2):
     print("they are same")
else:
     print("they are different")