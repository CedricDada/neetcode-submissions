from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        stack = [] # Va stocker les indices (pour calculer la largeur)
        total_water = 0
        
        for i in range(len(height)):
            # On a trouvé un mur droit qui ferme potentiellement une cuvette
            while stack and height[i] > height[stack[-1]]:
                # Le point le plus bas de la cuvette
                bottom_index = stack.pop()
                
                # S'il n'y a pas de mur à gauche pour retenir l'eau, elle s'écoule
                if not stack:
                    break
                    
                # L'index du mur gauche est maintenant au sommet de la pile
                left_index = stack[-1]
                
                # Largeur entre le mur gauche et le mur droit actuel
                width = i - left_index - 1
                
                # La hauteur d'eau retenue est le minimum des deux murs moins la hauteur du fond
                bounded_height = min(height[left_index], height[i]) - height[bottom_index]
                
                # Ajout du volume d'eau de cette cuvette horizontale
                total_water += width * bounded_height
                
            # On ajoute l'index actuel à la pile décroissante
            stack.append(i)
            
        return total_water