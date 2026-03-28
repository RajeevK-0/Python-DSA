class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        res = [""] * n
        char_code = ord('a')
        
        # 1. Greedy Construction
        for i in range(n):
            if res[i] == "":
                if char_code > ord('z'):
                    return ""
                curr_char = chr(char_code)
                for j in range(i, n):
                    if lcp[i][j] > 0:
                        res[j] = curr_char
                char_code += 1
        
        # Check if any index was left unassigned
        if "" in res: return ""
        
        # 2. Verification using DP
        # We build the actual LCP matrix for our string from bottom-right to top-left
        actual_lcp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if res[i] == res[j]:
                    actual_lcp[i][j] = actual_lcp[i + 1][j + 1] + 1
                else:
                    actual_lcp[i][j] = 0
                
                # Immediate check against input
                if actual_lcp[i][j] != lcp[i][j]:
                    return ""
                    
        return "".join(res)