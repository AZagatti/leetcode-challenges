# Last updated: 29/05/2025, 21:42:52
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        result = []
        current_node = root
        stack = []
        while current_node is not None or stack:
            while current_node is not None:
                stack.append(current_node)
                current_node = current_node.left
            last_node = stack.pop()
            if result and last_node.val <= result[-1]:
                return False
            result.append(last_node.val)
            current_node = last_node.right
        return True