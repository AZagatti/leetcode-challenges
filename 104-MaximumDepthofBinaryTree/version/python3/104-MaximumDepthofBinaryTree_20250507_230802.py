# Last updated: 07/05/2025, 23:08:02
# Iterative with dequeue (popleft is O(1)).
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
        depth = 0
        queue = deque([root])
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                item = queue.popleft()
                if not item:
                    break
                if item.left:
                    queue.append(item.left)
                if item.right:
                    queue.append(item.right)
            depth += 1
        return depth
