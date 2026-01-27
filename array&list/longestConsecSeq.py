class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        s = set(nums)
        ans = 0
        for i in s:
            c = i-1
            if c not in s:
                x = i
                while x+1 in s:
                    x += 1
                ans = max(ans,x-c)
        return ans