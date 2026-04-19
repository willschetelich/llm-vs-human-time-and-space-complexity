from functools import lru_cache

class Solution:
    def minDays(self, n: int) -> int:
        # Time: O(log^2 n), Space: O(log^2 n)
        @lru_cache(maxsize=None)
        def dp(n):
            if n <= 1:
                return n
            return 1 + min(n % 2 + dp(n // 2), n % 3 + dp(n // 3))
        return dp(n)
