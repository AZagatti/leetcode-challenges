# Last updated: 07/05/2025, 22:23:20
# Recursive.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev_val = float("-inf")
        def inorder_check(node: Optional[TreeNode]) -> bool:
            nonlocal prev_val
            if node is None:
                return True
            if not inorder_check(node.left):
                return False
            if node.val <= prev_val:
                return False
            prev_val = node.val
            if not inorder_check(node.right):
                return False
            return True
        return inorder_check(root)
