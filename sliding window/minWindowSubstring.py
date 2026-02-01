class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" :
            return ""
        countT = {}
        countS = {}
        
        for i in t:
            countT[i] = countT.get(i,0)+1
            
        res = [-1,-1]
        resL = float('inf')
        need = len(countT)
        have = 0
        j = 0
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i],0)+1
            if s[i] in countT and countS[s[i]] == countT[s[i]]:
                have+=1
            while have == need:
                if (i-j+1)<resL:
                    res = [j,i]
                    resL = i-j+1
                countS[s[j]]-=1
                if s[j] in countT and countS[s[j]]<countT[s[j]]:
                    have-=1
                j+=1
        l,r = res
        return s[l:r+1] if resL != float('inf') else ""



 # if len(s)<len(t):
        #     return ""
        # if len(s) == len(t):
        #     if sorted(s)== sorted(t):
        #         return s
        #     return ""
        # start = 0
        # dt = {}
        # for i in t:
        #     dt[i] = dt.get(i,0)+1
        # scount = 0
        # ds={}
        # for end in range(len(s)):
        #     if s[end] in dt and scount == 0:
        #         start = end
        #     if s[end] in dt:
        #         scount+=1
        #     if scount >= len(dt.keys()):
        #         res = start,end
        #         start+=1
        #         while s[start] not in dt:
        #             start +=1
        #         scount-=1
        #         rs = s[res[0]:res[1]+1]
        # return rs
        # start = 0
        # if len(s)<len(t):
        #     return res
        # d = {}
        # ds = {}
        # for i in t:
        #     d[i] = d.get(i ,0)+1
        # for end in range(len(s)):
        #     if s[end] in d and s[start] not in d:
        #         start = end
        #     ds[s[end]] = ds.get(s[end],0)+1
        #     c = 0
        #     for i in d.keys():
        #         if i in ds and ds[i]>=d[i]:
        #             c+=1
        #     if len(d.keys())==c:
        #         res = s[start:end+1]
        #         if len(res)>end-start+1:
        #             res = s[start:end+1]
        # return res                