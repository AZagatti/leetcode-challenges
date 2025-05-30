# Last updated: 29/05/2025, 21:42:39
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        turtle = head
        hare = head
        while hare is not None and hare.next is not None:
            turtle = turtle.next
            hare = hare.next.next
            if turtle == hare:
                return True
        return False

