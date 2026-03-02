class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        trailing_zeros = []
        for row in grid:
            count = 0
            for i in range(n - 1, -1, -1):
                if row[i] == 0:
                    count += 1
                else:
                    break
            trailing_zeros.append(count)
        swaps = 0
        for i in range(n):
            target_zeros = n - 1 - i
            found = False
            for j in range(i, n):
                if trailing_zeros[j] >= target_zeros:
                    row_to_move = trailing_zeros.pop(j)
                    trailing_zeros.insert(i, row_to_move)
                    swaps += (j - i)
                    found = True
                    break
            
            if not found:
                return -1
                
        return swaps