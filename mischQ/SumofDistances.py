class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        count = defaultdict(int)
        sum_indices = defaultdict(int)
        for i, x in enumerate(nums):
            res[i] += (count[x] * i) - sum_indices[x]
            count[x] += 1
            sum_indices[x] += i
        count.clear()
        sum_indices.clear()
        for i in range(n - 1, -1, -1):
            x = nums[i]
            res[i] += sum_indices[x] - (count[x] * i)
            count[x] += 1
            sum_indices[x] += i
        return res