from collections import deque
class graph:
    def __init__(self,vco =0):
        self.vertexCount=vco
        self.adjList = {i:[]*vco for i in range(vco)}
    def addEdge(self,u,v,weight = 1):
        if 0<=u<self.vertexCount and 0<=v<self.vertexCount:
            self.adjList[u].append((v,weight))
            self.adjList[v].append((u,weight))
        else:
            raise IndexError("not in dict")
    def removeEdge(self,u,v):
        if 0<=u<self.vertexCount and 0<=v<self.vertexCount:
            self.adjList[u] = [(ver,weight) for ver,weight in self.adjList[u] if ver!=v]
            self.adjList[v] = [(ver,weight) for ver,weight in self.adjList[v] if ver!=u]
        else:
            raise IndexError("not in dict")
    def hasEdge(self,u,v):
        if 0<=u<self.vertexCount and 0<=v<self.vertexCount:
            return any(vertex == v for vertex, x in self.adjList[u])
        else:
            raise IndexError("not in dict")
    def printAdjList(self):
        for i,n in self.adjList.items():
            print("v",i,":",n)
    def bfs(self,s):
        dq = deque()
        dq.append(s)
        v = [False]*self.vertexCount
        v[s] = True
        res = []
        while dq:
            temp = dq.popleft()
            res.append(temp)
            for u,w in self.adjList[temp]:
                if v[u] == False:
                    dq.append(u)
                    v[u] = True
        return res
    def dfs(self,s):
        st = [s]
        res = []
        v = [False]*self.vertexCount
        v[s] = True
        while st:
            temp = st.pop()
            res.append(temp)
            for u,w in self.adjList[temp]:
                if v[u] == False:
                    st.append(u)
                    v[u] = True
        return res
if __name__ == "__main__":
    g1 = graph(vco=5)
    g1.addEdge(0,0,10)
    g1.addEdge(0,1,10)
    g1.addEdge(1,2,10)
    g1.addEdge(2,3,10)
    g1.addEdge(1,1,20)
    g1.addEdge(2,2,30)
    g1.addEdge(3,3,40)
    g1.addEdge(4,4,50)
    print(g1.hasEdge(2,2))
    g1.printAdjList()
    # g1.removeEdge(2,2)
    # print(g1.hasEdge(2,2))
    # print("*"*30)
    # g1.printAdjList()
    print("*"*30)
    print(g1.bfs(0))
    print(g1.dfs(0))