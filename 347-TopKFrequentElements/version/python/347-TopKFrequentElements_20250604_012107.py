# Last updated: 04/06/2025, 01:21:07
'''
-----
Using built-in Counter and heapq.nlargest.
-----
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)
