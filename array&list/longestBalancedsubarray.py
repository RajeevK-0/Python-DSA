class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 0
        
        for i in range(n):
            evens = set()
            odds = set()
            for j in range(i, n):
                val = nums[j]
                if val % 2 == 0:
                    evens.add(val)
                else:
                    odds.add(val)
                if len(evens) == len(odds):
                    max_len = max(max_len, j - i + 1)
                    
        return max_len