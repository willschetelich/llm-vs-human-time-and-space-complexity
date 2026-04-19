from typing import List

class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:
        # Time: O(n), Space: O(1)
        n = len(regular)
        result = [0] * n
        reg_cost = 0
        exp_cost = expressCost

        for i in range(n):
            reg_cost += regular[i]
            exp_cost += express[i]
            result[i] = min(reg_cost, exp_cost + expressCost)
            exp_cost = min(exp_cost, reg_cost + expressCost)
        return result
