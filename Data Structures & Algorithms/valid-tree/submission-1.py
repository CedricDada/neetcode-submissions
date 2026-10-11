import collections
from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Un arbre valide doit avoir exactement n - 1 arêtes
        if len(edges) != n - 1:
            return False

        adj = collections.defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()
        
        # On ajoute un paramètre 'prev' pour se souvenir d'où l'on vient
        def dfs(i, prev):
            if i in visited:
                return False
            
            visited.add(i)
                
            for neighbor in adj[i]:
                # On ignore le nœud dont on vient d'arriver
                if neighbor == prev:
                    continue
                # Si un appel récursif détecte un cycle, on remonte l'erreur
                if not dfs(neighbor, i):
                    return False
            
            return True

        # On lance le DFS depuis le nœud 0, avec -1 comme faux "parent" de départ
        if not dfs(0, -1):
            return False
            
        # On vérifie que tous les nœuds ont bien été visités (graphe totalement connecté)
        return len(visited) == n