# Last updated: 19/05/2025, 19:46:55
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price_so_far = float('inf')
        max_profit_so_far = 0
        for price in prices:
            if price < min_price_so_far:
                min_price_so_far = price
            sell_price = price - min_price_so_far
            if sell_price > max_profit_so_far:
                max_profit_so_far = sell_price
        return max_profit_so_far