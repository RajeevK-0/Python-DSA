from abc import ABC,abstractmethod
class person:
    #dunder
    def __init__(self,name = 'xyz',age = 22):
        self.name = name
        self.age = age
    def greet(self,name = 'xyz'):
        print(f"hello {name}, how was your day ")
    def prin(self):
        print(self.name*4)
'''pr inherit person class
    OOPs-inheritance'''
class pr(person):
    pass #placholder for future code
prs = pr()
prs.greet()


# p = person()
# p.greet()
# p.prin()