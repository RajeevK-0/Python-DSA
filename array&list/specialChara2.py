class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        d = {}
        for i in range(len(word)):
            if word[i] not in d:
                d[word[i]] = [i]
            else:
                d[word[i]].append(i)
        ans =0
        vis = [0]*26
        for i in word:
            if i!=i.upper() and vis[ord(i)-97]!=1:
                if i in d:
                    if i.upper() in d:
                        if d[i][-1] < d[i.upper()][0]:
                            ans+=1 
                            vis[ord(i)-97] = 1
        return ans
        # s = set(word)'
        # ans = 0
        # for i in s:
        #     if i != i.upper():
        #         if i.upper() in s:
        #             ans +=1
        # return ans