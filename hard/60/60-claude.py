import math
from typing import List

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # Time: O(n^2), Space: O(n)
        digits = list(range(1, n+1))
        k -= 1
        result = []
        for i in range(n, 0, -1):
            f = math.factorial(i-1)
            idx = k // f
            result.append(str(digits[idx]))
            digits.pop(idx)
            k %= f
        return ''.join(result)
