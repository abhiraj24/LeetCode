class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=99999
        max_profit=0
        for i in prices:
            min_price=min(min_price,i)
            max_profit=max(max_profit,i-min_price)
        return max_profit