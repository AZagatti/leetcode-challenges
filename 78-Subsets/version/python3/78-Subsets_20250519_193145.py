# Last updated: 19/05/2025, 19:31:45
'''
-----
Iterative with Dynamic Programming.
-----
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price_so_far = float('inf')
        max_profit_so_far = 0
        for price in prices:
            if min_price_so_far > price:
                min_price_so_far = price
                continue
            sell_price = price - min_price_so_far
            if sell_price > max_profit_so_far:
                max_profit_so_far = sell_price
                continue
        return max_profit_so_far