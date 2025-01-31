class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_value = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            # print(i, buy_value, profit)
            if prices[i]<buy_value:
                buy_value = prices[i]
            elif prices[i]-buy_value>profit:
                profit = prices[i]-buy_value
        return profit
