class Solution:
    def dfs(self,visit,d,node,prev,n):
        if node in visit and node != prev:
            return False
        visit.add(node)
        for i in d[node]:
            prev = node
            self.dfs(visit,d,i,prev,n)
        if n == len(visit):
            return True
        return False
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #if no node is given even then its a valid tree
        if not n:
            return True
        #edges are number of node-1 so if they dont match they arent valid tree
        if n-1 != len(edges):
            return False
        d = {i:[] for i in range(n) }
        for i,j in edges: 
            d[i].append(j)
            d[j].append(i)
        visit = set()
        prev = -1
        return self.dfs(visit,d,0,prev,n)