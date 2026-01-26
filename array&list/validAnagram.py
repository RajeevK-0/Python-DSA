class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        S = list(s)
        for l in t:
            try:
                S.remove(l)
            except:
                return False
        if S  == []:
            return True
        return False