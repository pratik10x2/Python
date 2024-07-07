class Calculator:
    def __init__(self,num):
        self.num = num

    @staticmethod
    def greet():
        print("Good Morning Everyone.....")
    
    def square(self):
        print(f"The square is {self.num * self.num}")
    def cube(self):
        print(f"The cube is {self.num * self.num * self.num}")
    def squareroot(self):
        print(f"The squareroot is {self.num ** 1/2}")
        
    
num = Calculator(25)
num.greet()
num.square()
num.cube()
num.squareroot()

        