from typing import *
# 121. Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and 
# choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. 
# If you cannot achieve any profit, return 0.

# Runtime: O(n) Space: O(1)
# Two Pointer Solution
def maxProfit(prices: List[int]) -> int:
    maxProfit = 0
    minPrice = prices[0]
    for price in prices:
        maxProfit = max(maxProfit, price-minPrice)
        minPrice = min(minPrice, price)
    return maxProfit
