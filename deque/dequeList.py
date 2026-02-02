class deque:
    def __init__(self):
        self.list= []
    def isEmpty(self):
        return len(self.list) == 0
    def insert_front(self,item):
        self.list.insert(0,item)
    def insert_rear(self,item):
        self.list.append(item)
    def del_front(self):
        if not self.isEmpty():
            d = self.list[0]  
            self.list.remove(self.list[0]) 
            return d
        else:
            raise IndexError("deque is empty")
    def del_rear(self):
        if not self.isEmpty():
            d = self.list[-1]
            self.list.remove(self.list[-1]) #or self.list.pop()
            return d
        else:
            raise IndexError("deque is empty")
    def get_front(self):
        if not self.isEmpty():
            return self.list[0]
        else:
            raise IndexError("deque is empty")
    def get_rear(self):
        if not self.isEmpty():
            return self.list[-1]
        else:
            raise IndexError("deque is empty")
    def size(self):
        return len(self.list)
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