class Solution:

    def encode(self, strs: list[str]) -> str:
        s = ''
        for i in strs:
            n = len(i)
            s += str(n)+'#'+i
        return s
    def decode(self, s: str) -> list[str]:
        strs = []
        i = 0 
        while i<len(s):
            j = i 
            while s[j] != "#":
                j+=1
            l = int(s[i:j])
            r = s[j+1:j+1+l] 
            strs.append(r)
            i = j+1+l
        return strs