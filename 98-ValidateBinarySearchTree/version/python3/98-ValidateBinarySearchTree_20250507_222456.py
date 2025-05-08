# Last updated: 07/05/2025, 22:24:56
# Recursive.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValidBSTHelper(node, lower_bound, upper_bound):
            if node is None:
                return True
            if node.val <= lower_bound or node.val >= upper_bound:
                return False
            return isValidBSTHelper(node.left, lower_bound, node.val) and isValidBSTHelper(node.right, node.val, upper_bound)
        return isValidBSTHelper(root, float('-inf'), float('inf'))