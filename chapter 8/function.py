#Function Definition
"""def avg():
    a = int(input("Enter a:"))
    b = int(input("Enter a:"))
    c = int(input("Enter a:"))
    average= (a+b+c)/3
    print("The average is:",average)

avg() #Function call
print("Thank You.")
"""

#Function with Arguments
"""def gooday(name,ending):
    print("Good day," + name)
    print(ending)
    
gooday("Pratik","Thank You")
"""
#Function with argument with return
"""def gooday(name,ending):
    gr = "Good day " + name + "\n"+ending
    return gr

a = gooday("Pratik","Thank you")
print(a)
"""
#Default parameter value
"""
def val(name,ending="Thank you"):
    print(f"Good day {name}")
    print(ending)
    
val("Pratik")"""

#Factorial using Recursion
"""def fact(num):
    if(num == 1 or num == 0):
        return 1
    return num * fact(num-1)
         
a = int(input("Enter the number:"))
print(f"Factorial of {a}:{fact(a)}")"""