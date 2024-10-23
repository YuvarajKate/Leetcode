class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        
        # Directions for moving up, down, left, right
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Visited matrices for Pacific and Atlantic
        visited_pacific = [[False] * cols for _ in range(rows)]
        visited_atlantic = [[False] * cols for _ in range(rows)]
        
        def dfs(row: int, col: int, visited: List[List[bool]]):
            visited[row][col] = True
            for dr, dc in directions:
                r, c = row + dr, col + dc
                # Check if the new position is within bounds and the height condition is met
                if 0 <= r < rows and 0 <= c < cols and not visited[r][c] and heights[r][c] >= heights[row][col]:
                    dfs(r, c, visited)

        # Start DFS for Pacific Ocean (first row and first column)
        for r in range(rows):
            dfs(r, 0, visited_pacific)
        for c in range(cols):
            dfs(0, c, visited_pacific)

        # Start DFS for Atlantic Ocean (last row and last column)
        for r in range(rows):
            dfs(r, cols - 1, visited_atlantic)
        for c in range(cols):
            dfs(rows - 1, c, visited_atlantic)

        # Collect results where both oceans can reach
        result = []
        for r in range(rows):
            for c in range(cols):
                if visited_pacific[r][c] and visited_atlantic[r][c]:
                    result.append([r, c])
        
        return result