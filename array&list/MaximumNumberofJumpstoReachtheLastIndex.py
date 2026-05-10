class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # Initialize DP array with -1
        dp = [-1] * n
        dp[0] = 0 # Starting point
        
        for j in range(1, n):
            for i in range(j):
                # Check if previous index i is reachable and jump is valid
                if dp[i] != -1 and abs(nums[j] - nums[i]) <= target:
                    dp[j] = max(dp[j], dp[i] + 1)
                    
        return dp[n-1]