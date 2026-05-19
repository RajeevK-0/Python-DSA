class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        j = 0      
        n = len(nums1)
        m = len(nums2)
        while i < n and j < m:
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] < nums2[j]:
                i+=1
            else:
                j+=1
        return -1

        #method 2
        if nums1[-1] < nums2[0]:
            return -1
        if nums2[-1] < nums1[0]:
            return -1
        p1, p2 = 0, 0
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                return nums1[p1]
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1
        
        return -1