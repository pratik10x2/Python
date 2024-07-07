import random
class Train:
    def __init__(self,trainNo,fromm,to):
        self.trainNo = trainNo
        self.fromm = fromm
        self.to = to
        
    def bookTicket(self):
        print(f"Your ticket is booked in Train No. {self.trainNo} which is going from {self.fromm} to {self.to}")
    
    def getStatus(self):
        print(f"Train No. {self.trainNo} is running on time.")
        
    def getFare(self):
        print(f"The fare of Train No. {self.trainNo} from {self.fromm} to {self.to} is {random.randint(200,2000)}")
        
t1 = Train(1522,"Sangli","Pune")
t1.bookTicket()
t1.getStatus()
t1.getFare()

t2 = Train(1552,"Sangli","Ayodhya")
t2.bookTicket()
t2.getStatus()
t2.getFare()