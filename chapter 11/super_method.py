class Employee:
    def __init__(self):
        print("Constructor of a Employee")
    a =1 

class Programmer(Employee):
    def __init__(self):
        print("Constructor of a Programmer")
    b =2

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of a Manager")
    c=3

o= Manager()
print(o.a , o.b,o.c)