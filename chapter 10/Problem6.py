# Can you change the self-parameter inside a class to something else (say
# “harry”). Try changing self to “slf” or “harry” and see the effects.

import random
class Train:
    def __init__(pratik,trainNo,fromm,to):  # we replaces self parameter from  self to pratik
        pratik.trainNo = trainNo
        pratik.fromm = fromm
        pratik.to = to
        
    def bookTicket(pratik):
        print(f"Your ticket is booked in Train No. {pratik.trainNo} which is going from {pratik.fromm} to {pratik.to}")
    
    def getStatus(pratik):
        print(f"Train No. {pratik.trainNo} is running on time.")
        
    def getFare(pratik):
        print(f"The fare of Train No. {pratik.trainNo} from {pratik.fromm} to {pratik.to} is {random.randint(200,2000)}")
        
t1 = Train(1522,"Sangli","Pune")
t1.bookTicket()
t1.getStatus()
t1.getFare()

t2 = Train(1552,"Sangli","Ayodhya")
t2.bookTicket()
t2.getStatus()
t2.getFare()