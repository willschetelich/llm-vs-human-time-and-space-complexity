from typing import List

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # Time: O(4^(m*n)), Space: O(m*n)
        m, n = len(grid), len(grid[0])
        start = end = None
        empty = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] != -1:
                    empty += 1
                if grid[r][c] == 1:
                    start = (r, c)
                elif grid[r][c] == 2:
                    end = (r, c)

        self.result = 0
        def dfs(r, c, count):
            if (r, c) == end:
                if count == empty:
                    self.result += 1
                return
            tmp = grid[r][c]
            grid[r][c] = -1
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != -1:
                    dfs(nr, nc, count+1)
            grid[r][c] = tmp

        dfs(start[0], start[1], 1)
        return self.result
