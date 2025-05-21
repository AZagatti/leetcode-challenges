# Last updated: 21/05/2025, 20:04:41
'''
-----
Bit Manipulation using XOR(^).
-----
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single_num = 0
        for num in nums:
            single_num = single_num ^ num
        return single_num