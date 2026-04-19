from typing import List

class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        # Time: O(m*n*L), Space: O(L)
        rows, cols = len(board), len(board[0])
        rword = word[::-1]
        for r in range(rows):
            for c in range(cols):
                for dr, dc in [(0,1),(1,0)]:
                    # check if this is the start of a slot
                    pr, pc = r - dr, c - dc
                    if 0 <= pr < rows and 0 <= pc < cols and board[pr][pc] != '#':
                        continue
                    # collect the slot
                    cells = []
                    nr, nc = r, c
                    while 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                        cells.append(board[nr][nc])
                        nr += dr; nc += dc
                    if len(cells) != len(word):
                        continue
                    for w in [word, rword]:
                        if all(cells[i] == '.' or cells[i] == w[i] for i in range(len(w))):
                            return True
        return False
