class deque(list):
    def isEmpty(self):
        return len(self)==0
    def insert_front(self,item):
        self.insert(0,item)
    def insert_rear(self,item):
        self.append(item)
    def del_front(self):
        if self.isEmpty():
            return IndexError("deque is empty")
        else:
            d = self[0]
            self.pop(0)
            return d
    def del_rear(self):
        if self.isEmpty():
            return IndexError("deque is empty")
        else:
            d = self[-1]
            self.pop()
            return d
    def get_front(self):
        if self.isEmpty():
            return IndexError("deque is empty")
        else:
            return self[0]
    def get_rear(self):
        if self.isEmpty():
            return IndexError("deque is empty")
        else:
            return self[-1]
    def size(self):
        return len(self)
    
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