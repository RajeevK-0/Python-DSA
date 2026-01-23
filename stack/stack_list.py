class stack:
    def __init__(self,list = []):
        self.list = list
    def isEmpty(self):
        return len(self.list) == 0
    def push(self,element):
        self.list.append(element)
    def pop(self):
        if not self.isEmpty():
            self.list.pop()
        else:
            raise IndexError('list is empty')
    def peek(self):
        if not self.isEmpty():    
            return self.list[-1]
        else:
            raise IndexError('list is empty')
    def size(self):
        return len(self.list)
    
s = stack()
# s.peek()
# s.pop()
print(s.isEmpty())
s.push(10)
s.push(1)
s.push(2)
print(s.peek())
print(s.size())
s.pop()
print(s.peek())
print(s.size())
print(s.isEmpty())