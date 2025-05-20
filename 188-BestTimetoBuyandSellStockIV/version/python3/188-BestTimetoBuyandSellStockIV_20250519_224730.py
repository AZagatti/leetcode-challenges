# Last updated: 19/05/2025, 22:47:30
'''
-----
Dynamic Programming, without otimization for k elements.
-----
'''

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        buy = [float('-inf')] * k
        sell = [0] * k
        for price in prices:
            for j in range(k):
                previous_sell_profit_for_buy = sell[j-1] if j > 0 else 0
                buy[j] = max(buy[j], previous_sell_profit_for_buy - price)
                sell[j] = max(sell[j], buy[j] + price)
        return sell[k-1]