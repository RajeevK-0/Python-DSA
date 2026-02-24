class Solution:
    def dfs(self,visit,d,node):
        visit.add(node)
        for i in d[node]:
            if i not in visit:
                visit.add(i)
                self.dfs(visit,d,i)
            
        # for i in d.keys():
        #     if i not in visit:
        #         visit.add(i)
        #         count+=1
        #         self.dfs(visit,d,count,i)
        # return count
                
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = set()
        d = {i:[] for i in range(n)}
        for i,j in edges:
            d[i].append(j)
            d[j].append(i)
        count = 0
        for i in d.keys():
            if i not in visit:
                count+=1
                self.dfs(visit,d,i)
        return count
#union find (disjoint set) algo
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, node):
        cur = node
        while cur != self.parent[cur]:
            self.parent[cur] = self.parent[self.parent[cur]]
            cur = self.parent[cur]
        return cur

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.rank[pv] > self.rank[pu]:
            pu, pv = pv, pu
        self.parent[pv] = pu
        self.rank[pu] += self.rank[pv]
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        res = n
        for u, v in edges:
            if dsu.union(u, v):
                res -= 1
        return res 
