# Last updated: 29/05/2025, 21:42:26
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)