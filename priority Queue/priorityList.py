class priorityQueue:
    def __init__(self):
        self.list = []
        self.priority = []
    def push(self,item,priority):
        i = 0
        while i<len(self.list) and self.list[i][1]<=priority:
            i +=1
        self.list.insert(i,(item,priority))
    def isEmpty(self):
        return len(self.list) == 0
    def pop(self):
        if self.isEmpty():
            raise IndexError("priority Queue is empty")
        return self.list.pop(0)[0]
    def size(self):
        return len(self.list)
if __name__ == "__main__":
    pr = priorityQueue()
    pr.push("rajeev",0)
    pr.push("xyz",1)
    pr.push("zxc",1)
    print(pr.size())
    print("*"*30)
    print(pr.pop())
    print(pr.size())