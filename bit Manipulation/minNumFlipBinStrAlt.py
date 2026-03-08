class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s + s
        
        # Target patterns
        p1 = ""
        p2 = ""
        for i in range(len(s)):
            p1 += "0" if i % 2 == 0 else "1"
            p2 += "1" if i % 2 == 0 else "0"
            
        ans = float('inf')
        diff1, diff2 = 0, 0
        
        for i in range(len(s)):
            # Add new character entering the window
            if s[i] != p1[i]: diff1 += 1
            if s[i] != p2[i]: diff2 += 1
            
            # Once the window reaches size n, start checking/sliding
            if i >= n:
                # Remove the character that just left the window
                if s[i - n] != p1[i - n]: diff1 -= 1
                if s[i - n] != p2[i - n]: diff2 -= 1
                
            # Update answer only when we have a full window of size n
            if i >= n - 1:
                ans = min(ans, diff1, diff2)
                
        return ans