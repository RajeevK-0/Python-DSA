from circularDoubleLinkedList import *
class deque(doublyCircularLinkedList):
    def __init__(self, start=None):
        super().__init__(start)
        self.count = 0
        self.rear = None
    def isEmpty(self):
        return super().isEmpty()
    def insert_front(self,item):
        self.insertAtStart(item=item)
        self.count += 1
    def insert_rear(self,item):
        self.insertAtEnd(item=item)
        self.count += 1
    def del_front(self):
        d = self.delFirst()
        self.count-=1
        return d
    def del_rear(self):
        d = self.delLast()
        self.count-=1
        return d
    def get_front(self):
        return self.start.item
    def get_rear(self):
        return self.start.prev.item
    def size(self):
        return self.count
if __name__ == "__main__":
    dq= deque()
    dq.insert_front(10)
    dq.insert_front(20)
    dq.insert_rear(10)
    dq.insert_rear(40)
    print(dq.get_front())
    print(dq.get_rear())
    print(dq.size())
    print("*"*30)
    print(dq.del_front())
    print(dq.del_rear())
    print(dq.get_front())
    print(dq.get_rear())
    print(dq.size())