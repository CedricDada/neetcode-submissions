class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
            
        left_border = 0
        right_border = len(matrix[0]) - 1  # -1 pour avoir le vrai index
        top_border = 0
        bottom_border = len(matrix) - 1    # -1 pour avoir le vrai index

        res = []

        # On boucle tant que les murs ne se sont pas croisés
        while left_border <= right_border and top_border <= bottom_border:
            
            # 1. De gauche à droite (sur la bordure haute)
            for j in range(left_border, right_border + 1):
                res.append(matrix[top_border][j])
            top_border += 1  # Le mur du haut descend
            
            # 2. De haut en bas (sur la bordure droite)
            for i in range(top_border, bottom_border + 1):
                res.append(matrix[i][right_border])
            right_border -= 1  # Le mur de droite se décale vers la gauche
            
            # Vérification vitale pour les matrices rectangulaires
            if top_border <= bottom_border:
                # 3. De droite à gauche (sur la bordure basse)
                # Le -1 à la fin du range permet de boucler à l'envers
                for j in range(right_border, left_border - 1, -1):
                    res.append(matrix[bottom_border][j])
                bottom_border -= 1  # Le mur du bas remonte
                
            # Vérification vitale pour les matrices rectangulaires
            if left_border <= right_border:
                # 4. De bas en haut (sur la bordure gauche)
                for i in range(bottom_border, top_border - 1, -1):
                    res.append(matrix[i][left_border])
                left_border += 1  # Le mur de gauche se décale vers la droite

        # Plus besoin de rajouter le centre manuellement !
        return res