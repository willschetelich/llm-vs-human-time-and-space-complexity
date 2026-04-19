from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # Time: O(n^2 * m) where m=num rows, Space: O(n)
        n = len(strs[0])
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if all(strs[r][j] <= strs[r][i] for r in range(len(strs))):
                    dp[i] = max(dp[i], dp[j] + 1)
        return n - max(dp)
