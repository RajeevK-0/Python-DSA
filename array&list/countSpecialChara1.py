class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s = set(word)
        ans = 0
        for i in s:
            if i!=i.lower():
                if i.lower() in s:
                    ans+=1
        return ans
    #m2
    # d = {}
        # visited = [0]*26
        # for i in word:
        #     d[i] = d.get(i,0)+1
        # special = 0
        # for i in d.keys():
        #     if i != i.lower():
        #         if i in d and ord(i.lower())-97==0 :
        #             special+=1
        #             visited[ord(i.lower())-97] = 1
        # return special