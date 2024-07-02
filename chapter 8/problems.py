#Problem number 1
# Write a program using functions to find greatest of three numbers.
"""def greatest_number(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
    
a =int(input("Enter number:"))    
b =int(input("Enter number:"))    
c =int(input("Enter number:"))    
print(f"Greatest number is:{greatest_number(a,b,c)}")"""
        
    
#Problem number 2
#  Write a python program using function to convert Celsius to Fahrenheit.
"""def f_to_c(farenheit):
    return (farenheit - 32)*5/9
    
f = int(input("Enter temperature into celcius:"))
c = f_to_c(f)
print(f"{round(c,2)} °C")"""

#Problem number 3
# How do you prevent a python print() function to print a new line at the end.
"""print("a")
print("b")
print("c",end=" ")
print("d",end=" ")"""


#Problem number 4
# Write a recursive function to calculate the sum of first n natural numbers.
'''def total_sum(n):
    if(n == 1):
        return 1
    return total_sum(n-1) + n

print(total_sum(5))'''

#Problem number 5
#  Write a python function to print first n lines of the following pattern:
# ***
# ** - for n = 3
# *
'''def pattern(n):
    if(n == 0):
        return
    print("*" * n)
    pattern(n-1)
    
pattern(3)'''

#Problem number 6
# Write a python function which converts inches to cms.
'''def inch_to_cms(inch):
    return inch * 2.54

n =  int(input("Enter value is inches:"))
print(f"The value in centimeters is: {round(inch_to_cms(n),2)} cms")'''

#Problem number 7
# Write a python function to remove a given word from a list ad strip it at the same time
'''def remove(l,word):
    n = []
    for item in l:
        if (item != word):
            n.append(item.strip(word))
    return n
    
l = ["Harry","sohan","rohan","an"]
print(remove(l,"an"))'''

#Problem number 8
# Write a python function to print multiplication table of a given number.
'''def mul_table(num):
    for i in range(1,11):
        print(f"{num} X {i}: {num*i}")
    
mul_table(5)''' 