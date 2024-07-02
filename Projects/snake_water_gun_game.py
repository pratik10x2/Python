'''
snake = 1
water = -1
gun = 0

'''
import random
computer  = random.choice([-1,0,1])
youStr = input("Enter your Choice:")
youDict = {"s":1,"w":-1,"g":0}
reverseDict = {1:"Snake" , -1:"Water" , 0:"Gun"}

you = youDict[youStr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}.")

if(computer == you):
    print("Draw")
else:
    if(computer == 1 and you == -1):
        print("Awwww, You Lose bro")
    elif(computer == 1 and you == 0):
        print("Yeahh, You win bother,hoorreeyy!")
    elif(computer == -1 and you == 1):
        print("Yeahh, You win bother,hoorreeyy!")
    elif(computer == -1 and you == 0):
        print("Awwww, You Lose bro")
    elif(computer == 0 and you == 1):
        print("Awwww, You Lose bro")
    elif(computer == 0 and you == -1):
        print("Yeahh, You win bother,hoorreeyy!")
    else:
        print("Something went wrong,Please Enter valid input.")
    