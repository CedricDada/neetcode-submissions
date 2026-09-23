class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
            n = len(nums)
            # Initialisation : chaque element est une sequence croissante de taille 1
            dp = [1] * n
            
            # On calcule la reponse pour chaque element i de gauche a droite
            for i in range(1, n):
                # Pour cet element i, on inspecte TOUT l'historique avant lui (j)
                for j in range(i):
                    if nums[j] < nums[i]:
                        # Si nums[i] est plus grand, on peut prolonger la sequence !
                        dp[i] = max(dp[i], dp[j] + 1)
                        
            # La plus longue sequence ne se termine pas forcement au TOUT DERNIER index.
            # Il faut donc prendre le maximum de tout le tableau dp.
            return max(dp)