from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # Time: O(n), Space: O(n)
        prefix = {0: -1}
        balance = 0
        max_len = 0
        for i, num in enumerate(nums):
            balance += 1 if num == 1 else -1
            if balance in prefix:
                max_len = max(max_len, i - prefix[balance])
            else:
                prefix[balance] = i
        return max_len
