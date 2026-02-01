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




        