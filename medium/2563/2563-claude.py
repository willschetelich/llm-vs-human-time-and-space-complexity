from typing import List
import bisect

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # Time: O(n log n), Space: O(1)
        nums.sort()
        count = 0
        for i in range(len(nums)):
            lo = bisect.bisect_left(nums, lower - nums[i], i+1)
            hi = bisect.bisect_right(nums, upper - nums[i], i+1)
            count += hi - lo
        return count
