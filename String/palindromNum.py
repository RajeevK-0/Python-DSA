class Solution:
    def isPalindrome(self, x: int) -> bool:
        X = str(x)
        if X == X[::-1]:
            return True
        return False