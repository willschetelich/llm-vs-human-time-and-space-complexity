from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # Time: O(n), Space: O(1)
        n = len(nums)
        dup = -1
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                dup = abs(num)
            else:
                nums[idx] = -nums[idx]
        missing = next(i + 1 for i, v in enumerate(nums) if v > 0)
        return [dup, missing]
