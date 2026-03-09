class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        
        # dp[i][j][0] -> ends in 0
        # dp[i][j][1] -> ends in 1
        dp = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]
        
        # Base cases: single blocks that don't exceed the limit
        for i in range(1, min(zero, limit) + 1):
            dp[i][0][0] = 1
        for j in range(1, min(one, limit) + 1):
            dp[0][j][1] = 1
            
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                # To form a sequence ending in 0:
                # We take a sequence ending in 1 and add 1 to 'limit' zeros.
                for k in range(1, min(i, limit) + 1):
                    dp[i][j][0] = (dp[i][j][0] + dp[i - k][j][1]) % MOD
                
                # To form a sequence ending in 1:
                # We take a sequence ending in 0 and add 1 to 'limit' ones.
                for k in range(1, min(j, limit) + 1):
                    dp[i][j][1] = (dp[i][j][1] + dp[i][j - k][0]) % MOD
                    
        return (dp[zero][one][0] + dp[zero][one][1]) % MOD