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