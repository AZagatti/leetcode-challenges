# Last updated: 08/05/2025, 00:09:20
# Recursive.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        temp_left = root.left
        temp_right = root.right
        root.left = temp_right
        root.right = temp_left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
