class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_len = len(board)
        col_len = len(board[0])

        row_set = set()
        col_set = set()
        block_set = set()

        for r in range(row_len):
            for c in range(col_len):
                val = board[r][c] 
                if val == '.':
                    continue

                row_key = ("row",r,val)
                col_key = ("col",c,val)
                block_key = ("block",r // 3, c // 3,val)

                if (row_key in row_set) or (col_key in col_set) or (block_key in block_set):
                    return False
                
                row_set.add(row_key)
                col_set.add(col_key)
                block_set.add(block_key)
            
        return True