#types of methods in python

class Students:

    college = "IMCOST"

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return(self.m1+self.m2+self.m3)/3

    def get_m1(self):
        return self.m1

    def set_m1(self,value):
        if value < 0:
            raise ValueError("marks cannot be zero ..")
        self.m1=value
    @classmethod
    def getCollege(cls):
        return cls.college

    @staticmethod
    def info():
        print(f"This is student class ..")

s1 = Students(81,52,84)
s2 = Students(79,78,76)

print("Student 1 avg marks : ", s1.avg(),s1.getCollege())
print("Student 2 avg marks : ", s2.avg(),s2.getCollege())

print(Students.info())