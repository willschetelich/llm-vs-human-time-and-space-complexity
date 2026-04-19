from typing import List
from collections import deque

class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        # Time: O(2^(m*n) * m*n), Space: O(2^(m*n))
        m, n = len(mat), len(mat[0])
        def to_int(grid):
            result = 0
            for r in range(m):
                for c in range(n):
                    result = result * 2 + grid[r][c]
            return result

        start = to_int(mat)
        if start == 0:
            return 0

        def flip(state, r, c):
            for dr, dc in [(0,0),(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < m and 0 <= nc < n:
                    state ^= (1 << (nr*n + nc))
            return state

        visited = {start}
        queue = deque([(start, 0)])
        while queue:
            state, steps = queue.popleft()
            for r in range(m):
                for c in range(n):
                    nxt = flip(state, r, c)
                    if nxt == 0:
                        return steps + 1
                    if nxt not in visited:
                        visited.add(nxt)
                        queue.append((nxt, steps+1))
        return -1
