from typing import List

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        # Time: O(n), Space: O(1)
        cur_max = nums[0]
        partition_max = nums[0]
        partition = 0
        for i in range(1, len(nums)):
            cur_max = max(cur_max, nums[i])
            if nums[i] < partition_max:
                partition = i
                partition_max = cur_max
        return partition + 1
