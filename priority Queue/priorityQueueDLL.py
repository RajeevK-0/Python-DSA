class Node:
    def __init__(self,item = None,priority = None,next = None):
        self.item = item
        self.priority = priority
        self.next = next
class priorityQueue:
    def __init__(self):
        self.start = None
        self.count = 0
    def isEmpty(self):
        return self.start == None
    def push(self,item,priority):
        n = Node(item=item,priority=priority)
        if self.isEmpty() or priority <  self.start.priority:
            self.start = n
            n.next = None
            self.count +=1
        else:
            temp = self.start
            while temp.next and temp.next.priority<=priority:
                # if temp.next == None:
                #     temp.next = n
                #     n.next = None
                # elif temp.next.priority <= n.priority:
                #     n.next = temp.next
                #     temp.next = n
                temp = temp.next
            n.next = temp.next
            temp.next = n
            self.count+=1
    def pop(self):
        if self.isEmpty():
            raise IndexError("priority queue is empty")
        else:
            d = self.start.item
            self.start = self.start.next
            self.count -= 1
            return d
    def size(self):
        return self.count
if __name__ == "__main__":
    pr = priorityQueue()
    pr.push("rajeev",0)
    pr.push("xyz",1)
    pr.push("zxc",2)
    print(pr.size())
    print("*"*30)
    print(pr.pop())
    print(pr.size())