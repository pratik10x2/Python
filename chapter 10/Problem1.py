class Programmer:
    company = "Microsoft"
    def __init__(self,name,position,language,salary):
        self.name = name
        self.position = position
        self.language = language
        self.salary = salary
        
p1 = Programmer("Pratik Nikam","SWE","Python",200000)
print(p1.name,p1.position,p1.language,p1.salary,p1.company)
p2 = Programmer("Sakshi Patil","SDE","Python",200000)
print(p2.name,p2.position,p2.language,p2.salary,p2.company)
p3 = Programmer("Pratiksha Sawant","STE","Python",200000)
print(p3.name,p3.position,p3.language,p3.salary,p3.company)
    
