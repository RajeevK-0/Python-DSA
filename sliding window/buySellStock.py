class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        mx = float('inf')
        for i in range(len(prices)):
            mx = min(mx,prices[i])
            prof = prices[i]-mx
            profit = max(profit,prof)
        return profit