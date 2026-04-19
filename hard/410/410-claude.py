from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # Time: O(n log(sum)), Space: O(1)
        def can_split(max_sum):
            parts, curr = 1, 0
            for num in nums:
                curr += num
                if curr > max_sum:
                    parts += 1
                    curr = num
            return parts <= k

        lo, hi = max(nums), sum(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if can_split(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
