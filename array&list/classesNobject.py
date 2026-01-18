class person:
    def __init__(self,name = None,age = None):
        self.name = name
        self.age = age
    def show(self):
        print(f'Name : {self.name}, Age : {self.age}')
p1 = person('raj',23)
p1.show()