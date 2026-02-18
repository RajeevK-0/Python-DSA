class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        all_ones = n ^ (n >> 1)
        return (all_ones & (all_ones + 1)) == 0