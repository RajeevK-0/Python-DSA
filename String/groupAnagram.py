class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d = {}
        for word in strs:
            t = [0]*26
            for c in word:
                k = ord(c)-ord('a')
                t[k] += 1
            key = tuple(t)
            if key in d:
                d[key].append(word)
            else:
                d[key] = [word] 
        return list(d.values())     