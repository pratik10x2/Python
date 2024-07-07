class Employee:
    salary = 2000000
    company = "Microsoft"
    def show(self):
        print(f"The salary of the employee is {self.salary} in {self.company}")
        
class Coder(Employee):
    language = "Python"
    def showLang(self):
        print(f"The company name is {self.company} and language used by {self.company} is {self.language}")

class Programmer(Coder):
    name = "Pratik Nikam"
    company = "Google"
    def allInfo(self):
        print(f"The programmer name is {self.name} and compny name is {self.company} & this company provides {self.salary} salary.")
             
a = Employee()
b = Coder()
c = Programmer()

# a.show()
# b.show()
# c.show()
c.showLang()
c.allInfo()