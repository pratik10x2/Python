class Employee:
    name = "Pratik nikam"
    language = "Python"
    salary = 1500000
    
    def getInfo(self):
        print(f"The language is {self.language}\nThe salary is {self.salary}")
    
    
    @staticmethod #when the object has no attributes and then we use @staticmethod 
    def greet():
        print("Good Morning everyone")

pratik = Employee()
pratik.language="javascript"
pratik.greet()
pratik.getInfo()
