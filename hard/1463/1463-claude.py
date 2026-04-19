from typing import List

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        # Time: O(m * n^2), Space: O(n^2)
        m, n = len(grid), len(grid[0])
        dp = [[[-1]*n for _ in range(n)] for _ in range(m)]
        dp[0][0][n-1] = grid[0][0] + grid[0][n-1]

        for r in range(1, m):
            ndp = [[[-1]*n for _ in range(n)] for _ in range(m)]
            for c1 in range(n):
                for c2 in range(c1, n):
                    best = -1
                    for dc1 in [-1, 0, 1]:
                        for dc2 in [-1, 0, 1]:
                            pc1, pc2 = c1 - dc1, c2 - dc2
                            if 0 <= pc1 < n and 0 <= pc2 < n and dp[r-1][pc1][pc2] >= 0:
                                best = max(best, dp[r-1][pc1][pc2])
                    if best >= 0:
                        cherries = grid[r][c1] + (grid[r][c2] if c1 != c2 else 0)
                        ndp[r][c1][c2] = best + cherries
            dp = ndp

        return max(dp[m-1][c1][c2] for c1 in range(n) for c2 in range(c1, n) if dp[m-1][c1][c2] >= 0)
