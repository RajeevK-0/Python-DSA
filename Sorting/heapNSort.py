class heap:
    def __init__(self):
        self.heap = []

    def createHeap(self,list):
        for i in list:
            self.insert(i)
        return self.heap
    
    def insert(self,e):#percolate up
        index = len(self.heap)
        parent = (index-1)//2
        while index >0 and self.heap[parent]<e:
            if index == len(self.heap):
                self.heap.append(self.heap[parent])
            else:
                self.heap[index] = self.heap[parent]
            index = parent
            parent = (index-1) // 2
        if index == len(self.heap):
            self.heap.append(e)
        else:
            self.heap[index] = e

    def top(self):
        if len(self.heap) == 0:
            raise EmptyHeapException
        return self.heap[0]

    def delete(self):#percolate down
        if len(self.heap) == 0:
            raise EmptyHeapException
        if len(self.heap) == 1:
            return self.heap.pop()
        index = 0
        c1 = 2*index+1
        c2 = 2*index+2
        maxVal = self.heap[0]
        a = self.heap.pop()
        while len(self.heap) > c1:
            if c2 < len(self.heap):
                if self.heap[c1] > self.heap[c2]:
                    if self.heap[c1] > a:
                        self.heap[index] = self.heap[c1]
                        index = c1
                    else:
                        break
                else:
                    if self.heap[c2]>a:
                        self.heap[index] = self.heap[c2]
                        index = c2
                    else:
                        break
            else:
                if self.heap[c1] > a:
                    self.heap[index] = self.heap[c1]
                    index = c1
                else :
                    break
            c1 = 2*index+1
            c2 = 2*index+2
        self.heap[index] = a    
        return maxVal
    
    def heapSort(self,list1):
        self.heap = []
        self.createHeap(list1)
        l2 = []
        while len(self.heap) >0:
            l2.append(self.delete())
        return l2[::-1]
        # try:
        #     while True:
        #         l2.append(self.delete())
        # except EmptyHeapException:
        #     pass
        # return l2
        
class EmptyHeapException(Exception):
    def __init__(self,msg = "Heap is Empty"):
        self.msg = msg
    def __str__(self):
        return self.msg

if __name__ == "__main__":
    list1 = [35,56,12,78,43,25,10,80,60]
    h = heap()
    list1 = h.heapSort(list1)
    print(list1)
    