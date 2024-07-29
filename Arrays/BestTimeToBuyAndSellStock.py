class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min1,max1 = float('inf'),0
        for i in range(len(prices)):
            if min1 > prices[i]:
                min1 = prices[i]
            elif max1 < prices[i] - min1:
                max1 = prices[i] - min1
        return max1