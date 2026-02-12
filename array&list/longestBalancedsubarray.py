class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 0
        
        for i in range(n):
            distinct_evens = set()
            distinct_odds = set()
            
            for j in range(i, n):
                val = nums[j]
                if val % 2 == 0:
                    distinct_evens.add(val)
                else:
                    distinct_odds.add(val)
                
                # Check if the current subarray [i...j] is balanced
                if len(distinct_evens) == len(distinct_odds):
                    max_len = max(max_len, j - i + 1)
                    
        return max_len