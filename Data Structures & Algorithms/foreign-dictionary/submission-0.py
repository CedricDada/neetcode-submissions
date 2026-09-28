import collections
from typing import List, Dict

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        # pour résoudre ce problème il nous suffira de créer un graphe entre les différents caractères, 
        # en se basant sur les positions des différents éléments du tableau words
        adj = collections.defaultdict(list)
        for w in words:
            for c in w:
                adj[c] # Astuce parfaite : crée la clé avec une liste vide pour chaque caractère existant
        
        # tracons les edges de notre graphe
        for i in range(len(words)-1):
            # on exploite le fait que le mot i < mot i+1 lexicographiquement
            word, next_word = words[i], words[i+1]
            
            # Gérer le cas où un mot plus long précède un préfixe plus court (invalide)
            # Ex: "apple" avant "app" n'est pas logique dans un dictionnaire
            min_len = min(len(word), len(next_word))
            if len(word) > len(next_word) and word[:min_len] == next_word[:min_len]:
                return ""
            
            # Itérer seulement jusqu'à la longueur du mot le plus court
            for j in range(min_len):
                if word[j] != next_word[j]:
                    adj[word[j]].append(next_word[j])
                    # Il est crucial de s'arrêter dès la première différence trouvée !
                    break 

        # faisons un tri topologique de notre graphe 
        # Utilisation de deux sets pour détecter les cycles (indispensable)
        visited = set() # Garde la trace des noeuds totalement traités
        path = set()    # Garde la trace des noeuds DANS LE CHEMIN ACTUEL du DFS (pour repérer un cycle)
        
        ordering = []
        
        # La fonction DFS doit être définie AVANT de s'en servir
        def dfs(at: str) -> bool:
            # Si le noeud est dans le chemin actuel, on a fait une boucle (Cycle !)
            if at in path:
                return True
            # Si le noeud a déjà été traité avec succès, on passe
            if at in visited:
                return False
                
            # On marque le noeud comme étant "en cours d'exploration"
            path.add(at)
            
            for neighbor in adj[at]:
                if dfs(neighbor):
                    return True # Propage l'erreur de cycle vers le haut
            
            # On a fini d'explorer ce noeud, on le retire du chemin et on le marque comme terminé
            path.remove(at)
            visited.add(at)
            # On l'ajoute à la liste. Comme on est en DFS "Post-Order", le résultat sera inversé
            ordering.append(at)
            return False

        # On itère sur les noeuds du graphe (adj), pas sur visited qui est vide
        for at in adj.keys():
            if dfs(at):
                return "" # Si un cycle est détecté, le dictionnaire est invalide
        
        # L'ordre a été rempli de la fin vers le début, on l'inverse et on en fait un string
        ordering.reverse()
        return "".join(ordering)