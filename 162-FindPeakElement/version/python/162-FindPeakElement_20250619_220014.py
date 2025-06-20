# Last updated: 19/06/2025, 22:00:14
'''
-----
Binary Search for peak element.
-----
'''

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        right = len(nums) - 1
        left = 0
        while left < right:
            mid = (right + left) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left
