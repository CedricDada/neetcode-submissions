# class Solution:
#     def minCostConnectPoints(self, points: List[List[int]]) -> int:
#         class UnionFind:
#             def __init__(self, n):
#                 self.parent = list(range(n))
#                 self.rank = [0] * n

#             def find(self, i):
#                 if self.parent[i] == i:
#                     return i
#                 self.parent[i] = self.find(self.parent[i])
#                 return self.parent[i]
            
#             def union(self, i, j):
#                 root_i = self.find(i)
#                 root_j = self.find(j)

#                 if root_i != root_j:
#                     if self.rank[root_i] < self.rank[root_j]:
#                         self.parent[root_i] = root_j
#                     elif self.rank[root_i] > self.rank[root_j]:
#                         self.parent[root_j] = root_i
#                     else:
#                         self.parent[root_j] = root_i
#                         self.rank[root_i] += 1
#                     return True
#                 return False
#         def manhattan_distance(i : int, j: int) -> float:
#             return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

#         edges = []
#         for i in range(len(points)):
#             for j in range(i, len(points)):
#                 edges.append((i, j, manhattan_distance(i,j)))
        
#         edges.sort(key = lambda x: x[2])

#         n = len(points)
#         union_find = UnionFind(n)

#         min_cost = 0
#         edges_used = 0
#         # un arbre couvrant de poids minimal contient toujours n-1 arretes pour relier les n sommets

#         for u, v, weight in edges:&
#             if union_find.union(u, v):
#                 min_cost += weight
#                 edges_used += 1

#                 if edges_used==n-1:
#                     break
#         return min_cost if edges_used==n-1 else -1
import heapq
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 0
            
        def manhattan_distance(i: int, j: int) -> int:
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        # Le tas min stocke des tuples (coût_pour_atteindre_le_noeud, index_du_noeud)
        # On démarre au noeud 0 avec un coût de 0
        min_heap = [(0, 0)]
        visited = set()
        min_cost = 0

        # On s'arrête dès que tous les noeuds sont connectés
        while len(visited) < n:
            weight, u = heapq.heappop(min_heap)

            # Si le noeud est déjà dans l'arbre, on l'ignore (filtre anti-cycle)
            if u in visited:
                continue

            # On valide ce noeud et on ajoute le coût à notre total
            visited.add(u)
            min_cost += weight

            # On évalue la distance vers tous les autres noeuds non visités
            for v in range(n):
                if v not in visited:
                    dist = manhattan_distance(u, v)
                    heapq.heappush(min_heap, (dist, v))

        return min_cost