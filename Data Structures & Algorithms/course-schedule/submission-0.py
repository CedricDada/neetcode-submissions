class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = collections.defaultdict(list)
        for u,v in prerequisites:
            adj[v].append(u)

        #ordering = []
        visited = set()
        visiting = set() # le chemin en cours d'exploration


        def dfs(at: int) -> bool: # notre fonction retourne true quand il y a un cycle
            if at in visiting:
                return True 
            if at in visited:
                return False
            visiting.add(at)
            for neighbor in adj[at]:
                if dfs(neighbor):
                    return True # cycle détecté, on propage l'erreur
            # le noeud at a été totalement visité
            visiting.remove(at)
            visited.add(at)
            #ordering.append(at)
            return False
                
        

        for at in range(numCourses):
            if at not in visited:
                if dfs(at):
                    return False
        return True
            


