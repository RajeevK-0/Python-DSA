class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        s = set()
        c = []
        com = 0
        for i in range(len(A)):
            if A[i] in s :
                com+=1
            else:
                s.add(A[i])
            if B[i] in s:
                com+=1
            else:
                s.add(B[i])
            # if A[i] == B[i]: <--------- if want to elaborate steps like this use and in above if's and keep check that a!=b
            #     com+=1
            c.append(com)
        return c
        # could do the same without equating a and b since one of them will end up in dict first
        # c = []
        # ma = {}
        # mb = {}
        # com = 0
        # for i in range(len(A)):
        #     ma[A[i]] = i
        #     mb[B[i]] = i
        #     if A[i] == B[i] :
        #         com +=1
        #     if (A[i] in mb and A[i] != B[i] ) : 
        #         com+=1
        #     if (B[i] in ma and A[i] != B[i]):
        #         com+=1
        #     c.append(com)
        # return c
        #method 3
        # counts = [0]*(len(A)+1)
        # common = 0
        # C = []
        # for a,b in zip(A,B):
        #     counts[a]+=1
        #     if counts[a]==2:
        #         common+=1
        #     counts[b]+=1
        #     if counts[b]==2:
        #         common+=1
        #     C.append(common)
        # return C