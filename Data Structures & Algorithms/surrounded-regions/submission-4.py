class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
                return
            board[r][c] = 'T'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # checking left and right
        for r in range(rows):
            # left
            if board[r][0] == 'O':
                dfs(r, 0)
            # right
            if board[r][cols - 1] == 'O':
                dfs(r, cols - 1)
        
        # checking top and bottom
        for col in range(cols):
            # top
            if board[0][col] == 'O':
                dfs(0, col)
            # bottom
            if board[rows - 1][col] == 'O':
                dfs(rows - 1, col)
            
        # final pass to update the board
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
                else:
                    board[r][c] = 'X'