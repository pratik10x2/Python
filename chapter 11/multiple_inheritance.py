class Employee:
    company = "Google"
    name = "Pratik nikam"
    def show(self):
        print(f"The name of the employee is {self.name} and company name is {self.company}")

class Coder:
    language = "Python"
    def showLanguage(self):
        print(f"out of all languages here is your language: {self.language}")
    
class Programmer(Employee,Coder):
    company = "Microsoft"
    def showInfo(self):
        print(f"The name of the company is {self.company} and the language is used {self.language} and the name of the Programmer is {self.name}")
        
a = Employee()
b = Coder()
c = Programmer()

c.show()
c.showLanguage()
c.showInfo()