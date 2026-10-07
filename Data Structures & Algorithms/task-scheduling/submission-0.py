from collections import Counter, deque
from heapq import heapify, heappop, heappush

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        # 1. Compter les fréquences de chaque tâche
        counts = Counter(tasks)
        counts = [-cnt for cnt in counts.values()]

        time = 0
        
        # On transforme la liste en Max-Heap (simulé avec des négatifs)
        heapify(counts)
        heap = counts 

        queue = deque([])

        while heap or queue:
            time += 1
            
            # Si on a des tâches prêtes, on prend la plus fréquente
            if heap:
                cnt = heappop(heap)
                cnt += 1 # on décrémente la quantité restante

                if cnt != 0: 
                    # Il reste des tâches de ce type, on la met en file de refroidissement
                    queue.append((cnt, time + n))
            
            # Vérifier si la tâche en tête de file a fini de refroidir
            if queue:
                freq, t = queue[0]
                if t == time:
                    queue.popleft()
                    heappush(heap, freq)

        return time