class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
            
        n = len(s)
        # On ajoute une case supplémentaire au début pour gérer dp[i-2] facilement
        # dp[i] représente le nombre de façons de décoder les i premiers caractères
        dp = [0] * (n + 1) 
        
        dp[0] = 1 # Chaine vide (utile pour les maths de dp[i-2])
        dp[1] = 1 # Le premier caractère (déjà vérifié qu'il n'est pas "0")

        for i in range(2, n + 1):
            # 1. Décodage d'un seul caractère (s[i-1])
            # Valide si le caractère courant n'est pas '0'
            if s[i-1] != "0":
                dp[i] += dp[i-1]
                
            # 2. Décodage de deux caractères (s[i-2:i])
            # Valide si le nombre formé est entre 10 et 26
            two_digits = int(s[i-2:i])
            if 10 <= two_digits <= 26:
                dp[i] += dp[i-2]
                
        return dp[n]