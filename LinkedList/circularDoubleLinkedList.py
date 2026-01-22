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
            n.next = self.start.prev.next
            n.prev = self.start.prev
            self.start.prev.next = n
            self.start.prev = n
            self.start = n
        else :
            n.prev = n
            n.next = n
            self.start = n
    