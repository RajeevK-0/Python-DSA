# 3129. Find All Possible Stable Binary Arrays I
#Topic Dp,Presum
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        dp = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]
        for i in range(1, min(zero, limit) + 1):
            dp[i][0][0] = 1
        for j in range(1, min(one, limit) + 1):
            dp[0][j][1] = 1
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                for k in range(1, min(i, limit) + 1):
                    dp[i][j][0] = (dp[i][j][0] + dp[i - k][j][1]) % MOD
                for k in range(1, min(j, limit) + 1):
                    dp[i][j][1] = (dp[i][j][1] + dp[i][j - k][0]) % MOD
        return (dp[zero][one][0] + dp[zero][one][1]) % MOD