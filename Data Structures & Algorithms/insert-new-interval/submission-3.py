class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        res  = []
        if len(intervals) == 0:
            res.append(newInterval)
            return res
        
        start = 0
        found = False  # <-- AJOUT : On crée un marqueur
        
        for i in range(len(intervals)):
            if newInterval[0] <= intervals[i][1]:
                start = i
                found = True  # <-- AJOUT : On valide qu'on a trouvé où l'insérer
                break
            res.append(intervals[i])
            
        # <-- AJOUT : Si on a parcouru tout le tableau sans "break", 
        # c'est que newInterval va tout à la fin, on l'ajoute et on s'arrête.
        if not found:
            res.append(newInterval)
            return res
            
        # deux cas 
        # premier cas : overlapping entre newInterval et intervals[i]
        if newInterval[0] >= intervals[i][0]:
            res.append([intervals[i][0], max(intervals[i][1], newInterval[1])])
        else:
            res.append(newInterval)
            start = i-1

        last_added_interval = res[-1]

        last_added_interval[1] = max(last_added_interval[1], newInterval[1])

        for i in range(start + 1, len(intervals)):
            # mettons à jour le last de res à chaque fois
            last_added_interval = res[-1]
            current_interval = intervals[i]

            if current_interval[0] <= last_added_interval[1]:
                last_added_interval[1] = max(current_interval[1], last_added_interval[1])
            else:
                res.append(intervals[i])
                
        return res