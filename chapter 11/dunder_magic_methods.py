# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
#     def __str__(self):
#         return f"{self.name} {self.age}"
#     def __repr__(self):
#         return f"{self.name} {self.age}"

# p = Person("Pratik Nikam",21)
# print(p)
# print(str(p))
# print(repr(p))
        
    
class Mylist:
    def __init__(self,item):
        self.item = item 
        
    def __len__(self):
        return len(self.item)

list1 = [1,2,4,"Pratik", "Harry",21]
print(len(list1))