class Employee:
    name = "Pratik Nikam"
    language = "Python"
    salary = 1500000
    
    def __init__(self,name,language,salary):
        self.name = name
        self.language = language
        self.salary = salary
        # print("Hello ji mai init hu jo ki pass ho raha hu without calling.")
    
    def getInfo(self):
        print(f"The language is {self.language}\nThe salary is {self.salary}")
    
    
    @staticmethod #when the object has no attributes and then we use @staticmethod 
    def greet():
        print("Good Morning everyone")
        
pratik = Employee("Pratik Nikam","CPP",300000)
print(pratik.name,pratik.language,pratik.salary)

harry = Employee("Harry Singh","Javascript",200000)
print(harry.name,harry.language,harry.salary)

sakshi = Employee("Sakshi Patil","Java",2500000)
print(sakshi.name,sakshi.language,sakshi.salary)

# harry.greet()
# harry.getInfo()
