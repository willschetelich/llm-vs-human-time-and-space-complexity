from typing import List
from collections import defaultdict
from math import gcd

class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        # Time: O(n), Space: O(n)
        ratio_count = defaultdict(int)
        result = 0
        for w, h in rectangles:
            g = gcd(w, h)
            ratio = (w // g, h // g)
            result += ratio_count[ratio]
            ratio_count[ratio] += 1
        return result
