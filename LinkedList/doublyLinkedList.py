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
        if self.start is not None:
            self.start.prev = n
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

        elif self.start.next == None:
            self.start = None
        else:
            temp = self.start.next
            while temp is not None:
                if temp.next.next == None:
                    # temp.next.prev = None
                    temp.next = None
                temp = temp.next
    
    # def delNode(self,item):
    #     if self.start is None:
    #         return
    #     else:
    #         temp = self.start
    #         while temp is not None:
    #             if temp.item == item:
    #                 if temp.next is not None:
    #                     temp.next.prev = temp.prev
    #                 if temp.prev is not None:
    #                     temp.prev.next = temp.next
    #                 else:
    #                     self.start = temp.next
    #                 break
    #             temp = temp.next
    # def delNode(self, item):
    #     if self.start is None:
    #         return  # Use return to exit immediately

    #     aim = self.search(item)
        
    #     # SAFETY CHECK: If item is not found, stop here to avoid crashes
    #     if aim is None:
    #         return 

    #     # Case 1: Deleting a Middle Node
    #     # We check if it has neighbors on BOTH sides
    #     if aim.prev is not None and aim.next is not None:
    #         n = aim.next
    #         p = aim.prev
    #         # Link previous node to next, and next node to previous
    #         n.prev = p
    #         p.next = n
                
    #     # Case 2: Deleting the Head Node
    #     elif aim.prev is None:
    #         self.start = aim.next
    #         # FIX: If there is a new head, ensure its 'prev' is None
    #         if self.start is not None:
    #             self.start.prev = None

    #     # Case 3: Deleting the Tail Node
    #     else:
    #         # We know aim.prev exists (not head) and aim.next is None (is tail)
    #         aim.prev.next = None
    
    
    def delNode(self,item):
        if self.start is None:
            pass
        else:
            aim = self.search(item)
            if aim and aim.prev is not None and aim.next is not None:
                n = aim.next
                p = aim.prev
                n.prev,p.next = p,n
            elif aim.prev == None:
                self.start = aim.next
            else:
                aim.prev.next = None
                # else:
                #     aim.prev.next = None
        # if self.start is not None:
        #     aim = self.search(item)
        #     temp = aim.prev
        #     connect = aim.next
        #     temp.next = connect
        #     connect.prev = temp

    def __iter__(self):
        temp = self.start
        while temp is not None:
            yield temp.item
            temp = temp.next

myList = doublyLinkedList()
print(myList.isEmpty())
myList.insertAtstart(40)
myList.insertAtstart(30)
myList.insertAtstart(20)
myList.insertAtstart(10)
myList.insertAtstart(2)
print(myList.isEmpty())
myList.delNode(10)
print()
# myList.delLast()
myList.printDll()
# print(myList.search(20).item)
# myList.delNode(20)
# print('*'*20)
# for i in myList:
#     print(i,end=' ')