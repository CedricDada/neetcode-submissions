from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # CONCEPT 'TWO POINTERS' : On utilise deux indices distincts qui avancent 
        # dans la même direction à des vitesses différentes pour comparer deux valeurs.
        # CONCEPT 'SLIDING WINDOW' : Ces deux pointeurs définissent les bords gauche (l) 
        # et droit (r) d'une "fenêtre" temporelle [l, r] que l'on va faire grandir ou glisser.
        
        l = 0 # Bord gauche de la fenêtre : jour d'achat
        r = 1 # Bord droit de la fenêtre : jour de vente
        max_profit = 0

        while r < len(prices):
            # ÉVALUATION DE LA FENÊTRE : La fenêtre actuelle est-elle valide/profitable ?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                # RÉINITIALISATION DE LA FENÊTRE (Sliding) : 
                # On a trouvé un prix (r) inférieur ou égal à notre prix d'achat (l).
                # Notre fenêtre actuelle [l, r] ne sert plus à rien. On "ferme" l'ancienne 
                # fenêtre et on en ouvre une nouvelle en plaçant le bord gauche sur r.
                l = r
            
            # ÉLARGISSEMENT DE LA FENÊTRE (Expansion) :
            # À chaque itération, on décale le pointeur droit pour agrandir la fenêtre 
            # d'un jour supplémentaire et tester un nouveau prix de vente.
            r += 1
            
        return max_profit