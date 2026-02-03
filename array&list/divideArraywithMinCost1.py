class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        first = nums[0]
        min1 = 61
        min2 = 62
        for i in range(1,len(nums )):
            val = nums[i]
            if val<min1:
                min2 = min1
                min1 = val
            elif val<min2:
                min2 = val
        return first+min1+min2

        
        # first = nums[0]
        # rem = sorted(nums[1:])
        # ans = first+rem[0]+rem[1]
        # return ans
        
        # mn = 51
        # for i in range(1,len(nums)):
        #     mn = min(nums[i],mn)
        # sec = mn
        # third = 51
        # for i in range(1,len(nums)):
        #     if nums[i] == sec:
        #         third = nums[i]
        #     else:
        #         third = min(nums[i],third)
        # ans = fElement+sec+third
        # return ans