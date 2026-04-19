from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Time: O(log n) average, O(n) worst with duplicates, Space: O(1)
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            elif nums[mid] < nums[hi]:
                hi = mid
            else:
                hi -= 1
        return nums[lo]
