from typing import List
import heapq

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # Time: O(n log k), Space: O(k)
        heap = []
        cur_max = float('-inf')
        for i, lst in enumerate(nums):
            heapq.heappush(heap, (lst[0], i, 0))
            cur_max = max(cur_max, lst[0])

        best = [heap[0][0], cur_max]
        while True:
            cur_min, i, j = heapq.heappop(heap)
            if cur_max - cur_min < best[1] - best[0]:
                best = [cur_min, cur_max]
            if j + 1 == len(nums[i]):
                break
            next_val = nums[i][j+1]
            heapq.heappush(heap, (next_val, i, j+1))
            cur_max = max(cur_max, next_val)
        return best
