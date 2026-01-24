class Node:
    def __init__(self,item = None,next = None):
        self.item = item
        self.next = next
class stack:
    def __init__(self,start = None):
        self.start = start
        self.count = 0
    def isempty(self):
        return self.count == 0
    
    def push(self,item):
        n = Node(item=item,next=self.start)
        self.start = n
        self.count += 1
        # if not self.isempty():
        #     n.next = self.start
        #     self.start = n
        #     self.count +=1
        # else:
        #     self.start = n
    
    def pop(self):
        if not self.isempty():
            data = self.start.item
            self.start = self.start.next
            self.count -=1
            return data
        else:
            raise IndexError('stack is empty')
    
    def peek(self):
        if not self.isempty():
            return self.start.item
        else:
            raise IndexError('stack is empty')
    
    def size(self):
        return self.count
if __name__ == "__main__":
    s = stack()
    s.push(10)
    s.push(20)
    s.push(30)
    s.push(40)
    print(s.peek())
    print(s.size())
    s.pop()
    print(s.peek())
    print(s.size())
