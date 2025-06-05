# Last updated: 05/06/2025, 19:24:28
'''
-----
Using BFS with queue.
-----
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        queue = deque([root])
        viewed = set()
        while queue:
            node = queue.popleft()
            if k - node.val in viewed:
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            viewed.add(node.val)
        return False