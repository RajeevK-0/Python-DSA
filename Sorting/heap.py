class heap:
    def __init__(self,hlist = []):
        self.hlist = hlist if hlist is not None else []
    def createHeap(self,list):
        for i in list:
            self.insert(i)
    def insert(self,ele):
        index = len(self.hlist)
        parentIndex = (index-1)//2
        while index > 0 and self.hlist[parentIndex]<ele:
            if index == len(self.hlist):
                self.hlist.append(self.hlist[parentIndex])
            else:
                self.hlist[index] = self.hlist[parentIndex]
            index = parentIndex
            parentIndex = (index-1)//2  
        if index == len(self.hlist):
            self.hlist.append(ele)
        else:
            self.hlist[index] = ele
    def topElement(self):
        if len(self.hlist) == 0:
            raise EmptyHeapException()
        return self.hlist[0]
    
    def deletion(self):
        if len(self.hlist) == 0:
            raise EmptyHeapException()
        maxVal= self.hlist[0]
        temp = self.hlist.pop()
        if len(self.hlist) == 0:
            return maxVal
        index = 0
        child1 = 2*index+1
        child2 = 2*index+2
        while child1 < len(self.hlist):
            if child2<len(self.hlist):
                if self.hlist[child1]>self.hlist[child2]:
                    if self.hlist[child1]>temp:
                        self.hlist[index] = self.hlist[child1]
                        index = child1
                    else:
                        break
                else:
                    if self.hlist[child2]>temp:
                        self.hlist[index] = self.hlist[child2]
                        index = child2
                    else:
                        break
            else:
                if self.hlist[child1]>temp:
                    self.hlist[index] = self.hlist[child1]
                    index = child1
                else:
                    break
            child1 = 2*index+1
            child2 = 2*index+2
        self.hlist[index] = temp
        return maxVal
    
    def heapSort(self,list1):
        self.createHeap(list1)
        list2 = []
        try:
            while True:
                list2.insert(0,self.deletion())
        except EmptyHeapException:
            pass
        return list2
class EmptyHeapException(Exception):
    def __init__(self,msg = "heap is empty"):
        self.msg = msg
    def __str__(self):
        return self.msg
if __name__ == "__main__":
    list1 = [35,56,12,78,43,25,10,80,60]
    h = heap()
    list1 = h.heapSort(list1)
    print(list1)    
        # while index < len(self.hlist) and :
        #     if self.hlist[child1] > self.hlist[child2]:
        #         if self.hlist[child1] < e:
        #             self.hlist[index] = e
        #         self.hlist[index] = self.hlist[child1]
        #     else:
        #         if self.hlist[child2] < e:
        #             self.hlist[index] = e
        #         self.hlist[index] = self.hlist[child2]
            
        # for i in range(len(self.hlist)):
        #     if self.hlist[i] > ele:
        #         if self.hlist[2*i+1] is None:
        #             self.hlist[2*i+1] = ele
        #         if self.hlist[2*i+2] is None:
        #             self.hlist[2*i+2] = ele
        #     else:
        #         temp = self.hlist[i]
        #         self.hlist[i] = ele
        #         if self.hlist[2*i+1] is None:
        #             self.hlist[2*i+1] = temp
        #         if self.hlist[2*i+2] is None:
        #             self.hlist[2*i+2] = temp
                