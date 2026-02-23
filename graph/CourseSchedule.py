class Solution:
    def dfs(self,d,cs,visit):
        if cs in visit:
            return False
        if d[cs] == []:
            return True
        visit.add(cs)
        for i in d[cs]:
            if not self.dfs(d,i,visit):
                return False
        visit.remove(cs)
        d[cs] = []
        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = {i:[] for i in range(numCourses)}
        for i,j in prerequisites:
            d[i].append(j)
        visit = set()
        for i in d.keys():
            if not self.dfs(d,i,visit):
                return False
        return True        
