class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
            
        # 1. Trier les intervalles par leur valeur de début
        intervals.sort(key=lambda x: x[0])
        
        # 2. Initialiser le résultat avec le premier intervalle
        res = [intervals[0]]
        
        for i in range(1, len(intervals)):
            last_added_interval = res[-1]
            current_interval = intervals[i]
            
            # Si le début du courant est <= à la fin du dernier ajouté, il y a chevauchement
            if current_interval[0] <= last_added_interval[1]:
                # On fusionne en mettant à jour la fin du dernier intervalle ajouté
                last_added_interval[1] = max(last_added_interval[1], current_interval[1])
            else:
                # Sinon, on ajoute simplement le nouvel intervalle au résultat
                res.append(current_interval)
                
        return res