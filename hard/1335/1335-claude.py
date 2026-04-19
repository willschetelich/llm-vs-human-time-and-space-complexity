from typing import List

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        # Time: O(n^2 * d), Space: O(n * d)
        n = len(jobDifficulty)
        if n < d:
            return -1
        INF = float('inf')
        dp = [[INF] * n for _ in range(d)]
        dp[0][0] = jobDifficulty[0]
        for j in range(1, n):
            dp[0][j] = max(dp[0][j-1], jobDifficulty[j])
        for day in range(1, d):
            for j in range(day, n):
                max_diff = jobDifficulty[j]
                for k in range(j, day-1, -1):
                    max_diff = max(max_diff, jobDifficulty[k])
                    if dp[day-1][k-1] != INF:
                        dp[day][j] = min(dp[day][j], dp[day-1][k-1] + max_diff)
        return dp[d-1][n-1] if dp[d-1][n-1] != INF else -1
