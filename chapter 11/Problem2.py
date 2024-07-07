class Animal:
    pass
class Pets(Animal):
    pass
class Dog(Pets):
    @staticmethod
    def bark():
        print("Bhow Bhow Bhow!!!")

a = Dog()
a.bark()