"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
""" 

class Solution:
    def maxProfit(self, prices):
        profit = 0
        buy_price = prices[0]
        for current_price in prices[1:]:
            if buy_price > current_price:
                buy_price = current_price

            profit = max(profit, current_price - buy_price)
        return profit
