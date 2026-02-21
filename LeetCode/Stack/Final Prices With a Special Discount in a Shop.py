class Solution:
    def finalPrices(self, prices):
        stack = []  # will store indices

        for i in range(len(prices)):x
            while stack and prices[stack[-1]] >= prices[i]:
                idx = stack.pop()
                prices[idx] -= prices[i]
            stack.append(i)

        return prices