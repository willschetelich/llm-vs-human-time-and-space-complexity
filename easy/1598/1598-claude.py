from typing import List

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        # Time: O(n), Space: O(1)
        depth = 0
        for log in logs:
            if log == '../':
                depth = max(0, depth - 1)
            elif log != './':
                depth += 1
        return depth
