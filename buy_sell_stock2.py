"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

"""

class Solution:
    def maxProfit(self, prices):
        total_profit = 0
        start_price = prices[0]

        for i in range(len(prices)):
            if start_price < prices[i]:
                total_profit += prices[i]-start_price
            start_price = prices[i]         
        return total_profit
