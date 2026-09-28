import collections
from typing import List

class UnionFind():
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        # Astuce : On peut compter les composantes directement ici !
        # Au début, chaque noeud est sa propre composante, donc on en a 'n'.
        self.components_count = n

    def find(self, i: int) -> int:
        if self.parent[i] == i:
            return i
        
        # Optimisation cruciale : Path Compression (Compression de chemin)
        # Au lieu de juste retourner self.find(self.parent[i]), 
        # on met à jour le parent pour pointer directement vers la racine absolue.
        # Cela aplatit l'arbre et rend les futurs find() beaucoup plus rapides.
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> bool:
        parent_i = self.find(i)
        parent_j = self.find(j)
        
        if parent_i == parent_j:
            return True
            
        if self.rank[parent_i] < self.rank[parent_j]:
            self.parent[parent_i] = parent_j
        elif self.rank[parent_i] > self.rank[parent_j]:
            self.parent[parent_j] = parent_i
        else:
            self.parent[parent_i] = parent_j
            self.rank[parent_j] += 1
            
        # À chaque fois qu'on relie deux composantes distinctes, 
        # le nombre total de composantes diminue de 1.
        self.components_count -= 1
        return False

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Pas besoin de créer un dictionnaire d'adjacence 'adj' avec l'algo Union-Find.
        uf = UnionFind(n)
        
        # On itère SIMPLEMENT sur la liste des arêtes fournies.
        # Plus besoin de visited_pairs ni de double boucle for i, for j.
        for u, v in edges:
            uf.union(u, v)

        return uf.components_count