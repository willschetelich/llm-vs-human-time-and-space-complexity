from functools import lru_cache

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        # Time: O(n^4), Space: O(n^3)
        @lru_cache(maxsize=None)
        def dp(a, b):
            if a == b:
                return True
            if sorted(a) != sorted(b):
                return False
            n = len(a)
            for i in range(1, n):
                if (dp(a[:i], b[:i]) and dp(a[i:], b[i:])) or \
                   (dp(a[:i], b[n-i:]) and dp(a[i:], b[:n-i])):
                    return True
            return False
        return dp(s1, s2)
