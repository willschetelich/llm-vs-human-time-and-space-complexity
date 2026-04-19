from typing import List

class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        # Time: O(n), Space: O(1)
        score = 0
        window = sum(calories[:k])
        if window < lower:
            score -= 1
        elif window > upper:
            score += 1
        for i in range(k, len(calories)):
            window += calories[i] - calories[i - k]
            if window < lower:
                score -= 1
            elif window > upper:
                score += 1
        return score
