from typing import List
from functools import reduce
import operator

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # Time: O(n), Space: O(1)
        # OR of all elements times 2^(n-1)
        return reduce(operator.or_, nums) * (1 << (len(nums) - 1))
