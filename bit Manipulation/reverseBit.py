class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            # Shift result left to make space
            res = res << 1
            # Get the last bit of n and add it to res
            res = res | (n & 1)
            # Shift n right to move to the next bit
            n = n >> 1
        return res