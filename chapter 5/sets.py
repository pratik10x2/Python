# emptyset= set() #this is an empty set 
# print(type(emptyset)) 

# emptyset2 = {} # dont use emptyset2 = {} as it will create an empty dictionary

s = {1,5,32,32,4354,5,5,5,"Pratik"}
# print(s,type(s))

s.add(44)
s.remove(44)
s.discard(5)
# item= s.pop()
# print(item)
# s.clear()
# print(s,type(s))

s1 = {1,2,3,6}
s2 = {3,5,6}
s3 = s1.union(s2)
print(s1.intersection(s2))
# s1.update(s2)
# print(s1)
# print(s3)
# print(len(s1))
