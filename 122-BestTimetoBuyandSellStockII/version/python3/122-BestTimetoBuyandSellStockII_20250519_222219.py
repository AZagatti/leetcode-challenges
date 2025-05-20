# Last updated: 19/05/2025, 22:22:19
'''
-----
Dynamic Programming with if statement, more performative.
-----
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1 = float('-inf')
        sell1 = 0
        buy2 = float('-inf')
        sell2 = 0
        for price in prices:
            if buy1 < -price:
                buy1 = -price
            if sell1 < buy1 + price:
                sell1 = buy1 + price
            if buy2 < sell1 - price:
                buy2 = sell1 - price
            if sell2 < buy2 + price:
                sell2 = buy2 + price
        return sell2
