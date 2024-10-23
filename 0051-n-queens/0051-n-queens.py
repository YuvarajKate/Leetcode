class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(row: int):
            if row == n:  # All queens are placed successfully
                result.append(["".join(row) for row in board])
                return
            
            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue  # This column or diagonal is under attack
                
                # Place the queen
                board[row][col] = 'Q'
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                
                # Move to the next row
                backtrack(row + 1)
                
                # Remove the queen and backtrack
                board[row][col] = '.'
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        result = []
        board = [['.'] * n for _ in range(n)]  # Initialize the board
        cols = set()  # Columns where queens are placed
        diag1 = set()  # Major diagonals (row - col)
        diag2 = set()  # Minor diagonals (row + col)

        backtrack(0)  # Start from the first row
        return result