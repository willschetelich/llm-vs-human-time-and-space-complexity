from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Time: O(n log n), Space: O(n)
        return [name for _, name in sorted(zip(heights, names), reverse=True)]
