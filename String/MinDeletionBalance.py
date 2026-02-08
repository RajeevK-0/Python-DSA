class Solution:
    def minimumDeletions(self, s: str) -> int:
        delCount = 0
        bCount = 0
        for c in s:
            if c == 'b':
                bCount += 1
            else:
                delCount = min(delCount+1,bCount)
        return delCount 