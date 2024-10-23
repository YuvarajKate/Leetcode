class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Dimensions of the grid
        rows, cols = len(grid), len(grid[0])
        # Queue for BFS
        queue = deque()
        # Count fresh oranges and add rotten ones to the queue
        fresh_oranges = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))  # (row, col, minutes)
                elif grid[r][c] == 1:
                    fresh_oranges += 1
        # If there are no fresh oranges, return 0
        if fresh_oranges == 0:
            return 0
        # BFS directions: up, down, left, right
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # BFS traversal
        minutes_passed = 0
        while queue:
            row, col, minutes_passed = queue.popleft()  
            # Explore all 4 directions
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                # Check if the new cell is within bounds and is a fresh orange
                if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1:
                    # This fresh orange becomes rotten
                    grid[new_row][new_col] = 2
                    fresh_oranges -= 1
                    queue.append((new_row, new_col, minutes_passed + 1))
        # If there are no fresh oranges left, return the time elapsed
        if fresh_oranges == 0:
            return minutes_passed
        else:
            return -1  # There are still fresh oranges left that can't be reached
