class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = float('inf')
        max_p = 0
        for i in range(len(prices)):
            if prices[i] < min:
                min = prices[i]
            elif prices[i] - min > max_p:
                max_p = prices[i] - min
        return max_p
                
        