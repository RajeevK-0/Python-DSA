class graph:
    def __init__(self,vertexCount = 0):
        self.vertexCount = vertexCount
        self.adjMatrix = [[0]*vertexCount for i in range(vertexCount)]
    def addEdge(self,u,v,weight = 1):
        if 0<=u<self.vertexCount and 0<=v<self.vertexCount:
            self.adjMatrix[u][v] = weight
            self.adjMatrix[v][u] = weight
        else:
            raise IndexError("out of range")
    def removeEdge(self,u,v):
        if 0<=u<self.vertexCount and 0<=v<self.vertexCount:
            self.adjMatrix[u][v] = 0
            self.adjMatrix[v][u] = 0
        else:
            raise IndexError("out of range")
    def hasEdge(self,u,v):
        if 0<=u<self.vertexCount and 0<=v<self.vertexCount:
            return self.adjMatrix[u][v] != 0
        else:
            raise IndexError("out of range")
    def printAdjMatrix(self):
        for i in self.adjMatrix:
            print(' '.join(map(str,i)))
            # for j in range(self.vertexCount):
            #     print(self.adjMatrix[i][j],end=' ')
            # print()
if __name__ == "__main__":
    g1 = graph(vertexCount=5)
    g1.addEdge(0,0,10)
    g1.addEdge(1,1,20)
    g1.addEdge(2,2,30)
    g1.addEdge(3,3,40)
    g1.addEdge(4,4,50)
    g1.printAdjMatrix()
    g1.removeEdge(2,2)
    print("*"*30)
    g1.printAdjMatrix()