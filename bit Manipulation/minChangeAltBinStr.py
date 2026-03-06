class Solution:
    def minOperations(self, s: str) -> int:
        count0 = 0  # Operations to make it start with '0' (0101...)
        
        for i in range(len(s)):
            # If i is even, we expect '0'. If i is odd, we expect '1'.
            # i % 2 gives us exactly that pattern: 0, 1, 0, 1...
            if int(s[i]) != i % 2:
                count0 += 1
        
        # The other option is making it start with '1' (1010...)
        # This would require (Total Length - count0) operations.
        return min(count0, len(s) - count0)