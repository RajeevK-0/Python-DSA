class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()
        
        # Step 1: Put all mathematical prefixes of arr1 into a set
        for val in arr1:
            while val > 0:
                prefixes.add(val)
                val //= 10  # Strips the last digit mathematically
                
        ans = 0
        
        # Step 2: Crop numbers in arr2 and check if they exist in our set
        for val in arr2:
            while val > 0:
                if val in prefixes:
                    # len(str(val)) gives us the prefix length
                    ans = max(ans, len(str(val)))
                    break # Since we go top-down, the first match is the longest for THIS number
                val //= 10
                
        return ans

        # ans = 0
        # for i in arr1:
        #     for j in arr2:
        #         t , c = self.isPrefix(i,j)
        #         if t == True:
        #             ans = max(ans,c)
        # return ans