class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # Step 1: Create a number that should be all 1s if n alternates
        all_ones = n ^ (n >> 1)
        
        # Step 2: Check if all_ones + 1 is a power of 2
        # (e.g., 1111 & 10000 == 0)
        return (all_ones & (all_ones + 1)) == 0