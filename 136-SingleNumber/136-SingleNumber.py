# Last updated: 29/05/2025, 21:42:42
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single_num = 0
        for num in nums:
            single_num = single_num ^ num
        return single_num