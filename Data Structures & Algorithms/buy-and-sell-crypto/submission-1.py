class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price_seen = float('inf') 
        max_profit = 0

        for price in prices:
            max_profit = max(max_profit, price - min_price_seen)    
            min_price_seen = min(min_price_seen, price)

        return max_profit