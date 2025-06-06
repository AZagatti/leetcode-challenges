# Last updated: 29/05/2025, 21:42:14
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def findBST(node):
            if node is None:
                return None
            if node.val == val:
                return node
            if val > node.val:
                return findBST(node.right)
            if val < node.val:
                return findBST(node.left)

        return findBST(root)
