class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])
        shift = k % n
        if shift == 0:
            return True
        for i in range(m):
            for j in range(n):
                if i % 2 == 0:
                    if mat[i][j] != mat[i][(j + shift) % n]:
                        return False
                else:
                    if mat[i][j] != mat[i][(j - shift + n) % n]:
                        return False
        return True
########################################################################
class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n = len(mat)
        m = len(mat[0])
        k %= m
        if not k:
            return True
        for i in range(n):
            row = mat[i][(-1) ** (i) * k:] + mat[i][:(-1) ** (i) * k]
            if mat[i] != row:
                return False
        return True
#########################################################################
class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        for l in mat:
            n = len(l)
            for i in range(n):
                if l[i] != l[(i+k)%n]:
                    return False
        return True