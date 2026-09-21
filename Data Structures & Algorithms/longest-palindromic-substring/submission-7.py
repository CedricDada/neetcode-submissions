# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         dp = [['' for i in range(len(s))] for j in range(len(s))]

#         for i in range(len(s)): 
#             dp[i][i] = s[i]
        
#         for i in range(len(s) - 1, -1, -1):
#             for j in range(i + 1, len(s)):
#                 # Si les bords sont égaux ET que le centre est un palindrome parfait
#                 if s[i] == s[j] and len(dp[i+1][j-1]) == j - i - 1:
#                     dp[i][j] = s[i] + dp[i+1][j-1] + s[j]
#                 else:
#                     # Sinon, on transmet simplement le plus long palindrome trouvé jusque-là
#                     if len(dp[i+1][j]) >= len(dp[i][j-1]):
#                         dp[i][j] = dp[i+1][j]
#                     else:
#                         dp[i][j] = dp[i][j-1]
                        
#         return dp[0][len(s)-1]
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         n = len(s)
#         if n == 0: return ""
        
#         # Représente la ligne i+1 (initialement vide au tout début)
#         ligne_suivante = ['' for _ in range(n)]
        
#         for i in range(n - 1, -1, -1):
#             # On prépare la ligne i
#             ligne_actuelle = ['' for _ in range(n)]
#             ligne_actuelle[i] = s[i]  # L'équivalent de dp[i][i] = s[i]
            
#             for j in range(i + 1, n):
#                 # On utilise ligne_suivante au lieu de dp[i+1] 
#                 # et ligne_actuelle au lieu de dp[i]
#                 if s[i] == s[j] and len(ligne_suivante[j-1]) == j - i - 1:
#                     ligne_actuelle[j] = s[i] + ligne_suivante[j-1] + s[j]
#                 else:
#                     if len(ligne_suivante[j]) >= len(ligne_actuelle[j-1]):
#                         ligne_actuelle[j] = ligne_suivante[j]
#                     else:
#                         ligne_actuelle[j] = ligne_actuelle[j-1]
            
#             # Une fois la ligne i terminée, elle devient la ligne i+1 pour le prochain tour de boucle
#             ligne_suivante = ligne_actuelle
            
#         # À la fin, la réponse se trouve à la fin de notre toute dernière ligne calculée (i=0)
#         return ligne_suivante[n-1]
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        
        # On initialise une matrice N x N remplie de False
        dp = [[False] * n for _ in range(n)]
        
        start = 0
        max_len = 1
        
        # On parcourt toujours i à l'envers
        for i in range(n - 1, -1, -1):
            # On peut commencer j à i (pour inclure les mots d'1 seule lettre)
            for j in range(i, n):
                
                # Un palindrome est valide SI :
                # 1. Les lettres aux extrémités sont égales
                # ET 
                # 2. Le centre est un palindrome (dp[i+1][j-1] == True)
                #    OU la sous-chaîne fait 1, 2 ou 3 lettres (j - i <= 2)
                if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    
                    # Si c'est un palindrome et qu'il est plus long que notre record actuel
                    if j - i + 1 > max_len:
                        max_len = j - i + 1
                        start = i
                        
        # À la toute fin, on découpe la chaîne originale une seule fois
        return s[start:start + max_len]