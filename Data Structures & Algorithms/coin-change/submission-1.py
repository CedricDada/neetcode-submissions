class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        dp[0] = 0
        # dp[i] représente le nombre de pièces pour obtenir l'amount = i
        for coin in coins:
            for s in range (amount + 1 - coin):
                if dp[s] >= 0:
                    dp[s+coin] = min(dp[s+coin], dp[s] + 1) if dp[s+coin]>0 else dp[s]+1
        

        return dp[amount]