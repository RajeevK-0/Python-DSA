class Node:
    def __init__(self,val = None,next = None,prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0
    def isEmpty(self):
        return self.count == 0
    def insert_front(self,item):
        n = Node(val=item)
        if self.isEmpty():
            self.front = n
            self.rear = n
        else:
            n.next = self.front 
            self.front.prev = n
            self.front = n
        self.count+=1
    def insert_rear(self,item):
        if self.isEmpty():
            self.front = Node(val=item)
            self.rear = Node(val=item)
        else:
            t = self.rear
            self.rear = Node(val=item,next=self.front,prev=t)
        self.count+=1
    def del_front(self):
        if self.isEmpty():
            raise IndexError("deque is empty")
        else:
            d = self.front.val
            self.front.next.prev = self.rear
            self.rear.next = self.front.next
            self.front = self.front.next
            self.count -=1
            return d
    def del_rear(self):
        if self.isEmpty():
            raise IndexError("deque is empty")
        else:
            d = self.rear.val
            self.rear.prev.next = self.front
            self.front.prev = self.rear.prev
            self.rear = self.rear.prev
            self.count-=1
            return d
    def get_front(self):
        if self.isEmpty():
            raise IndexError("deque is empty")
        else:
            return self.front.val
    def get_rear(self):
        if self.isEmpty():
            raise IndexError("deque is empty")
        else:
            return self.rear.val
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