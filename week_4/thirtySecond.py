#Inheritance in python

class A:
    def feature1(self):
        print("feature1 in A class ..")

class B():
    def feature2(self):
        print("feature2 in B class ..")

class C(A,B):
    def feature3(self):
        print("feature3 in C class ..")

obj = A()
obj.feature1()

obj2 = B()
# obj2.feature1()
obj2.feature2()

obj3 = C()
obj3.feature1()
obj3.feature2()
obj3.feature3()