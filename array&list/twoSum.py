class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        d = {}
        for i in range(n):
            x = target-nums[i]
            if x in d:
                ans = [d[x],i]
            else:
                d[nums[i]] = i
        return ans