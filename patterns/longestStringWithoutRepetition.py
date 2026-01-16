class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        start = 0
        result = 0
        for i in range(len(s)):
            if s[i] in map and map[s[i]] >= start:
                start = map[s[i]]+1
            map[s[i]] = i
            result = max(result, map[s[i]]-start+1)
        return result