class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        res = [""] * n
        char_code = ord('a')
        for i in range(n):
            if res[i] == "":
                if char_code > ord('z'):
                    return ""
                curr_char = chr(char_code)
                for j in range(i, n):
                    if lcp[i][j] > 0:
                        res[j] = curr_char
                char_code += 1
        if "" in res: return ""
        actual_lcp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if res[i] == res[j]:
                    actual_lcp[i][j] = actual_lcp[i + 1][j + 1] + 1
                else:
                    actual_lcp[i][j] = 0
                if actual_lcp[i][j] != lcp[i][j]:
                    return ""
        return "".join(res)
########################################################################
class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        word = [""] * n
        current = ord("a")
        for i in range(n):
            if not word[i]:
                if current > ord("z"):
                    return ""
                word[i] = chr(current)
                for j in range(i + 1, n):
                    if lcp[i][j]:
                        word[j] = word[i]
                current += 1
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word[i] != word[j]:
                    if lcp[i][j]:
                        return ""
                else:
                    if i == n - 1 or j == n - 1:
                        if lcp[i][j] != 1:
                            return ""
                    else:
                        if lcp[i][j] != lcp[i + 1][j + 1] + 1:
                            return ""
        return "".join(word)
####################################################################
class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        # Assign characters greedily
        s = [0] * n
        cur = 1
        for i in range(n):
            if s[i] > 0:
                continue
            if cur > 26:
                return ""
            for j in range(i, n):
                if lcp[i][j] > 0:
                    if s[j] > 0 and s[j] != cur:
                        return ""
                    s[j] = cur
            cur += 1
        # Verify LCP matrix
        # Build expected LCP and compare
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] == s[j]:
                    expected = 1 + (lcp[i + 1][j + 1] if i + 1 < n and j + 1 < n else 0)
                else:
                    expected = 0
                if lcp[i][j] != expected:
                    return ""
        return ''.join(chr(ord('a') + c - 1) for c in s)