# Last updated: 29/05/2025, 21:42:34
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        def dfs(node, level):
            if node is None:
                return
            if len(result) == level:    
                result.append(node.val)
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)
        dfs(root, 0)
        return result
        