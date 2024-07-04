#Problem number 1
'''with open("poem.txt") as f:
    content =f.read()
    
    if("twinkle" in content):
        print("The word twinkle is present in the poem.")
    else:
        print("The word twinkle is not present in the poem.")
'''

#Problem number 2
'''The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file 'Hi-score.txt' which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.'''

'''import random

def game():
    print("You are Playing a game....")
    score = random.randint(1,100)
    #read a file hiscore.txt
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
            
    print(f"Your score is:{score}") 
    if(score>hiscore):
        with open("hiscore.txt","w") as f:
            f.write(str(score))
        
    return score    
    
game()'''

#Problem number 3

'''def generate_table(n):
    table = ""
    for i in range(1,11):
        table+= f"{n} X {i} = {n*i}\n"
        
    with open(f"chapter_9_txtfile/tables/table_{n}.txt","w") as f:
        f.write(table)
      
for i in range(2,21):
    generate_table(i)'''
    
#Problem number 4 
word = "Donkey"

'''with open("newfile.txt","r") as f:
    content = f.read()
    
newcontent = content.replace(word,"######")

with open("newfile.txt","w") as f:
    f.write(newcontent)
    '''
    
#Problem number 5
'''words = ["Donkey","bad","ganda"]

with open("newfile.txt","r") as f:
    content = f.read()

for word in words:
    content = content.replace(word,"#" * len(word))
    

with open("newfile.txt","w") as f:
    f.write(content)'''
    
#Problem number 6
'''with open("log.txt","r") as f:
    content = f.read()

if("python" in content):
    print("Yes h bhai Please le jao yarr bhaut pareshan kr rakkha h.")
else:
    print("Nhi h yar kitni bar bolu nhi h nhi h nhi h.")'''

#Problem number 7
'''with open("log.txt","r") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("python" in line):
        print(f"Yes Python is presert at line number {lineno} ")
        break
    lineno+=1
else:
    print("No python is not present")'''
    
#Problem number 8
'''with open("this.txt","r") as f:
    file = f.read()

with open("this_copy.text","w") as f:
    f.write(file)
    '''
    
#Problem number 9
'''with open("file1.txt","r") as f:
    file1 = f.read()
with open("file2.txt","r") as f:
    file2 = f.read()
    
if(file1 == file2):
    print("Yes these two files are identical.")
else:
    print("No these two files are not same.")

'''
#Problem number 10  (Wipe out all content of the file)
'''with open("file1.txt","w") as f:
    f.write("")'''
    
#Problem number 11
'''with open("oold.txt" , "r") as f:
    content = f.read()

with open("oold_named_python.txt","w") as f:
    f.write(content)'''