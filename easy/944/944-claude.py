from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # Time: O(n*m), Space: O(1)
        count = 0
        for col in range(len(strs[0])):
            for row in range(1, len(strs)):
                if strs[row][col] < strs[row-1][col]:
                    count += 1
                    break
        return count
