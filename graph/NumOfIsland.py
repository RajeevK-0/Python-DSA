# using breadth first search
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        row,col = len(grid) , len(grid[0])
        visit = set()
        island = 0
        dir = [[1,0],[-1,0],[0,1],[0,-1]]
        def bfs(r,c):
            dq = deque()
            dq.append((r,c))
            visit.add((r,c))
            while dq:
                rw,cl = dq.popleft()
                for ur,uc in dir:
                    nr , nc = rw+ur , cl+uc
                    if (nr,nc) not in visit and nr in range(row) and nc in range(col) and grid[nr][nc] == "1":
                        dq.append((nr,nc))
                        visit.add((nr,nc))
                        bfs(nr,nc)
        for i in range(row):
            for j in range(col):
                if (i,j) not in visit and grid[i][j]== "1":
                    bfs(i,j)
                    visit.add((i,j))
                    island+=1
        return island
    
#using depth first search
