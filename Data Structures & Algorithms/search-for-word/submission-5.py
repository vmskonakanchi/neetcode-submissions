class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        seen = set()

        def found(r,c,idx):
            if idx == len(word):
                return True

            # bounds check
            if (r < 0 or r >= rows) or (c >= cols or c < 0):
                return False

            if board[r][c] != word[idx]:
                return False

            if (r,c) in seen:
                return False

            seen.add((r,c))
            res = (
                found(r + 1,c, idx + 1) or
                found(r - 1,c, idx + 1) or
                found(r,c + 1, idx + 1) or
                found(r,c - 1, idx + 1)
            )
            seen.remove((r,c))

            return res

        for r in range(rows):
            for c in range(cols):
                if found(r,c,0):
                    return True
        
        return False