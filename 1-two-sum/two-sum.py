class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in cache:
                return [cache[complement], idx]
            cache[num] = idx
        return []
        
        