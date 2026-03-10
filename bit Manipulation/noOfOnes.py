class Solution:
    def hammingWeight(self, n: int) -> int:
        t = str(bin(n))
        print(t)
        c=0
        for i in t:
            if i == '1':
                c+=1
        return c