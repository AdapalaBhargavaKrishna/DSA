class Solution(object):
    def maxProfit(self, prices):
        min_price = float('inf')
        max_price = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_price:
                max_price = price - min_price

        return max_price
    
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.