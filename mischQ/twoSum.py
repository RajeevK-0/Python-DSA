class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        map = {}
        for i,j in enumerate(nums):
            s = target - j
            if s in map:
                return [map[s] , i]
            map[j] = i
        return