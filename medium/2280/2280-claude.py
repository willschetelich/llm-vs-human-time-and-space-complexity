from typing import List

class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        # Time: O(n log n), Space: O(1)
        stockPrices.sort()
        if len(stockPrices) == 1:
            return 0
        lines = 1
        for i in range(2, len(stockPrices)):
            x0, y0 = stockPrices[i-2]
            x1, y1 = stockPrices[i-1]
            x2, y2 = stockPrices[i]
            # Check collinearity using cross product to avoid float
            if (y1 - y0) * (x2 - x1) != (y2 - y1) * (x1 - x0):
                lines += 1
        return lines
