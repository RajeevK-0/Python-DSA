class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev = prev
        self.item = item
        self.next = next
class doublyCircularLinkedList:
    def __init__(self,start=None):
        self.start = start
    
    def isEmpty(self):
        return self.start == None
    
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

    def delFirst(self):
        if self.start is not None:
            if self.start.next == self.start:
                self.start = None
            else:
                t = self.start.item
                self.start.next.prev = self.start.prev
                self.start.prev.next = self.start.next
                self.start = self.start.next
                return t
    def delLast(self):
        if self.start is not None:
            if self.start == self.start.next:
                self.start = None
            else:
                t = self.start.prev.item
                self.start.prev.prev.next = self.start
                self.start.prev = self.start.prev.prev
                return t
    def delNode(self,item):
        if self.start is not None:
            if self.start.next == self.start:
                if self.start.item == item:
                    self.start == None
            elif self.start.item == item:
                self.delFirst()
            elif self.start.prev.item == item:
                self.delLast()
            else:
                a = self.search(item)
                if a:
                    a.prev.next = a.next
                    a.next.prev = a.prev
    
    def __iter__(self):
        if self.start is not None:
            temp = self.start
            while temp.next != self.start:
                yield temp.item
                temp = temp.next
            yield temp.item 
if __name__ == "__main__":    
    mylist = doublyCircularLinkedList()
    mylist.insertAtStart(1)
    mylist.insertAtStart(12)
    mylist.insertAtStart(3)
    mylist.insertAtStart(4)
    mylist.insertAtEnd(13)
    mylist.insertAfter(13,5)
    # mylist.delFirst()
    # mylist.delLast()
    mylist.delNode(1)
    mylist.printList()
    print('*'*30)
    for x in mylist:
        print(x,end=' ')