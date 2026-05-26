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
    #m3
    # a-z:97,122
        # A-Z:65,90
        # res = [0]*26
        # seen_upper, seen_lower = set(), set()
        # for c in word:
        #     if ord(c)>96 and c not in seen_lower:
        #         res[97-ord(c)]+= 1
        #         seen_lower.add(c)
        #     if ord(c)<91 and c not in seen_upper:
        #         res[65-ord(c)]+= 1
        #         seen_upper.add(c)
        # ans = 0
        # for num in res:
        #     if num==2:
        #         ans+=1
        # return ans