class rectangle:
    def __init__(self,length=None,breadth = None):
        self.length = length
        self.breadth = breadth
    def setDim(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def getdim(self):
        return self.length , self.breadth
    def recArea(self):
        return self.length*self.breadth
    def circumference(self):
        return 2*(self.length+self.breadth)
    
r1 = rectangle(10,10)
print(r1.getdim())
print(r1.circumference())
print(r1.recArea())

r1.setDim(4,5)
print(r1.getdim())
print(r1.circumference())
print(r1.recArea())
