class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price_seen = prices[0]
        max_profit = 0

        for price in prices:
            min_price_seen = min(min_price_seen, price)
            max_profit = max(max_profit, price - min_price_seen)    

        return max_profit