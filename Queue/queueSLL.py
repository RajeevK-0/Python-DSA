from singlyLinkedList import SLL
class queue:
    def __init__(self):
        self.queue = SLL()
        self.front = None
        self.rear = None
        self.count = 0
    def isempty(self):
        return self.queue.isEmpty()
    def enqueue(self,item):
        self.queue.insertAtLast(item)
        self.rear = self.queue.search(item).item
        self.count += 1
    def dequeue(self):
        if not self.queue.isEmpty():
            self.count -= 1
            x = self.queue.deleteFirst()
            return x
        else:
            raise IndexError("queue is empty")
    def get_front(self):
        self.front = self.queue.start.item
        return self.front
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