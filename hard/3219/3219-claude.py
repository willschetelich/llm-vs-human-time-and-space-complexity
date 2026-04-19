from typing import List

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        # Time: O(m log m + n log n), Space: O(1)
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)
        h_idx = v_idx = 0
        h_pieces = v_pieces = 1
        total = 0
        while h_idx < len(horizontalCut) or v_idx < len(verticalCut):
            h_cost = horizontalCut[h_idx] if h_idx < len(horizontalCut) else -1
            v_cost = verticalCut[v_idx] if v_idx < len(verticalCut) else -1
            if h_cost >= v_cost:
                total += h_cost * v_pieces
                h_pieces += 1
                h_idx += 1
            else:
                total += v_cost * h_pieces
                v_pieces += 1
                v_idx += 1
        return total
