class Employee: # this is an class
    #these are class attributes
    language = "Python"
    salary = 50000

pratik = Employee()  # here pratik is object
pratik.name = "Pratik Nikam" #object or instance attribute
pratik.gender = "Male"
print(pratik.name,pratik.language,pratik.salary,pratik.gender)

harry = Employee()
harry.name = "harry ji"
harry.gender = "Male"
print(harry.name,harry.language,harry.salary,harry.gender)

# here name and gender is object attributes and language & salary is class attributes as they directly belongs to the class 