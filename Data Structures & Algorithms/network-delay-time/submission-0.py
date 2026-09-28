import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #il s'agit d'appliquer l'algo de dijkstra entre le noeud k et tous les autres noeuds

        shortest_paths = {}

        for i in range(1, n+1):
            shortest_paths[i] = float('inf')
        shortest_paths[k] = 0 # car le noeud k est notre noeud initial

        visited = set()

        min_heap = [(0, k)] #on va pousser progressivement des valeurs de la forme (weight to attend k, k)

        while min_heap:
            weight, i = heapq.heappop(min_heap)
            if i in visited:
                continue

            # cherchons tous les noeuds atteignables par le noeud i
            for j in range(len(times)):
                uj, vj, tj = times[j][0], times[j][1], times[j][2]
                if i == uj:
                    heapq.heappush(min_heap, (weight+tj, vj))
            visited.add(i)
            shortest_paths[i] = weight
        # je dois retourner le maximum de shortest_paths
        res = max(shortest_paths.values())
        if res == float('inf'):
            return -1
        return res