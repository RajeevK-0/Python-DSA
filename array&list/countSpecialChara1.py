class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s = set(word)
        ans = 0
        for i in s:
            if i!=i.lower():
                if i.lower() in s:
                    ans+=1
        return ans