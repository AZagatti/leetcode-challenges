# Last updated: 19/05/2025, 19:43:00
'''
-----
Iterative with 'min' and 'max', worst performance.
-----
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price_so_far = float('inf')
        max_profit_so_far = 0
        for price in prices:
            min_price_so_far = min(min_price_so_far, price)
            max_profit_so_far = max(max_profit_so_far, price - min_price_so_far)
        return max_profit_so_far