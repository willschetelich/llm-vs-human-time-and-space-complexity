from typing import List
from collections import Counter

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        # Time: O(1) bounded by 100-999 range, Space: O(1)
        count = Counter(digits)
        result = []
        for num in range(100, 1000, 2):
            c = Counter([num // 100, (num // 10) % 10, num % 10])
            if all(c[d] <= count[d] for d in c):
                result.append(num)
        return result
