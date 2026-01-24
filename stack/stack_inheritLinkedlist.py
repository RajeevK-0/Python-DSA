from singlyLinkedList import *
class stack(SLL):
    def __init__(self):
        super().__init__()
        self.count = 0
    def isempty(self):
        return self.isEmpty()
    def push(self,item): 
        self.insertAtStart(item)
        self.count+=1    
    def pop(self):
        if not self.isEmpty():
            d = self.start.item
            self.deleteFirst()
            self.count-=1
        else:
            raise IndexError("stack underflow")
    def peek(self):
        if not self.isEmpty():
            return self.start.item
        else:
            raise IndexError("stack underflow")
    def size(self):
        return self.count
    
if __name__ == "__main__":
    s = stack()
    s.push(1)
    s.push(2)
    s.push(33)
    s.push(44)
    print(s.peek())
    print(s.size())
    s.pop()
    print(s.peek())
    print(s.size())
