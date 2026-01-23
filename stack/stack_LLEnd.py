class Node:
    def __init__(self,item = None,next = None):
        self.item = item
        self.next = next
class stack:
    def __init__(self,start=None,count = 0):
        self.start = start
        self.count = count
    def isEmpty(self):
        return self.count == 0
    def push(self,item):
        n=Node(item=item)
        if self.count != 0:
            temp = self.start
            while temp is not None:
                if temp.next == None:
                    temp.next = n
                    n.next = None
                    break
                temp = temp.next
            self.count+=1
        else:
            self.start = n
            n.next = None
            self.count+=1
    def pop(self):
        if self.count != 0:
            if self.start.next == None:
                self.start = None
                self.count-=1
            else:    
                temp = self.start
                while temp is not None:
                    if temp.next.next == None:
                        temp.next = None
                        self.count -=1
                        break
                    temp = temp.next
        else:
            raise IndexError('Stack is empty')
    def peek(self):
        if self.count != 0:
            temp = self.start
            while temp is not None:
                if temp.next == None:
                    return temp.item
                temp = temp.next
        else:
            raise IndexError('stack is empty')
    def size(self):
        return self.count
    
s = stack()
s.push(10)
s.push(20)
s.push(30)
print(s.size())
print(s.peek())
s.pop()
print(s.size())
print(s.peek())