class Node:
    def __init__(self,item = None,next = None):
        self.item = item
        self.next = next

class circularLinkedlist:
    def __init__(self,last = None):
        self.last = last
    
    def isEmpty(self):
        return self.last == None
    
    def insertAtStart(self,item):
        n= Node(item=item)
        if self.last is not None:
            t = self.last.next
            self.last.next = n
            n.next = t
        else:
            self.last = n
            n.next = n
    
    def insertAtLast(self,item):
        t= self.last.next
        n= Node(item=item)
        self.last.next = n
        n.next = t
        self.last = n
    
    def search(self,aim):
        temp = self.last.next
        while temp != self.last:
            if temp.item == aim:
                return temp
            temp = temp.next
    
    def printCll(self):
        while self.last.next != self.last:
            print(self.last.next.item,end=' ')
            self.last.next = self.last.next.next
        print(self.last.item,end=' ')
mylist = circularLinkedlist()
mylist.insertAtStart(5)
mylist.insertAtStart(1)
mylist.insertAtStart(9)
mylist.insertAtStart(10)
mylist.insertAtLast(6)
mylist.printCll()
print(mylist.search(6))