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
#Encapsulation.....
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner       # Public
        self.__balance = balance # Private (note the double underscore)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Added Rs.{amount}")

    def get_balance(self):
        # We provide a controlled way to read the private data
        return self.__balance

account = BankAccount("Raj", 1000)
account.deposit(500)

# print(account.__balance) # This would raise an AttributeError
print(account.get_balance()) # Output: 1500
print(account.owner)
###Inheritance
# Parent Class
class Animal:
    def speak(self):
        print("Animal makes a sound")

# Child Class inherits from Animal
class Cat(Animal):
    def speak(self):
        print("Meow")

# Child Class inherits from Animal
class Dog(Animal):
    def speak(self):
        print("Woof")
my_cat = Cat()
my_cat.speak() # Output: Meow (overrides parent method)

