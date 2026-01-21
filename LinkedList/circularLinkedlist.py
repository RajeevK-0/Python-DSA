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
        if self.last is not None:
            t= self.last.next
            n= Node(item=item)
            self.last.next = n
            n.next = t
            self.last = n
        else:
            self.last = n
            n.next = n   
    
    def search(self,aim):
        if self.last is not None:
            temp = self.last.next
            while temp != self.last:
                if temp.item == aim:
                    return temp
                temp = temp.next
        
    def insertAfter(self,target,aim):
        n = Node(item=aim)
        if self.last is not None:
            a = self.search(target)
            if a != self.last:
                temp = a.next
                a.next = n
                n.next = temp
            else:
                temp = a.next
                a.next = n
                n.next = temp
                self.last = n
    
    def printCll(self):
        while self.last.next != self.last:
            print(self.last.next.item,end=' ')
            self.last.next = self.last.next.next
        print(self.last.item,end=' ')

    def __iter__(self):
        t = self.last
        while t.next != t:
            yield t.next
            t = t.next

mylist = circularLinkedlist()
mylist.insertAtStart(5)
mylist.insertAtStart(1)
mylist.insertAtStart(9)
mylist.insertAtStart(10)
mylist.insertAtLast(6)
mylist.printCll()
print(mylist.search(6))
