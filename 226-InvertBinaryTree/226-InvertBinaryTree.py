# Last updated: 29/05/2025, 21:42:25
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
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                temp_left = node.left
                node.left = node.right
                node.right = temp_left
                queue.append(node.left)
                queue.append(node.right)
        return root