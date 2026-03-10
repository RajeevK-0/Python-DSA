class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            c = 0
            k = str(bin(i))
            for j in k:
                if j == '1':
                    c+=1
            res.append(c)
        return res