# Last updated: 29/05/2025, 21:42:29
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = nums[:k]
        heapify(min_heap)
        for i in range(k, len(nums)):
            if nums[i] > min_heap[0]:
                heapreplace(min_heap, nums[i])
        return min_heap[0]
