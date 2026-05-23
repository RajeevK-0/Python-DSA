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
        
        
    
        # simple = False
        # last = nums[0]
        # i = 1
        # while i < len(nums) 
        #     if nums[i] >= last:
        #         i+=1
        #     else:
        #         break
        #     if i == len(nums)-1:
        #         simple = True
        # # i,j = 0,len(nums)-1
        # # while i<j:
        # #     mid = (i+j)//2
        # #     if nums[i] > nums[j]:
        # #         if nums[mid] < nums[j]:
        # #             j = mid-1
        # #         else:
        # #             i = mid+1
        # #     else:
        # #         if mid 