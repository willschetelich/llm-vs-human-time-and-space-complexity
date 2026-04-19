from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Time: O(n), Space: O(h)
        dummy = TreeNode()
        self.cur = dummy
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            node.left = None
            self.cur.right = node
            self.cur = node
            inorder(node.right)
        inorder(root)
        return dummy.right
