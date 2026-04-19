from typing import List

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # Time: O(1) board is 8x8, Space: O(1)
        for r in range(8):
            for c in range(8):
                if board[r][c] == 'R':
                    count = 0
                    for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                        nr, nc = r + dr, c + dc
                        while 0 <= nr < 8 and 0 <= nc < 8:
                            if board[nr][nc] == 'B':
                                break
                            if board[nr][nc] == 'p':
                                count += 1
                                break
                            nr += dr
                            nc += dc
                    return count
        return 0
