def twoSum(nums, i , target,ans):
        j= len(nums)-1
        while i<j:
            t = nums[i]+nums[j]
            if t == target:
                ans.append([-target,nums[i],nums[j]]) 
                while i<j and nums[i] == nums[i+1]:
                    i+=1
                while i<j and nums[j] == nums[j-1]:
                    j-=1
                i+=1
                j-=1
            elif nums[i]+nums[j] > target:
                j-=1
            else:
                i+=1
        return ans
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if nums[i]>0:
                break
            if i>0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            twoSum(nums,j,-nums[i],ans)
        return ans