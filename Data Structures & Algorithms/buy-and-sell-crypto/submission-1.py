class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # time: O(n), space: O(1)

        max_profit = 0
        l, r = 0, 1

        while r < len(prices):

            # update left (buy) pointer when right pointer value is smaller
            # because want to buy at lowest possible price
            if prices[r] < prices[l]:
                l = r
            else: # profit made
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            
            r+=1

        return max_profit
