class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i,j in enumerate(nums):
            s = target - j
            if s in map:
                return [map[s] , i]
            map[j] = i
        return