class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] est True si s[:i] (les i premiers caractères) peut être décomposé
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True

        for i in range(len(s)):
            # Si on a pu arriver jusqu'à l'index i en formant des mots valides
            if dp[i]:
                for word in wordDict:
                    # On vérifie qu'on ne dépasse pas la taille de 's' 
                    # ET que la sous-chaîne correspond au mot
                    if i + len(word) <= len(s) and s[i : i + len(word)] == word:
                        dp[i + len(word)] = True
                        
        # On renvoie la dernière case qui indique si TOUTE la chaîne est valide
        return dp[-1]