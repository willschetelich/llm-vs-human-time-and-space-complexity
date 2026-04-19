from typing import List, Union

class Solution:
    def lastVisitedIntegers(self, nums: List[Union[int, str]]) -> List[int]:
        # Time: O(n), Space: O(n)
        seen = []
        result = []
        k = 0
        for x in nums:
            if x == "seen":
                k += 1
                result.append(seen[-k] if k <= len(seen) else -1)
            else:
                seen.append(x)
                k = 0
        return result
