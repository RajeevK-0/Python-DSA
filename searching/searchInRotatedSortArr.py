class Solution:
    def binary(self,nums,s,e,target):
        if s>e:
            return -1
        mid = (s+e)//2
        if nums[mid] == target:
            return mid
        if nums[s] <= nums[mid]:
            if nums[s] <= target <nums[mid]:
                return self.binary(nums,s,mid-1,target)
            else:
                return self.binary(nums,mid+1,e,target)
        else :
            if nums[mid] < target <= nums[e]:
                return self.binary(nums,mid+1,e,target)
            else:
                return self.binary(nums,s,mid-1,target)
    def search(self, nums: List[int], target: int) -> int:
        return self.binary(nums,0,len(nums)-1,target)