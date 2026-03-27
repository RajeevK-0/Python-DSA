class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])
        # We only care about k relative to the row length
        shift = k % n
        
        if shift == 0:
            return True
            
        for i in range(m):
            for j in range(n):
                # If row is even (0, 2...), it shifts left
                # The element at j must match the element at (j + shift) % n
                if i % 2 == 0:
                    if mat[i][j] != mat[i][(j + shift) % n]:
                        return False
                # If row is odd (1, 3...), it shifts right
                # The element at j must match the element at (j - shift) % n
                else:
                    if mat[i][j] != mat[i][(j - shift + n) % n]:
                        return False
        return True