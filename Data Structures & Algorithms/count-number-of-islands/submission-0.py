from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        num_islands = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        # Fonction DFS pour explorer toute l'île à partir d'une coordonnée (r, c)
        def dfs(r, c):
            # Conditions d'arrêt : si on sort de la grille, si c'est de l'eau, ou si c'est déjà visité
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0" or (r, c) in visited:
                return
            
            # On marque la case courante comme visitée
            visited.add((r, c))
            
            # On explore les 4 directions : bas, haut, droite, gauche
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Parcours de toute la grille
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    # On a trouvé un nouveau bout de terre non visité = une nouvelle île
                    num_islands += 1
                    # On lance l'exploration pour marquer toute l'île entière
                    dfs(i, j)

        return num_islands