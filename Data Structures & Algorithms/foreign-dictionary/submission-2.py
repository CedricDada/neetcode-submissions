import collections
from typing import List

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        # pour résoudre ce problème il nous suffira de créer un graphe entre les différents caractères, en se basant sur les positions des différents éléments du tableau words
        adj = collections.defaultdict(list)
        for w in words:
            for c in w:
                adj[c] 
        
        # tracons les edges de notre graphe
        for i in range(len(words)-1):
            # on exploite le fait que le mot i < mot i+1 lexicographiquement
            word, next_word = words[i], words[i+1]
            
            # il faut gérer le cas particulier où un mot plus long se trouve avant un de ses préfixes plus courts.
            # par exemple si "apple" est avant "app", ce n'est pas logique dans un dictionnaire, donc on retourne une chaîne vide.
            min_len = min(len(word), len(next_word))
            if len(word) > len(next_word) and word[:min_len] == next_word[:min_len]:
                return ""
            
            # on itère sur les caractères jusqu'à la longueur du mot le plus court
            for j in range(min_len):
                if word[j] != next_word[j]:
                    adj[word[j]].append(next_word[j])
                    # on doit impérativement s'arrêter dès qu'on trouve la première différence entre les deux mots, 
                    # car les caractères suivants ne nous donnent aucune information sur l'ordre lexicographique
                    break 

        # faisons un tri topologique de notre graphe 
        # on va utiliser deux ensembles pour garder une trace de notre parcours et surtout détecter s'il y a un cycle
        visited = set() # pour marquer les noeuds qu'on a fini de traiter complètement
        path = set()    # pour garder les noeuds qui sont dans notre chemin de recherche actuel (utile pour les cycles)
        
        ordering = []
        
        # on définit la fonction dfs avant de l'appeler pour éviter les erreurs de portée en Python
        def dfs(at: str) -> bool:
            # si le noeud sur lequel on arrive est déjà dans notre chemin actuel, cela veut dire qu'on tourne en rond
            # il y a donc un cycle dans le graphe, ce qui rend le dictionnaire invalide
            if at in path:
                return True
            
            # si on tombe sur un noeud qu'on a déjà exploré avec succès dans le passé, on peut s'arrêter là pour ce noeud
            if at in visited:
                return False
                
            # on ajoute le noeud actuel au chemin pour signifier qu'il est en cours d'exploration
            path.add(at)
            
            # on explore tous les voisins de ce noeud
            for neighbor in adj[at]:
                if dfs(neighbor):
                    return True 
            
            # une fois qu'on a fini d'explorer tous les voisins, on peut retirer le noeud de notre chemin actuel
            # et on l'ajoute aux noeuds définitivement visités
            path.remove(at)
            visited.add(at)
            
            # comme on est dans un parcours en profondeur (post-order), on ajoute l'élément à notre liste 
            # et on inversera le tout à la fin
            ordering.append(at)
            return False

        # on lance notre parcours en profondeur sur tous les noeuds de notre graphe
        for at in adj.keys():
            if dfs(at):
                # si la fonction nous retourne True, c'est qu'un cycle a été détecté, on retourne donc une chaîne vide
                return "" 
        
        # l'ordre topologique a été construit à l'envers, on doit donc l'inverser avant de le transformer en chaîne de caractères
        ordering.reverse()
        return "".join(ordering)