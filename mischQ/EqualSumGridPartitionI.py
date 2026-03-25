class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        total_sum = sum(sum(row) for row in grid)
        # If the total sum is odd, we can't split it into two equal integer sums
        if total_sum % 2 != 0:
            return False
        target = total_sum // 2
        # 1. Check Horizontal Cuts
        running_row_sum = 0
        for i in range(m - 1): # m-1 ensures the bottom section is non-empty
            running_row_sum += sum(grid[i])
            if running_row_sum == target:
                return True
        # 2. Check Vertical Cuts
        running_col_sum = 0
        for j in range(n - 1): # n-1 ensures the right section is non-empty
            # Sum the current column
            for i in range(m):
                running_col_sum += grid[i][j]
            if running_col_sum == target:
                return True
        return False