class Solution:
    def xorAfterQueries(self, nums: list[int], queries: list[list[int]]) -> int:
        MOD = 10**9 + 7
        
        for l, r, k, v in queries:
            # We use a range with step k to replicate the while loop efficiently
            # range(start, stop, step) is much faster in Python than a manual while loop
            for idx in range(l, r + 1, k):
                nums[idx] = (nums[idx] * v) % MOD
        
        result = 0
        for num in nums:
            result ^= num
            
        return result