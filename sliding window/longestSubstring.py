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
    # c = 0
        # for i in range(len(s)):
        #     j = i
        #     if s[i] in d:
        #         while j<=i:
        #             d[s[j]]-=1
        #             j+=1
        #     else:
        #         d[s[i]] = 1
        #     c = max(c,len(d.keys()))
        # return c 
    # i = 0
        # while i < len(s):
        #     j = i
        #     while s[i] not in d:
        #         d[s[i]] = 1
        #         i+=1
        #     if s[j] in d and j<=i:
        #         j+=1
        #         d[s[j]]-=1
        #     i+=1
        # return len(d.keys())