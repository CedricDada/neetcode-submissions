import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # La vitesse min est 1, la max est la plus grosse pile
        gauche, droite = 1, max(piles)
        res = droite
        
        while gauche <= droite:
            k = (gauche + droite) // 2
            
            # Calcul du temps total pour la vitesse k
            temps_total = 0
            for pile in piles:
                temps_total += math.ceil(pile / k)
                
            # Si on met moins ou exactement h heures, k est valide.
            # Mais on essaie de trouver un k encore plus petit (vers la gauche)
            if temps_total <= h:
                res = k
                droite = k - 1
            # Si ça prend trop de temps, il faut manger plus vite (vers la droite)
            else:
                gauche = k + 1
                
        return res