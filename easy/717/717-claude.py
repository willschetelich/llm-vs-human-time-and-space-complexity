from typing import List

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        # Time: O(n), Space: O(1)
        i = 0
        while i < len(bits) - 1:
            i += 2 if bits[i] == 1 else 1
        return i == len(bits) - 1
