from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        # Time: O(n), Space: O(h)
        self.res = 0
        def dfs(node, parent_val, length):
            if not node:
                return
            length = length + 1 if parent_val is not None and node.val == parent_val + 1 else 1
            self.res = max(self.res, length)
            dfs(node.left, node.val, length)
            dfs(node.right, node.val, length)
        dfs(root, None, 0)
        return self.res
