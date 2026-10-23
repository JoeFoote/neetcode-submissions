class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0      # Cutoff for profit is 0
        l = 0           # left side of window
        r = 1           # right side of window
        while (r < len(prices)):
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)
            if prices[r] < prices[l]:
                l = r
            r += 1
        return(max_profit)


