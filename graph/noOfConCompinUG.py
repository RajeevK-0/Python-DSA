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
         
