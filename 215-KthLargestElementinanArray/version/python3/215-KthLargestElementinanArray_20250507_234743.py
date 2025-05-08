# Last updated: 07/05/2025, 23:47:43
# Bad solution using nlargest.
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums
        heapify(heap)
        min_heap = nlargest(k, heap)
        return min_heap[-1]
