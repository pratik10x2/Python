class Employee:
    company = "Google"
    name = "Pratik Nikam"
    salary = 2000000
    def show(self):
        print(f"The name of the employee is {self.name} and salary is {self.salary}")

class Programmer(Employee):
    company = "Microsoft"
    name = "Harry Singh"
    lang = "Python"
    def showLang(self):
        print(f"The name of the programmer is {self.name} and languagee is {self.lang}")

a =Employee()
b = Programmer()

a.show()
b.showLang()
b.show()

print(a.company,b.company)
