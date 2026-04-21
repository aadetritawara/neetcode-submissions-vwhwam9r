class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute force: O(n^2)

        max_profit = 0

        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[i] < prices[j]:
                    max_profit = max(max_profit, prices[j] - prices[i])

        return max_profit