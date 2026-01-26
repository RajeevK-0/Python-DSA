from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d = defaultdict(list)
        for i in strs:
            count = [0]*26
            for j in i:
                t = ord(j)-ord('a')
                count[t]+=1
            d[tuple(count)].append(i)
        return list(d.values())
        