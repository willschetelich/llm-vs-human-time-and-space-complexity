from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Time: O(n+m), Space: O(m) where m=len(nums2)
        stack = []
        nge = {}
        for num in nums2:
            while stack and stack[-1] < num:
                nge[stack.pop()] = num
            stack.append(num)
        return [nge.get(x, -1) for x in nums1]
