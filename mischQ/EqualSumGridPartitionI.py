class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        total_sum = sum(sum(row) for row in grid)
        if total_sum % 2 != 0:
            return False
        target = total_sum // 2
        running_row_sum = 0
        for i in range(m - 1): 
            running_row_sum += sum(grid[i])
            if running_row_sum == target:
                return True
        running_col_sum = 0
        for j in range(n - 1):
            for i in range(m):
                running_col_sum += grid[i][j]
            if running_col_sum == target:
                return True
        return False
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:

                # Sum rows of the grid or its transpose and 
                # determine whether the equal partition exists
        def partitionExists(arr: list, sm = 0)-> bool:

            for row in arr:
                sm+= sum(row)
                if sm == halfSum: return True
                if sm >  halfSum: return False


                # Determine the target sum for each partition
                # and whether sum(grid) is odd
        halfSum, mod_ = divmod(sum(chain(*grid)), 2)
        if mod_ : return False

                # Check horizontal and vertical partitions
        return (partitionExists(grid) or 
                partitionExists(zip(*grid)))