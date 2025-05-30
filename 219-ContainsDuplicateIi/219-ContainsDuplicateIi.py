# Last updated: 29/05/2025, 21:42:27
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        for i in range(len(nums)):
            if len(seen) > k:
                seen.remove(nums[i - k - 1])
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        return False