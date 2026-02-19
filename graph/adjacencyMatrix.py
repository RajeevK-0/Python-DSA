class graph:
    def __init__(self,vertexCount = 0):
        self.vertexCount = vertexCount
        self.adjMatrix = [[0]*vertexCount for i in range(vertexCount)]
    def addEdge(self,u,v,weight = 1):
        self.adjMatrix[u][v] = weight
    def removeEdge(self,u,v):
        self.adjMatrix[u][v] = 0
    def hasEdge(self,u,v):
        return self.adjMatrix[u][v] != 0
    def printAdjMatrix(self):
        for i in range(self.vertexCount):
            for j in range(self.vertexCount):
                print(self.adjMatrix[i][j],end=' ')
            print()
if __name__ == "__main__":
    g1 = graph(vertexCount=5)
    g1.addEdge(0,0,10)
    g1.addEdge(1,1,20)
    g1.addEdge(2,2,20)
    g1.addEdge(3,3,30)
    g1.addEdge(4,4,40)
    
    