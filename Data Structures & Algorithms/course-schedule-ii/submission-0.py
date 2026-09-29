class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)

        for u,v in prerequisites:
            adj[u].append(v)
        
        visited = set() # les noeuds totolement visités (memes leurs voisins ont aussi été visités)
        visiting = set() # les noeuds en cours de visite
        ordering = []

        def dfs(at : int) -> bool: # retourne True quand il y a un cycle et False sinon
            if at in visited:
                return False
            if at in visiting:
                return True
            
            visiting.add(at)

            for neighbor in adj[at]:
                if dfs(neighbor):
                    return True # on est tombé sur un cycle et donc je propage l'erreur 

            visiting.remove(at)
            visited.add(at)  
            ordering.append(at)

        for at in range(numCourses):
            if at not in visited:
                if dfs(at):
                    return []
        return ordering
        