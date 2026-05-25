class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[n - 1] == '1':
            return False
            
        dp = [False] * n
        dp[0] = True
        
        reachable_count = 0
        
        for i in range(1, n):
            # Add the newest element that enters the window from the right side
            if i >= minJump:
                if dp[i - minJump]:
                    reachable_count += 1
                    
            # Remove the oldest element that leaves the window from the left side
            if i > maxJump:
                if dp[i - maxJump - 1]:
                    reachable_count -= 1
            
            # If the current position is '0' and there's a valid previous jump point
            if s[i] == '0' and reachable_count > 0:
                dp[i] = True
                
        return dp[n - 1]