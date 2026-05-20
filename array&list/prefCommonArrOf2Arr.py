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
            # if A[i] == B[i]:
            #     com+=1
            c.append(com)
        return c
        