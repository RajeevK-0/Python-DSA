#employee -- empid , name, salary
class employee:
    def __init__(self,empid = None , name = None, salary = None):
        self.empid = empid  
        self.name = name
        self.salary = salary
    def setEmpid(self,empid):
        self.empid = empid
    def setName(self,name):
        self.name = name
    def setSalary(self,salary):
        self.salary = salary
    def getEmpid(self):
        return self.empid
    def getName(self):
        return self.name
    def getSalary(self):
        return self.salary

e1 = employee(1234,'rajeev',50000)
print(e1.getName())