class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        num_layers = min(m, n) // 2
        
        for layer in range(num_layers):
            # 1. Collect elements of the current layer
            elements = []
            
            # Top row (left to right)
            for j in range(layer, n - layer - 1):
                elements.append(grid[layer][j])
            # Right column (top to bottom)
            for i in range(layer, m - layer - 1):
                elements.append(grid[i][n - layer - 1])
            # Bottom row (right to left)
            for j in range(n - layer - 1, layer, -1):
                elements.append(grid[m - layer - 1][j])
            # Left column (bottom to top)
            for i in range(m - layer - 1, layer, -1):
                elements.append(grid[i][layer])
                
            # 2. Rotate the list
            # Counter-clockwise rotation by k means the element at index i 
            # moves to (i - k) % length. Effectively, we slice the list.
            L = len(elements)
            shift = k % L
            rotated = elements[shift:] + elements[:shift]
            
            # 3. Put elements back into the grid
            idx = 0
            for j in range(layer, n - layer - 1):
                grid[layer][j] = rotated[idx]
                idx += 1
            for i in range(layer, m - layer - 1):
                grid[i][n - layer - 1] = rotated[idx]
                idx += 1
            for j in range(n - layer - 1, layer, -1):
                grid[m - layer - 1][j] = rotated[idx]
                idx += 1
            for i in range(m - layer - 1, layer, -1):
                grid[i][layer] = rotated[idx]
                idx += 1
                
        return grid