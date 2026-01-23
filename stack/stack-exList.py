class stack(list):
        
    def is_empty(self):
        return len(self) == 0
    def push(self,item):
        self.append(item)
    def pop(self):
        if not self.is_empty():
            return super().pop()#overriding could happen
        else:
            raise IndexError('list is empty')
    def peek(self):
        if not self.is_empty():    
            return self[-1]
        else:
            raise IndexError('list is empty')
    def size(self):
        return len(self)
    def insert(self,index,data):
        raise AttributeError("No attribute 'insert' in stack")

s = stack()
s.push(10)
s.push(20)
s.push(30)
print(s.peek())
s.pop()
print(s.peek())
print(s.size())