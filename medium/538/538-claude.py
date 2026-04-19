from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Time: O(n), Space: O(h) reverse in-order traversal
        self.acc = 0
        def reverse_inorder(node):
            if not node:
                return
            reverse_inorder(node.right)
            self.acc += node.val
            node.val = self.acc
            reverse_inorder(node.left)
        reverse_inorder(root)
        return root
