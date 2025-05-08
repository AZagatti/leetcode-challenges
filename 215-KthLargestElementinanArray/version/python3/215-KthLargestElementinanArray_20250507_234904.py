# Last updated: 07/05/2025, 23:49:04
# Good solution using heap queue algorithm.
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for i in range(0, k):
            heappush(min_heap, nums[i])
        for i in range(k, len(nums)):
            if min_heap[0] < nums[i]:
                heappushpop(min_heap, nums[i])
        return min_heap[0]
