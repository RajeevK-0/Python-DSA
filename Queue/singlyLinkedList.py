class Node:
    def __init__(self,item = None,next = None):
        self.item = item
        self.next = next
class SLL:
    def __init__(self,start = None):
        self.start = start
        
    def isEmpty(self):
        return True if self.start == None else False
    def insertAtStart(self,item):
        n = Node(item,self.start)
        self.start = n
        # temp = self.start()
        # self.start() = item.item()
        # item.next() = temp
    def insertAtLast(self,itemAtlast):
        n = Node(itemAtlast,None)
        if not self.isEmpty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
        else:
            self.start = n
        # if self.next == None:
        #     self.next() = itemAtlast.item()
        # itemAtlast.next() = None
    def search(self,item):
        temp = self.start
        while temp is not None:
            if temp.item == item:
                return temp
            temp = temp.next
        return None
        # while self.next != None:
        #     count = 0
        #     if self.item == item.item:
        #         break
        #     count+=1
        #     return count+1
    def insertAfter(self,node,item):
        if node is not None:
            n = Node(item,node.next)
            node.next = n
        # temp = node.next() 
        # self.node.next() = item.item()
        # item.next() = temp

    def printSSL(self):
        temp = self.start
        while temp is not None:
            print(temp.item,end=' ')
            temp = temp.next
    def deleteFirst(self):
        if self.start is not None:
            temp = self.start
            self.start  = temp.next
            return temp.item
    def deleteLast(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None
    def deleteItem(self,element):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item == element:
                self.start = None
        else:
            temp = self.start
            while temp.next is not None:
                if temp.next.item == element:
                    temp.next = temp.next.next
                    break
                temp = temp.next
        # temp = self.element.next()
        # while self.next() == None:
        #     if self.next() == element.item():
        #         return self.next()
        # self.next() ==  temp
    def __iter__(self):
        start = self.start
        while start is not None:
            yield start.item
            start = start.next
#     def __iter__(self):
#         return sllItrator(self.start)
# class sllItrator:
#     def __init__(self,start):
#         self.current = start
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if not self.current:
#             raise StopIteration
#         data = self.current.item
#         self.current = self.current.next
#         return data
if __name__ == "__main__":    
    myList = SLL()
    myList.insertAtStart(10)
    myList.insertAtStart(20)
    myList.insertAtStart(30)
    myList.insertAtLast(50)
    myList.insertAfter(myList.search(10),60)
    myList.printSSL()
    print()
    print('*'*10)
    for i in myList:
        print(i,end=' ')