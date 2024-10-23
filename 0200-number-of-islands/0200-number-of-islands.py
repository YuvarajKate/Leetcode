class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        def dfs(grid, i, j):
            # If we are out of bounds or the current cell is water ('0'), return
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
                return
            
            # Mark the current cell as visited by setting it to '0' (water)
            grid[i][j] = '0'
            
            # Visit all adjacent cells (up, down, left, right)
            dfs(grid, i + 1, j)
            dfs(grid, i - 1, j)
            dfs(grid, i, j + 1)
            dfs(grid, i, j - 1)
        
        num_islands = 0
        
        # Iterate through the grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # Whenever we encounter an unvisited land cell ('1'), it is part of a new island
                if grid[i][j] == '1':
                    num_islands += 1
                    # Perform DFS to mark the entire island
                    dfs(grid, i, j)
        
        return num_islands