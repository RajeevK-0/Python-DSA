class Solution:
    def bfs(self,i,j,visit,grid):
        row , col = len(grid),len(grid[0])
        dir = [[1,0],[-1,0],[0,1],[0,-1]]
        ans = 1
        dq = deque()
        dq.append((i,j))
        visit.add((i,j))
        while dq:
            r,c = dq.popleft()
            for rw,cl in dir:
                nr , nc = r+rw,c+cl
                if (0<=nr<row and 
                    0<=nc<col and
                    (nr,nc) not in visit and
                    grid[nr][nc] == 1):
                    ans+=1
                    dq.append((nr,nc))
                    visit.add((nr,nc))         
        return ans
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
        count = 0
        visit = set()
        row , col = len(grid),len(grid[0])
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and (i,j) not in visit :
                    # visit.add((i,j))
                    # a = bfs(i,j)
                    # print(a)
                    count = max(self.bfs(i,j,visit,grid),count)
        return count