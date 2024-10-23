class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False

        rows, cols = len(board), len(board[0])

        # Directions for moving up, down, left, right
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(r: int, c: int, index: int) -> bool:
            if index == len(word):  # Found the word
                return True
            
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]:
                return False
            
            # Mark the cell as visited by using a placeholder
            temp = board[r][c]
            board[r][c] = '#'  # Placeholder to mark as visited

            # Explore all possible directions
            for dr, dc in directions:
                if dfs(r + dr, c + dc, index + 1):
                    return True
            
            # Restore the original value after exploring
            board[r][c] = temp

            return False

        # Check each cell as a starting point for the DFS
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:  # Only start if the first letter matches
                    if dfs(r, c, 0):
                        return True
        
        return False