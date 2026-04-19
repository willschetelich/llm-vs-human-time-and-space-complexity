from typing import List

class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        # Time: O(n), Space: O(n)
        MOD = 10**9 + 7
        n = len(strength)
        stack = []
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + strength[i]
        prefix_prefix = [0] * (n + 2)
        for i in range(n + 1):
            prefix_prefix[i+1] = prefix_prefix[i] + prefix[i]

        result = 0
        for i in range(n + 1):
            while stack and (i == n or strength[stack[-1]] >= strength[i]):
                mid = stack.pop()
                left = stack[-1] if stack else -1
                right_sum = prefix_prefix[i+1] - prefix_prefix[mid+1]
                left_sum = prefix_prefix[mid+1] - prefix_prefix[left+1]
                right_cnt = i - mid
                left_cnt = mid - left
                contribution = strength[mid] * (right_sum * left_cnt - left_sum * right_cnt)
                result = (result + contribution) % MOD
            stack.append(i)
        return result
