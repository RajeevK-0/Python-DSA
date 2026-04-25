class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        factory_slots = []
        for pos, cap in factory:
            factory_slots.extend([pos] * cap)
        n, m = len(robot), len(factory_slots)
        dp = [0] + [float('inf')] * n
        for j in range(m):
            for i in range(n, 0, -1):
                dist = abs(robot[i-1] - factory_slots[j])
                dp[i] = min(dp[i], dp[i-1] + dist)
        return dp[n]