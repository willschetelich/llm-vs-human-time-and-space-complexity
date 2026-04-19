from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        # Time: O(T * L) where T=tree nodes, L=list length, Space: O(T+L)
        def match(tree, lst):
            if not lst:
                return True
            if not tree:
                return False
            if tree.val != lst.val:
                return False
            return match(tree.left, lst.next) or match(tree.right, lst.next)

        def dfs(node):
            if not node:
                return False
            return match(node, head) or dfs(node.left) or dfs(node.right)

        return dfs(root)
