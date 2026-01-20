class Node:
    def __init__(self,prev = None,item = None,next = None):
        self.prev = prev
        self.item = item
        self.next = next
class doublyLinkedList:
    def __init__(self,start = None):
        self.start = start
    def insertAtstart(self,item):
        n = Node(item=item,next=self.start)
        self.start = n
    def isEmpty(self):
        return True if self.start == None else False
    def insertAtLast(self,item):
        temp = self.start
        while temp is not None:
            if temp == None or temp.next == None:
                n = Node(item=item,next=None)
                temp.next = n
                n.prev = temp
                break
            temp = temp.next

    def insertAfter(self,temp,item):
        n = Node(item=item)
        x = self.start
        while x is not None:
            if x.item == temp.item:
                n.next = x.next
                n.prev = x
                x.next = n
            x = x.next
    
    def printDll(self):
        temp = self.start
        while temp is not None:
            print(temp.item,end=' ')
            temp = temp.next

    def search(self,aim):
        temp = self.start
        while temp is not None:
            if temp.item == aim:
                return temp
            temp = temp.next
        return None

    def delFirst(self):
        if self.start is None:
            print('DLL empty')
        else:
            temp = self.start.next
            self.start.next = None
            self.start = temp
    
    def delLast(self):
        if self.start is None:
            print('DLL empty')
        else:
            temp = self.start.next
            while temp is not None:
                if temp.next.next == None:
                    temp.next.prev = None
                    temp.next = None
                temp = temp.next
    
    def delNode(self,item):
        if self.start is not None:
            aim = self.search(item)
            temp = aim.prev
            connect = aim.next
            temp.next = connect
            connect.prev = temp

    def __iter__(self):
        temp = self.start
        while temp is not None:
            yield temp.item
            temp = temp.next

myList = doublyLinkedList()

myList.insertAtstart(20)
myList.insertAtstart(30)
print(myList.isEmpty())
myList.delLast()
myList.printDll()
print('*'*20)
for i in myList:
    print(i,end=' ')
