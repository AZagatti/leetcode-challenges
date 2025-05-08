# Last updated: 08/05/2025, 00:14:13
# Iterative.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        current_node = root
        while current_node:
            if current_node.val == val:
                return current_node
            if val > current_node.val:
                current_node = current_node.right
            elif val < current_node.val:
                current_node = current_node.left
        return None
