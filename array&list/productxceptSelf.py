class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ans = [1]*len(nums)
        l = 1
        for i in range(len(nums)):
            ans[i] = l
            l *= nums[i]
        r = 1
        for j in range(len(nums)-1,-1,-1):
            ans[j] *= r
            r *= nums[j]
        return ans
        