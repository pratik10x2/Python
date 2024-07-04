# str1= "This is a string.\tWe are creating in python"
# print(str1)

# 'this is my laptop" also mobile '
# str1 = "Apna"
# str2 = "College"
# finalStr= str1+ str2
# print(finalStr)
# len1= len(str1)
# len2= len(str2)
# print(len1)
# print(len2)
 
 
### INDEXING
 
# str = "Hello World"
# print(str[:5])
# print(str[2:5])
# print(str[2:])
# print(str[-3:-1])

# print(str[0])
# print(str[4])

###  STRING FUNCTIONS 
# str = "i am coooopder"

# print(str.endswith("ff")) #True
# print(str.capitalize())
# print(str.replace("coder" , "programmer"))
# print(str.find("i"))
# print(str.count("o"))
# print(str.upper())
# print(str.lower())


## WAP TO INPUT USER'S FIRST NAME & PRINT ITS LENGTH
"""
str = input("Enter your name:")
print("Your name length is: ",len(str)) 
"""

## WAP TO FIND  THE OCCURRENCE IN A STRING
"""
str = input("Enter string:")
print("$ in a string are: ",str.count("$")) 
"""

### CONDITIONAL STATEMENTS

# age =13

# if(age >= 18):
#     print("You are eligible for voting and driving.")
# else:
#     print("You are not eligible for voting and driving.")

# light = input("Enter light colour:")

# if(light == "green"):
#     print("GO")
# elif(light == "yellow"):
#     print("LOOk")
# elif(light == "red"):
#     print("STOP")
# else:
#     print("You entered wrong light.....")

# ## GRADE STUDENTS BASED ON MARKS

# marks = int(input("Enter marks:"))

# if(marks >= 90):
#     grade = "A"
# elif(marks >= 80 and marks <90):
#     grade = "B"
# elif(marks >= 70 and marks < 80):
#     grade = "C"
# elif( marks >= 60 and marks < 70):
#     grade = "D"
# else:
#     grade = "F"

# print("Grade of a student is: " , grade)

# ## WAP TO CHECK IF A NUMBER ENTERED BY THE USER IS ODD OR EVEN
# num = int(input("Enter the number:"))

# if(num % 2 == 0):
#     print("Number is EVEN.")
# else:
#     print("Number is ODD.")

# ## WAP TO FIND THE GREATEST OF 3 NUMBERS ENTERED BY THE USER
# num1 = int(input("Enter first number:"))
# num2 = int(input("Enter second number:"))
# num3 = int(input("Enter third number:"))

# if(num1 >= num2 and num1 >= num3 ):
#     num = num1
# elif(num2 >= num3 and num2 >= num1):
#     num = num2
# else:
#     num = num3 
# print("The greatest number is:",num)


# ## WAP TO CHECK IF A NUMBER IS MULTIPLE OF 7 OR NOT
# num = int(input("Enter the number:"))

# if(num % 7 == 0):
#     print(num," is divisible by 7")
# else:
#     print(num," is not divisible by 7")

##LARGEST OF 4
num1= int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
num3 = int(input("Enter third number:"))
num4 = int(input("Enter fourth number:"))

if(num1 >= num2 and num1 >= num3 ):
    num = num1
elif(num2 >= num3 and num2 >= num4):
    num = num2
elif(num3 >= num4):
    num = num3 
else:
    num = num4
    
print("The greatest number is:",num)