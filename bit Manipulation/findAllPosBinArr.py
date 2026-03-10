class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        
        # dp[i][j][0] -> i zeros, j ones, ends in 0
        # dp[i][j][1] -> i zeros, j ones, ends in 1
        dp = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]
        
        # Base cases: single blocks of 0s or 1s within the limit
        for i in range(1, min(zero, limit) + 1):
            dp[i][0][0] = 1
        for j in range(1, min(one, limit) + 1):
            dp[0][j][1] = 1
            
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                # To end in 0: we can add a 0 to any stable sequence ending in 0 or 1
                # But we must subtract sequences that would exceed the 'limit' of 0s
                dp[i][j][0] = (dp[i-1][j][0] + dp[i-1][j][1]) % MOD
                if i > limit:
                    # Subtract sequences that ended in a '1' followed by exactly 'limit' zeros
                    dp[i][j][0] = (dp[i][j][0] - dp[i - limit - 1][j][1] + MOD) % MOD
                    
                # To end in 1: we can add a 1 to any stable sequence ending in 0 or 1
                # But we must subtract sequences that would exceed the 'limit' of 1s
                dp[i][j][1] = (dp[i][j-1][0] + dp[i][j-1][1]) % MOD
                if j > limit:
                    # Subtract sequences that ended in a '0' followed by exactly 'limit' ones
                    dp[i][j][1] = (dp[i][j][1] - dp[i][j - limit - 1][0] + MOD) % MOD
                    
        return (dp[zero][one][0] + dp[zero][one][1]) % MOD