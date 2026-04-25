class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        
        # Flatten factories based on capacity
        factory_slots = []
        for pos, cap in factory:
            factory_slots.extend([pos] * cap)
            
        n, m = len(robot), len(factory_slots)
        # dp[i] will store the min distance for first i robots
        # Initialize with a very large number
        dp = [0] + [float('inf')] * n
        
        # Iterate through each factory slot
        for j in range(m):
            # Iterate backwards to reuse the same DP array (space optimization)
            for i in range(n, 0, -1):
                dist = abs(robot[i-1] - factory_slots[j])
                dp[i] = min(dp[i], dp[i-1] + dist)
                
        return dp[n]