class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        
        # Maps number -> [count_seen, total_sum_of_indices]
        # We'll use two passes (Left-to-Right and Right-to-Left)
        
        # Pass 1: Calculate distances to the LEFT
        count = defaultdict(int)
        sum_indices = defaultdict(int)
        for i, x in enumerate(nums):
            res[i] += (count[x] * i) - sum_indices[x]
            count[x] += 1
            sum_indices[x] += i
            
        # Pass 2: Calculate distances to the RIGHT
        count.clear()
        sum_indices.clear()
        for i in range(n - 1, -1, -1):
            x = nums[i]
            res[i] += sum_indices[x] - (count[x] * i)
            count[x] += 1
            sum_indices[x] += i
            
        return res