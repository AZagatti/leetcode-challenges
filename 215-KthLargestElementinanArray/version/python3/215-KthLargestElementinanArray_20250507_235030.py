# Last updated: 07/05/2025, 23:50:30
# Good solution with heap queue algorithm and heapreplace method.
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = nums[:k]
        heapify(min_heap)
        for i in range(k, len(nums)):
            if nums[i] > min_heap[0]:
                heapreplace(min_heap, nums[i])
        return min_heap[0]
