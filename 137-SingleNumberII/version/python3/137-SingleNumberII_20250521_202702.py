# Last updated: 21/05/2025, 20:27:02
'''
-----
Bit Manipulation.
-----
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single_num = 0
        for i in range(32):
            current_bit_sum = 0
            for num in nums:
                bit = num >> i & 1
                if bit == 1:
                    current_bit_sum += 1
            if current_bit_sum % 3 == 1:
                single_num = single_num | (1 << i)
        if single_num >= 2**31:
            single_num -= 2**32
        return single_num
