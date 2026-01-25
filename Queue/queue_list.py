class queue:
    def __init__(self,front=None,rear=None):
        self.queue = []
    def isempty(self):
        return len(self.queue) == 0
    def enqueue(self,item):    
        self.queue.append(item)
    def dequeue(self):
        if not self.isempty():
            d = self.queue[0]
            self.queue.remove(self.queue[0])
            return d
        else:
            raise IndexError("queue underflow")
    def get_front(self):
        if not self.isempty():
            return self.queue[0]
        else:
            raise IndexError("queue underflow")
    def get_rear(self):
        if not self.isempty():    
            return self.queue[-1]
        else:
            raise IndexError("queue underflow")
    def size(self):
        return len(self.queue)

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