from typing import List
from collections import defaultdict
from math import gcd

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # Time: O(n^2), Space: O(n)
        if len(points) <= 2:
            return len(points)
        result = 2
        for i in range(len(points)):
            slopes = defaultdict(int)
            for j in range(len(points)):
                if i == j:
                    continue
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                if dx == 0:
                    slope = (float('inf'), 0)
                else:
                    g = gcd(abs(dx), abs(dy))
                    dx, dy = dx // g, dy // g
                    if dx < 0:
                        dx, dy = -dx, -dy
                    slope = (dy, dx)
                slopes[slope] += 1
            result = max(result, max(slopes.values()) + 1)
        return result
