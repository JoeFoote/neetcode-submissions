class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_b = 101
        max_profit = 0
        l = 0
        for r in range(len(prices)):
            if prices[r] < min_b:
                l = r
                min_b = prices[r]
            max_profit = max(max_profit, prices[r] - prices[l])
        return(max_profit)


