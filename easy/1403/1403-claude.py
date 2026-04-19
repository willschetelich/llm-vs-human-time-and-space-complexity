from typing import List

class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        # Time: O(n log n), Space: O(n)
        nums.sort(reverse=True)
        total = sum(nums)
        sub_sum = 0
        for i, num in enumerate(nums):
            sub_sum += num
            if sub_sum > total - sub_sum:
                return nums[:i+1]
        return nums
