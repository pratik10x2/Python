# read the file
'''f = open("myfile.txt")
data = f.read()
print(data)
f.close()
'''

#write the file
'''st ="Hey Harry you are amazing"

f = open("myfile.txt","w")

f.write(st)

f.close'''

#readlines
'''f = open("myfile.txt")
lines = f.readlines()
print(lines,type(lines))
f.close()
'''

#readline (read single line)
'''f= open("myfile.txt")
line = f.readline()

while(line != ""):
    print(line)
    line = f.readline()
    
f.close'''

#Appending 
'''st = "Hi my name is pratik"
f = open("myfile.txt","a")
f.write(st)
f.close()'''

# + for updating
'''st = "Hi my name is nicholes"
f = open("myfile.txt","+a")
f.write(st)
f.close()
'''

#using with statement 
'''with open("myfile.txt") as f:
    print(f.read())'''
    
'''st = "hello ji kaise h saree"
with open("myfile.txt","w") as f:
    f.write(st)
    '''