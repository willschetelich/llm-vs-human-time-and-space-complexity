from typing import List

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # Time: O(m*n), Space: O(1)
        return [[1 ^ x for x in row[::-1]] for row in image]
