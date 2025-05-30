# Last updated: 29/05/2025, 21:42:49
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        max_depth_right = self.maxDepth(root.right)
        max_depth_left = self.maxDepth(root.left)
        return 1 + max(max_depth_right, max_depth_left)
