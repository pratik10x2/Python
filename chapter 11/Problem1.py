class TwoDVector:
    def __init__(self,i,j):
        self.i = i
        self.j = j
        
    def show(self):
        print(f"The value of i {self.i} and j {self.j}")


class ThreeDVector(TwoDVector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k
    def show(self):
        print(f"The value of i {self.i} and j {self.j} and k {self.k}")


a = TwoDVector(1,2)
b = ThreeDVector(3,4,6)
a.show()
b.show()
      