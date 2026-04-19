from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Time: O(n!), Space: O(n^2)
        result = []
        cols = set()
        pos_diag = set()
        neg_diag = set()
        board = [['.']*n for _ in range(n)]

        def backtrack(row):
            if row == n:
                result.append([''.join(r) for r in board])
                return
            for col in range(n):
                if col in cols or (row+col) in pos_diag or (row-col) in neg_diag:
                    continue
                cols.add(col); pos_diag.add(row+col); neg_diag.add(row-col)
                board[row][col] = 'Q'
                backtrack(row+1)
                board[row][col] = '.'
                cols.remove(col); pos_diag.remove(row+col); neg_diag.remove(row-col)

        backtrack(0)
        return result
