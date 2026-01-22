class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev = prev
        self.item = item
        self.next = next
class doublyCircularLinkedList:
    def __init__(self,start=None):
        self.start = start
    def insertAtStart(self,item):
        n = Node(item=item)
        if self.start is not None:
            n.next = self.start
            n.prev = self.start.prev
            self.start.prev.next = n
            self.start.prev = n
            self.start = n
        else :
            n.prev = n
            n.next = n
            self.start = n
    def insertAtEnd(self,item):
        n = Node(item=item)
        if self.start is not None:
            n.next = self.start
            n.prev = self.start.prev
            self.start.prev.next = n
            self.start.prev = n
        else :
            n.prev = n
            n.next = n
            self.start = n

    def search(self,item):
        temp = self.start
        while temp.next != self.start:
            if temp.item == item:
                return temp
            temp = temp.next
        return temp
    def insertAfter(self,aim,target):
        n = Node(item=target)
        if self.start is not None:
            a = self.search(aim)
            if a == self.start:
                if self.start.item == aim:
                    self.insertAtStart(target)
            
            elif a == self.start.prev:
                if self.start.prev.item == aim:
                    self.insertAtEnd(target)
        
            else:
                n.next = a.next
                n.prev = a
                a.next = n
                a.next.prev = n

    def printList(self):
        temp  = self.start
        while temp.next != self.start:
            print(temp.item,end=' ')
            temp = temp.next
        print(temp.item)
mylist = doublyCircularLinkedList()
mylist.insertAtStart(1)
mylist.insertAtStart(12)
mylist.insertAtStart(3)
mylist.insertAtStart(4)
mylist.insertAtEnd(13)
mylist.insertAfter(13,5)
mylist.printList()