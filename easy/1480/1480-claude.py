from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # Time: O(n), Space: O(1) excluding output
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums
