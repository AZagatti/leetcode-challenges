# Last updated: 04/06/2025, 01:32:29
'''
-----
Using sorting.
-----
'''

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]
