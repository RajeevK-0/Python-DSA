class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        c = 0
        j = 0
        for i in range(len(s)):
            if s[i] in d and d[s[i]]>=j:
                j = d[s[i]] + 1 
            d[s[i]] = i
            c = max(c,i-j+1)
        return c