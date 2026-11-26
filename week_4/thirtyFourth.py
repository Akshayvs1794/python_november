#polymorphism in python

class Pycharm:
    def execute(self):
        print("compiling ..")
        print("Running")

class MyEditor:
    def execute(self):
        print("spell check..")
        print("convention check ..")
        print("compiling ..")
        print("Running ..")

class Laptop:
    def code(self,ide):
        ide.execute()

obj = MyEditor()
l1 = Laptop()
l1.code(obj)