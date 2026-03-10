class Solution:
    def binary(self,nums,s,e):
        mid = (s+e)//2
        if s==e:
            return mid
        if nums[mid] > nums[e]:
            return self.binary(nums,mid+1,e)
        else:
            return self.binary(nums,s,mid)
    def findMin(self, nums: List[int]) -> int:
        return nums[self.binary(nums,0,len(nums)-1)]