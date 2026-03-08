class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = []
        for i in range(len(nums)):
            # If the i-th bit of the i-th string is '0', use '1'
            # If it's '1', use '0'
            res.append("1" if nums[i][i] == "0" else "0")
            
        return "".join(res)