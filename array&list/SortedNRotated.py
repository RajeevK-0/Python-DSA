class Solution:
    def check(self, nums: List[int]) -> bool:
        n =  len(nums)
        count = 1
        c = nums[0]
        i = 1
        while i<2*n:
            if nums[(i-1)%n] <= nums[i%n]:
                count+=1
                i+=1
            else:
                count = 1
                i+=1
            if count == n:
                return True
            
        return n==1
class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count += 1
        return count <= 1
      