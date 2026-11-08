class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_max = 0
        min_buy = float('inf')

        for price in prices:
            # find lowest price before now: set as buy price
            min_buy = min(min_buy, price)
            # calculate profit
            profit = price - min_buy
            # store max of current max and profit
            cur_max = max(profit, cur_max)
        return cur_max
