class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Time: O(n), Space: O(n)
        stack = [-1]
        result = 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    result = max(result, i - stack[-1])
        return result
