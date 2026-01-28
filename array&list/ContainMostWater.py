class Solution:
    def maxArea(self, heights: list[int]) -> int:
        i= 0
        j = len(heights)-1
        ans = 0
        while i < j:
            w = j-i
            h = min(heights[i],heights[j])
            a = w*h
            ans = max(ans,a)
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return ans