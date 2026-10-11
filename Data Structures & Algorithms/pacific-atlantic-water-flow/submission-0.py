class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        pacific_set = set()
        atlantic_set = set()
        
        ROWS, COLS = len(heights), len(heights[0])

        # On passe le set de l'océan au DFS pour savoir lequel on est en train de remplir
        def dfs(r, c, ocean_set):
            ocean_set.add((r, c))
            
            # On vérifie les 4 directions de manière plus propre
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Si le voisin est dans les limites,
                # qu'il n'a pas encore été visité par cet océan,
                # et que sa hauteur est supérieure ou égale (l'eau peut descendre vers nous)
                if (0 <= nr < ROWS and 0 <= nc < COLS and 
                    (nr, nc) not in ocean_set and 
                    heights[nr][nc] >= heights[r][c]):
                    
                    dfs(nr, nc, ocean_set)

        # 1. Lancer le DFS depuis les bords Gauche (Pacifique) et Droit (Atlantique)
        for i in range(ROWS):
            dfs(i, 0, pacific_set)
            dfs(i, COLS - 1, atlantic_set)
            
        # 2. Lancer le DFS depuis les bords Haut (Pacifique) et Bas (Atlantique)
        for j in range(COLS):
            dfs(0, j, pacific_set)
            dfs(ROWS - 1, j, atlantic_set)

        # 3. Le résultat est l'intersection exacte des deux sets (les cases touchées par les deux)
        # On retourne sous forme de liste de listes car c'est ce que LeetCode attend.
        return [list(coord) for coord in (pacific_set & atlantic_set)]