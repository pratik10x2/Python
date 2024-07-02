# Problem number 1
"""num = int(input("Enter number:"))

for i in range(1,11):
    # mul = num * i
    print(f"{num} X {i}: {num * i}")"""

# # Problem number 2
"""l = ["Harrn", "Sohan", "Sachin", "Sahun"]
for name in l:
    if(name.endswith("n")):
        print(f"Hello {name}")"""

# # Problem number 3
"""num = int(input("Enter number:"))
i = 1
while(i<11):
    print(f"{num}X{i}: {num * i}")
    i+=1
"""
# # Problem number 4
"""num = int (input("enter a number:"))

for i in range(2,num):
    if(num%i==0):
        print("Number is not Prime.")
        break
else:
    print("Number is Prime.")"""

# #Problem number 5
"""num = int(input("Enter number:"))
i=1
sum=0
while(i <= num):
    sum+=i
    i+=1

print(sum)"""

# #Problem number 6
"""num = int(input("Enter number:"))
fact = 1
for i in range(1,num+1):
    fact= fact * i

print(fact)"""

# #Problem numbe 7
"""num = int(input("Enter number:"))
for i in range(1,num+1):
    print(" "*  (num-i),end="")
    print("*"*  (2*i-1),end="")
    print("")"""


# #Problem number 8
"""num = int(input("Enter number:"))
for i in range(1,num+1):
    print("*"*  (i),end="")
    print("")"""

# #Problem number 9
"""num = int(input("Enter number:"))
for i in range(1,num+1):
    if(i == 1 or i == num):
        print("*"*num,end="")
    else:
        print("*",end="")
        print(" "*(num-2),end="")
        print("*",end="")
    print("")
"""
# #Problem number 10
"""num = int(input("Enter number:"))

for i in range(1,11):
    print(f"{num}X{11-i}:{num * (11-i)}")"""


#Pattern
"""num = int(input("Enter number:"))
for i in range(0,num):
    print(" "*(i) ,end="")
    print("*"*(num-i),end="")
    print("")"""

#Pattern
"""num = int(input("Enter number:"))
for i in range(1,num+1):
    print(" "*(i-1),end="")
    print("*"*(2*num-2*i+1),end="")
    print(" "*(i-1),end="")
    print("")"""