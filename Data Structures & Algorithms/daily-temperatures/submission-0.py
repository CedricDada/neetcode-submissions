class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        stack = []  # Stockera des tuples (index, temperature)

        for i in range(len(temperatures)-1, -1, -1):
            # 1. On nettoie la pile : on retire toutes les températures 
            # plus froides ou égales à celle du jour actuel.
            while stack and temperatures[i] >= stack[-1][1]:
                stack.pop()
            
            # 2. Si la pile n'est pas vide, le sommet contient le prochain jour plus chaud.
            if stack:
                res[i] = stack[-1][0] - i
            
            # 3. On ajoute le jour actuel à la pile pour les itérations suivantes.
            stack.append((i, temperatures[i]))

        return res