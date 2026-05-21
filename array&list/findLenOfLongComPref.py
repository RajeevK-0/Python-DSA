class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()
        for val in arr1:
            while val > 0:
                prefixes.add(val)
                val //= 10 
        ans = 0
        for val in arr2:
            while val > 0:
                if val in prefixes:
                    # len(str(val)) gives us the prefix length
                    ans = max(ans, len(str(val)))
                    break 
                val //= 10
        return ans

    # def isPrefix(self,x,y):
    #     n = len(str(x))
    #     t = len(str(y))
    #     if n > t:   <--------- need to check for both x and y which ever is large swap them
    #         return (False,0)
    #     if x == (y//(10*(t-n))):
    #         return (True , n)
    #     else:
    #         if x != (y//(10*(t-n))) and len(str(x)) ==1:
    #             return (False,0)
    #         x = x//10
    #         while x >0:
    #             n = len(str(x))
    #             if x == (y//(10*(t-n))):
    #                 return (True , n)
    #             if n == 1 :    
    #                 return (False,0)
    #             x = x//10
    #     return (False,0)

        
        # ans = 0
        # for i in arr1:
        #     for j in arr2:
        #         t , c = self.isPrefix(i,j)
        #         if t == True:
        #             ans = max(ans,c)
        # return ans