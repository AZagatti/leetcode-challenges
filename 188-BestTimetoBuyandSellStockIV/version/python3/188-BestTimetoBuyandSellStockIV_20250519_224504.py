# Last updated: 19/05/2025, 22:45:04
'''
-----
Dynamic Programming with max.
-----
'''

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if k >= n // 2:
            max_profit_unlimited = 0
            for i in range(1, n):
                if prices[i] > prices[i-1]:
                    max_profit_unlimited += prices[i] - prices[i-1]
            return max_profit_unlimited

        buy = [float('-inf')] * k
        sell = [0] * k
        for price in prices:
            for j in range(k):
                previous_sell_profit_for_buy = sell[j-1] if j > 0 else 0
                buy[j] = max(buy[j], previous_sell_profit_for_buy - price)
                sell[j] = max(sell[j], buy[j] + price)
        return sell[k-1]