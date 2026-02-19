class graph:
    def __init__(self,vco =0):
        self.vertexCount=vco
        self.adjList = {i:[0]*vco for i in range(vco)}
    def addEdge(self,u,v,weight = 1):
        if 0<=u<self.vertexCount and 0<=v<self.vertexCount:
            self.adjList[u][v] = weight
            self.adjList[v][u] = weight
        else:
            raise IndexError("not in dict")
    def removeEdge(self,u,v):
        if 0<=u<self.vertexCount and 0<=v<self.vertexCount:
            self.adjList[u][v] = 0
            self.adjList[v][u] = 0
        else:
            raise IndexError("not in dict")
    def hasEdge(self,u,v):
        if 0<=u<self.vertexCount and 0<=v<self.vertexCount:
            return self.adjList[u][v] != 0
        else:
            raise IndexError("not in dict")
    def printAdjList(self):
        for i in self.adjList:
            print('v',i,":",self.adjList[i])
if __name__ == "__main__":
    g1 = graph(vco=5)
    g1.addEdge(0,0,10)
    g1.addEdge(1,1,20)
    g1.addEdge(2,2,30)
    g1.addEdge(3,3,40)
    g1.addEdge(4,4,50)
    print(g1.hasEdge(2,2))
    g1.printAdjList()
    g1.removeEdge(2,2)
    print(g1.hasEdge(2,2))
    print("*"*30)
    g1.printAdjList()