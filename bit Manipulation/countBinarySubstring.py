class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans = 0
        prev_count = 0
        curr_count = 1
        
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                # We hit a switch (0 to 1 or 1 to 0)
                ans += min(prev_count, curr_count)
                prev_count = curr_count
                curr_count = 1
            else:
                curr_count += 1
               
        # Add the last transition
        return ans + min(prev_count, curr_count)