class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        positions = defaultdict(list)
    
        # Store indices for each value
        for i, num in enumerate(nums):
            positions[num].append(i)
        
        ans = float('inf')
        
        # Process each value
        for indices in positions.values():
            if len(indices) < 3:
                continue
            
            # Check consecutive triples
            for i in range(len(indices) - 2):
                dist = 2 * (indices[i + 2] - indices[i])
                ans = min(ans, dist)
        
        return ans if ans != float('inf') else -1