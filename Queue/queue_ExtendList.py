class queue(list):
    
    def isempty(self):
        return len(self)==0
    
    def enqueue(self,item):
        self.append(item)
    
    def dequeue(self):
        if not self.isempty():
            d = self[0]
            self.pop(0)
            return d
        else:
            raise IndexError("queue underflow")
    
    def get_front(self):
        return self[0]
    
    def get_rear(self):
        return self[-1]
    
    def size(self):
        return len(self)

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