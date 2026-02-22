class Solution:
    def pacific(self,i,j,heights):
        if i == 0 or j == 0:
            return True
        dir = [[-1,0],[0,-1],[1,0],[0,1]]
        visit = set()
        row , col = len(heights),len(heights[0])
        dq = deque()
        dq.append((i,j))
        visit.add((i,j))
        while dq:
            r,c = dq.popleft()
            for i,j in dir:
                nr , nc = i+r,j+c
                if nr in range(row) and nc in range(col) and heights[nr][nc]<=heights[r][c] and (nr,nc) not in visit:
                    dq.append((nr,nc))
                    visit.add((nr,nc))
                    if nr == 0 or nc == 0:
                        return True
    def atlantic(self,i,j,heights):
        dir = [[1,0],[0,1],[-1,0],[0,-1]]
        row , col = len(heights),len(heights[0])
        if i+1 == row or j+1 == col:
            return True
        visit = set()
        dq = deque()
        dq.append((i,j))
        visit.add((i,j))
        while dq:
            r,c = dq.popleft()
            for i,j in dir:
                nr , nc = i+r,j+c
                if nr in range(row) and nc in range(col) and heights[nr][nc]<=heights[r][c] and (nr,nc) not in visit:
                    dq.append((nr,nc))
                    visit.add((nr,nc))
                    if nr+1 == row or nc+1 == col:
                        return True
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        row , col = len(heights),len(heights[0])
        for i in range(row):
            for j in range(col):
                if self.pacific(i,j,heights) and self.atlantic(i,j,heights):
                    res.append([i,j])
        return res            
#optimize solution
class Solution:
    def pacific(self,heights,pac,atl):
        row ,col = len(heights),len(heights[0])
        visit = set()
        dq = deque()
        dir = [[1,0],[-1,0],[0,1],[0,-1]]
        dq.append(height[0][0])
        visit.add(height[0][0])
        while dq:
            r,c = dq.popleft()
            for rw , cl in dir:
                nr , nc = r+rw , c+cl
                if (nr,nc)not in pac and 0<=nr<row and 0<=nc<col and heights[nr][nc]>=heights[r][c]:
                    pac.add((nr,nc))
                if (nr,nc)not in atl and 0<=nr<row and 0<=nc<col and heights[nr][nc]>=heights[r][c]:
                    atl.add((nr,nc))
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        atl = set()
        row ,col = len(heights),len(heights[0])
        for i in range(col):
            pac.add(height[0][i])
            atl.add(height[row-1][i])