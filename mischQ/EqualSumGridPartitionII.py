class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                total += grid[i][j]
        for _ in range(4):
            exist = set()
            exist.add(0)
            sum_val = 0
            m = len(grid)
            n = len(grid[0])
            if m < 2:
                grid = self.rotation(grid)
                continue
            if n == 1:
                for i in range(m - 1):
                    sum_val += grid[i][0]
                    tag = sum_val * 2 - total
                    if tag == 0 or tag == grid[0][0] or tag == grid[i][0]:
                        return True
                grid = self.rotation(grid)
                continue
            for i in range(m - 1):
                for j in range(n):
                    exist.add(grid[i][j])
                    sum_val += grid[i][j]
                tag = sum_val * 2 - total
                if i == 0:
                    if tag == 0 or tag == grid[0][0] or tag == grid[0][n - 1]:
                        return True
                    continue
                if tag in exist:
                    return True
            grid = self.rotation(grid)
        return False

    def rotation(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        tmp = [[0] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                tmp[j][m - 1 - i] = grid[i][j]
        return tmp
    
########################################################################################
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        
        H, W = len(grid), len(grid[0])

        row_sums = list(map(sum, grid))
        col_sums = [ sum(grid[r][c] for r in range(H)) for c in range(W) ]
        total_sum = sum(row_sums)

        # Try cutting rows first
        # row_cut is the row index of the top row of the BOTTOM HALF
        row_cut = 0
        top_sum = 0
        bottom_sum = total_sum

        # max legal value for row_cut is H-1
        # But we will allow row_cut to be H in the loop to trigger the "reverse time by 1 step" handling
        for row_cut in range(1, H+1):

            top_sum += row_sums[row_cut-1]
            bottom_sum -= row_sums[row_cut-1]

            if top_sum == bottom_sum:
                print(f"At row_cut {row_cut}, top/bottom sum is {top_sum}/{bottom_sum}")
                return True
            elif top_sum > bottom_sum:

                # Let's look for something to discount
                top_discountable = set()
                if row_cut == 1:
                    # Only the top row is on the top, and removing cells in the middle
                    # will lead to disconnections
                    top_discountable = { grid[row_cut-1][0], grid[row_cut-1][W-1] }
                elif W == 1:
                    # The width is one, and removing any cells except the top and bottom
                    # from the top section will lead to disconnections
                    top_discountable = { grid[0][0], grid[row_cut-1][0] }
                else:
                    # No cell will cause disconnections
                    top_discountable = { grid[r][c] for r in range(row_cut) for c in range(W) }

                difference = top_sum - bottom_sum
                if difference in top_discountable:
                    print(f"At row_cut {row_cut}, top/bottom sum is {top_sum}/{bottom_sum}")
                    print(f"The difference is discountable: {top_discountable}")
                    return True

                # Last resort, let's check if we can rewind by one step
                # to make bottom_sum the bigger value, and then look for a discount in the

                # Rewinding by one step would make top_sum decrease by row_sum[row_cut-1]
                # and increase bottom_sum by the same amount, and their difference would be

                difference_alt = (bottom_sum + 2*row_sums[row_cut-1]) - top_sum
                
                # Let's look for something to discount in the bottom
                if row_cut == H:
                    # If row_cut is currently H, then "rewind by 1" means grid[H-1] is the top row
                    # of the bottom half
                    bottom_discountable = { grid[H-1][0], grid[H-1][W-1] }
                elif W == 1:
                    # The width is one, and removing any cells except the top and bottom
                    # from the top section will lead to disconnections
                    bottom_discountable = { grid[row_cut-1][0], grid[H-1][0] }
                else:
                    bottom_discountable = { grid[r][c] for r in range(row_cut-1, H) for c in range(W) }

                if difference_alt in bottom_discountable:
                    print(f"At row_cut {row_cut}, minus 1, top/bottom sum is {top_sum}/{bottom_sum}")
                    print(f"The adjusted difference {difference_alt} is discountable: {bottom_discountable}")
                    return True
                else:
                    # Should we keep checking? It depends
                    smallest_top = top_sum - max(top_discountable)
                    if smallest_top < bottom_sum:
                        # There's still a chance we can use a discount to find a solution
                        
                        continue
                    elif row_cut == 1:
                        # top_discountable might grow bigger on the next round, let's try again anyway
                        continue
                    else:
                        break

        col_cut = 0
        left_sum = 0
        right_sum = total_sum

        for col_cut in range(1, W+1):

            left_sum += col_sums[col_cut-1]
            right_sum -= col_sums[col_cut-1]

            if left_sum == right_sum:
                print(f"At col_cut {col_cut}, left/right sum is {left_sum}/{right_sum}")
                return True
            elif left_sum > right_sum:

                # Let's look for something to discount
                left_discountable = set()
                if col_cut == 1:
                    left_discountable = { grid[0][0], grid[H-1][0] }
                elif H == 1:
                    # The height is one, and removing any cells except the left and right
                    # from the left section will lead to disconnections
                    left_discountable = { grid[0][0], grid[0][col_cut-1] }
                else:
                    left_discountable = { grid[r][c] for c in range(col_cut) for r in range(H) }

                difference = left_sum - right_sum
                if difference in left_discountable:
                    print(f"At col_cut {col_cut}, left/right sum is {left_sum}/{right_sum}")
                    print(f"The difference {difference} is discountable on the left: {left_discountable}")
                    return True

                # Last resort, let's check if we can rewind by one step
                # to make right_sum the bigger value, and then look for a discount in the

                # Rewinding by one step would make left_sum decrease by col_sum[col_cut-1]
                # and increase right_sum by the same amount, and their difference would be

                difference_alt = (right_sum + 2*col_sums[col_cut-1]) - left_sum
                
                # Let's look for something to discount in the bottom
                if col_cut == W:
                    right_discountable = { grid[0][W-1], grid[H-1][W-1] }
                elif H == 1:
                    # The height is one, and removing any cells except the left and right
                    # from the right section will lead to disconnections
                    right_discountable = { grid[0][col_cut-1], grid[0][W-1] }
                else:
                    right_discountable = { grid[r][c] for c in range(col_cut-1, W) for r in range(H) }

                if difference_alt in right_discountable:
                    print(f"At col_cut {col_cut}, minus 1, left/right sum is {left_sum}/{right_sum}")
                    print(f"The adjust difference {difference_alt} is discountable on the right: {right_discountable}")
                    return True
                else:
                    # Should we keep checking? It depends
                    smallest_left = left_sum - max(left_discountable)
                    if smallest_left < right_sum:
                        # There's still a chance we can use a discount to find a solution
                        
                        continue
                    elif col_cut == 1:
                        # left_discountable might grow bigger on the next round, let's try again anyway
                        continue
                    else:
                        break

        return False
################################################################################################################################
class Solution:
  def canPartitionGrid(self, grid: list[list[int]]) -> bool:
    summ = sum(map(sum, grid))

    def canPartition(grid: list[list[int]]) -> bool:
      topSum = 0
      seen = set()
      for i, row in enumerate(grid):
        topSum += sum(row)
        botSum = summ - topSum
        seen |= set(row)
        if topSum - botSum in (0, grid[0][0],  grid[0][-1], row[0]):
          return True
        if len(grid[0]) > 1 and i > 0 and topSum - botSum in seen:
          return True
      return False

    return (canPartition(grid) or
            canPartition(grid[::-1]) or
            canPartition(list(zip(*grid))[::-1]) or
            canPartition(list(zip(*grid))))