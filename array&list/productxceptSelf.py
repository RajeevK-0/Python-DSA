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
    # for  i in nums:
        #     if prefix == []:
        #         prefix.append(1)
        #     else:
        #         t=1
        #         for j in prefix:
        #             t = t*j
        #         prefix.append(t)
        # for i in range(len(nums),0,-1):
        #     if suffix = []:
        #         suffix[i] = 1 
        #     else:
        #         t = 1
        #         for j in range(len(suffix),i,-1):
        #             t *= j
        #         suffix[i] = t
        