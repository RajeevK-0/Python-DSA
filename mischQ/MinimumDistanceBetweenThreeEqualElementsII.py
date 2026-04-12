class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        positions = defaultdict(list)
        for i, num in enumerate(nums):
            positions[num].append(i)
        ans = float('inf')
        for indices in positions.values():
            if len(indices) < 3:
                continue
            for i in range(len(indices) - 2):
                dist = 2 * (indices[i + 2] - indices[i])
                ans = min(ans, dist)
        return ans if ans != float('inf') else -1