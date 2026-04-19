from typing import List
from collections import Counter

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        # Time: O(n * sqrt(max_num)), Space: O(max_num)
        parent = list(range(max(nums) + 1))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            parent[find(x)] = find(y)

        for num in nums:
            d = 2
            while d * d <= num:
                if num % d == 0:
                    union(num, d)
                    union(num, num // d)
                d += 1

        count = Counter(find(num) for num in nums)
        return max(count.values())
