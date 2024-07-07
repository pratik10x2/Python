class Employee:
    a = 1 
    @classmethod  # when we write @classmethod it gives a = 1 which is class attribute, using this we print the class attribute with change in instance atribute but value is always of class attribute
    #in classmethod we use 'cls' instead of self
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

e = Employee()
e.a = 24 # @classmethod is used so instance attribute does not change value of a
e.show()