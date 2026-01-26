class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        d = {}
        count = 1
        for  i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i] = count
        f = [[] for _ in range (len(nums)+1)]
        for i,j in d.items():
            f[j].append(i)
        ans = []
        for i in range(len(nums),0,-1):
            for j in f[i]:
                ans.append(j)
                if  len(ans) == k:
                    return ans