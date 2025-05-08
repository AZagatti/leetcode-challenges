# Last updated: 07/05/2025, 22:09:50
'''
Good solution.
O(n)
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in cache:
                return [cache[complement], idx]
            cache[num] = idx
        return []
        
        