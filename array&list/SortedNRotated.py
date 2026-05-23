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
#m2
# class Solution:
#     def check(self, nums: List[int]) -> bool:
#         count = 0
#         n = len(nums)
#         for i in range(n):
#             if nums[i] > nums[(i + 1) % n]:
#                 count += 1
#         return count <= 1
#m3
# class Solution:
#     def check(self, nums: List[int]) -> bool:
#         cnt = 0
#         for i in range(1, len(nums)):
#             if nums[i] < nums[i - 1]:
#                 cnt += 1
#             if cnt == 1 and nums[-1] > nums[0]:
#                 return False
#             if cnt > 1:
#                 return False
#         return True
        