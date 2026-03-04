class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        
        row_counts = [0] * rows
        col_counts = [0] * cols
        
       
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 1:
                    row_counts[r] += 1
                    col_counts[c] += 1
                    
        special_count = 0
        
        
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 1:
                    if row_counts[r] == 1 and col_counts[c] == 1:
                        special_count += 1
                        
        return special_count