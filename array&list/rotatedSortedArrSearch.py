class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums)-1
        while i<=j:
            if nums[i] == target :
                return i
            if  nums[j] == target:
                return j
            mid = (i+j)//2
            if nums[mid] == target:
                return mid
            if nums[mid]>=nums[i]:
                if nums[mid] > target >= nums[i]:
                    j =mid-1
                else:
                    i = mid+1
            else:
                if nums[mid] < target <= nums[j]:
                    i = mid+1
                else:
                    j = mid-1
        return -1
