# Last updated: 19/05/2025, 21:50:13
'''
-----
Greedy Algorithm.
-----
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        ma = []
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                max_profit += prices[i + 1] - prices[i]
        return max_profit
