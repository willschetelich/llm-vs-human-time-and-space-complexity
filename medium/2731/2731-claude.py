from typing import List

class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        # Time: O(n log n), Space: O(n)
        MOD = 10**9 + 7
        positions = []
        for i, (pos, direction) in enumerate(zip(nums, s)):
            positions.append(pos + d if direction == 'R' else pos - d)
        positions.sort()
        total = 0
        prefix = 0
        for i, p in enumerate(positions):
            total += i * p - prefix
            prefix += p
        return total % MOD
