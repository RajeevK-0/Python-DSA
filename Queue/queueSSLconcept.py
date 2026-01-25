class Node:
    def __init__(self,item = None,next=None):
        self.item = item
        self.next = next
class queue:
    
    def __init__(self):
        self.count = 0
        self.front = None
        self.rear = None
    
    def isEmpty(self):
        return self.front == None #or self.rear == None,self.count = NOne
    
    def enqueue(self,item):
        n = Node(item = item,next=None)
        if not self.isEmpty():
            self.rear.next = n
            self.rear = n
        else:
            self.front = n
            self.rear = n
        self.count += 1
            
    def dequeue(self):
        if not self.isEmpty():
            d = self.front.item
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            self.count -= 1
            return d
        else:
            raise IndexError("Queue underflow")
    
    def get_rear(self):
        if not self.rear == None:
            return self.rear.item
        else:
            raise IndexError("Queue underflow")
    
    def get_front(self):
        if not self.front == None:
            return self.front.item
        else:
            raise IndexError("Queue underflow")
    
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