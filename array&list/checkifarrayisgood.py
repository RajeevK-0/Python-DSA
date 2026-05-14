class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        n = nums[-1]
        if n+1!=len(nums):
            return False
        for i in range(1,n+1):
            if i!=nums[i-1]:
                return False
        return True