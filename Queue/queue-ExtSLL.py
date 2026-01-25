from singlyLinkedList import *
class queue(SLL):
    def __init__(self, start=None):
        super().__init__(start)
        self.count = 0
        self.rear = None
    def isempty(self):
        return self.isEmpty()
    def enqueue(self,item):
        self.insertAtLast(item)
        self.rear = self.search(item).item
        self.count +=1
    def dequeue(self):
        self.count -= 1
        x = self.deleteFirst()
        return x
    def get_front(self):
        return self.start.item
    def get_rear(self):
        return self.rear
    def size(self):
        return self.count
if __name__ == "__main__":
    q = queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    print(q.get_front())
    print(q.get_rear())
    print(q.size())
    print(q.dequeue())
    print(q.get_front())
    print(q.get_rear())
    print(q.size())