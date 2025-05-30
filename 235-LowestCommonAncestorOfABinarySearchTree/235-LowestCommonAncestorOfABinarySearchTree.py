# Last updated: 29/05/2025, 21:42:24
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find_lca(node):
            if node is None:
                return None
            if p.val > node.val and q.val > node.val:
                return find_lca(node.right)
            if p.val < node.val and q.val < node.val:
                return find_lca(node.left)
            return node
        return find_lca(root)