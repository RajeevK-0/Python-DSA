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
            if temp.item == aim:
                return temp
            return None
        
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
        if self.last is not None:
            temp = self.last.next
            while temp != self.last:
                print(temp.item,end=' ')
                temp = temp.next
            print(self.last.item,end=' ')

    def delFirst(self):
        if self.last is not None:
            if self.last.next == self.last:
                self.last = None
            else:
                t = self.last
                t.next = t.next.next

    def delLast(self):
        if self.last is not None:
            if self.last.next == self.last:
                self.last = None
            else:
                temp = self.last.next
                while temp.next != self.last:
                    temp = temp.next
                temp.next = temp.next.next
                self.last = temp
    
    def delItem(self, item):
        if self.last is not None:
            if self.last.item == item:
                self.delLast()
            elif self.last.next.item== item:
                self.delFirst()
            else:
                temp = self.last.next
                while temp != self.last:
                    if temp.next == self.last:
                        if temp.next.item == item:
                            self.delLast()
                        break
                    if temp.next.item == item:
                        temp.next = temp.next.next
                        break
                    temp = temp.next
                
    def __iter__(self):
        t = self.last
        while t.next != self.last:
            yield t.next.item
            t = t.next
        yield self.last.item

mylist = circularLinkedlist()
mylist.insertAtStart(5)
mylist.insertAtStart(1)
mylist.insertAtStart(9)
mylist.insertAtStart(10)
mylist.insertAtLast(6)
mylist.printCll()
print()
print(mylist.search(6))
mylist.delItem(6)#last
mylist.printCll()