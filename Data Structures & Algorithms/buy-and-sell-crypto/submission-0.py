class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')
        for i in range(len(prices)):
            current_price = prices[i]
            if current_price < min_price:
                min_price = current_price
            else:
                max_profit = max(max_profit, current_price - min_price)
        return max_profit
        