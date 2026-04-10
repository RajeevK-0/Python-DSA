class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        index_map = defaultdict(list)
    
        # Store indices
        for i, num in enumerate(nums):
            index_map[num].append(i)
        
        min_dist = float('inf')
        
        # Check each value
        for indices in index_map.values():
            if len(indices) >= 3:
                for i in range(len(indices) - 2):
                    dist = indices[i + 2] - indices[i]
                    min_dist = min(min_dist, dist)
        
        return 2 * min_dist if min_dist != float('inf') else -1