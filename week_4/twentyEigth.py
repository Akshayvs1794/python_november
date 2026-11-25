# init() in python

class Computer:

    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Our PC config is : ",self.cpu, self.ram)

com1 = Computer("intel i5",16)
com2 = Computer("Ryzen 5", 16)

com1.config()
com2.config()