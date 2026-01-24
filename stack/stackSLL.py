from singlyLinkedList import SLL
class stack:
    def __init__(self):
        self.mylist = SLL()
        self.count = 0
    def isempty(self):
        return self.mylist.isEmpty()
    def push(self,item):
        self.mylist.insertAtStart(item)
        self.count += 1
    def pop(self):
        if self.mylist.start is not None:
            d = self.mylist.start.item
            self.mylist.deleteFirst()
            self.count -=1
            return d
    def peek(self):
        if not self.isempty():
            return self.mylist.start.item
    def size(self):
        return self.count
if __name__ == "__main__":
    s = stack()
    print()
    print(s.isempty())
    s.push(10)
    s.push(20)
    s.push(30)
    s.push(40)
    print(s.peek())
    print(s.size())
    s.pop()
    print(s.isempty())
    print(s.peek())
    print(s.size())
