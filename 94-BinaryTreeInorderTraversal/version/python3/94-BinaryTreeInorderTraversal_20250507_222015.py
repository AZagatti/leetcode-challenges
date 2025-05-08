# Last updated: 07/05/2025, 22:20:15
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        current_node = root
        stack = []
        while current_node is not None or stack:
            while current_node is not None:
                stack.append(current_node)
                current_node = current_node.left
            last_node = stack.pop()
            result.append(last_node.val)
            current_node = last_node.right
        return result