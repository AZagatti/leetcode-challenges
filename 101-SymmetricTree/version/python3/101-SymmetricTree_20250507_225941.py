# Last updated: 07/05/2025, 22:59:41
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True
        stack = [[root.left, root.right]]
        while stack:
            left, right = stack.pop()
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            if left.left or right.right:
                stack.append([left.left, right.right])
            if left.right or right.left:
                stack.append([left.right, right.left])
        return True