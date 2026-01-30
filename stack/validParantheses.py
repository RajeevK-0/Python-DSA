class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(': ')', '{': '}', '[' : ']'}
        stack = []
        for i in s:
            if stack != [] and stack[-1] in d and i == d[stack[-1]]:
                stack.pop()
            else:
                stack.append(i)
        return not stack
