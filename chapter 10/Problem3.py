class Attribute:
    a = 0
    
o1 = Attribute()
print(o1.a)  # Prints the class attribute because instance attribute is not present
o1.a = 1  
print(o1.a)  #Prints the instance attribute bacause instance attribute is present
print(Attribute.a) #prints the class attribute