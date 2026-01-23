class stack:
    def __init__(self,list = []):
        self.list = list
    def isEmpty(self):
        return len(self.list) == 0
    def push(self,element):
        self.list.append(element)
    def pop(self):
        self.list.remove(self.list[len(self.list)-1])
    def peek(self):
        return self.list[len(self.list)-1]
    def size(self):
        return len(self.list)
    
s = stack()
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