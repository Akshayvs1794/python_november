#constuctor inheritence and Method resolution order(MRE) in python

class A:
    def __init__(self):
        print("in A init ..")

class B:
    def __init__(self):
        #super().__init__()
        print("in B init ..")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("in C init ..")

obj = C()