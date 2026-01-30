class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i = 0
        j = len(numbers)-1
        ans = []
        while i<j:
            if numbers[i]+numbers[j]==target:
                ans.append(i+1)
                ans.append(j+1)
                return ans
            elif numbers[i]+numbers[j] < target:
                i+=1
            else:
                j-=1           