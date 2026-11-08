class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # naive approach
        # keep track of max, initial value = 0
        cur_max = 0
        # loop through each price
        for buy_pr_idx in range(len(prices)):
            # another loop through every price after that price
            for sell_pr_idx in range(buy_pr_idx, len(prices)):
        
                # calculate profit
                profit = prices[sell_pr_idx]-prices[buy_pr_idx]
                # max(profit, current_max)
                cur_max = max(cur_max, profit)

        return cur_max
