class Circle:
    def __init__(self,radius=None):
        self.radius = radius
    def setRadius(self,radius):
        self.radius = radius
    def getRadius(self):
        return self.radius
    def circleArea(self):
        return 3.414*(self.radius**2)
    def circleCirumference(self):
        return 2*3.414*self.radius
c1 = Circle(5)
print(c1.getRadius())
print(c1.circleArea())
print(c1.circleCirumference())
c1.setRadius(10)
print(c1.getRadius())
print(c1.circleArea())
print(c1.circleCirumference())