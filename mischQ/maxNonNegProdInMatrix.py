m, n = len(grid), len(grid[0])
        # Initialize DP tables with the starting value
        max_dp = [[0.0] * n for _ in range(m)]
        min_dp = [[0.0] * n for _ in range(m)]
        
        max_dp[0][0] = min_dp[0][0] = grid[0][0]
        
        # Fill first column
        for i in range(1, m):
            max_dp[i][0] = min_dp[i][0] = max_dp[i-1][0] * grid[i][0]
        
        # Fill first row
        for j in range(1, n):
            max_dp[0][j] = min_dp[0][j] = max_dp[0][j-1] * grid[0][j]
            
        # Fill the rest of the grid
        for i in range(1, m):
            for j in range(1, n):
                v = grid[i][j]
                # Candidates are coming from the top or from the left
                choices = (max_dp[i-1][j] * v, min_dp[i-1][j] * v, 
                           max_dp[i][j-1] * v, min_dp[i][j-1] * v)
                max_dp[i][j] = max(choices)
                min_dp[i][j] = min(choices)
        
        res = int(max_dp[-1][-1])
        return res % (10**9 + 7) if res >= 0 else -1