import heapq

class MedianFinder:

    def __init__(self):
        # small = Max-Heap (valeurs inversées avec un signe '-') pour la 1re moitié
        # large = Min-Heap (valeurs normales) pour la 2e moitié
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        # 1. On insère d'abord dans 'small' (en inversant le signe pour le Max-Heap)
        heapq.heappush(self.small, -num)

        # 2. On transfère le plus grand de 'small' vers 'large' 
        # pour garantir que tout ce qui est dans 'small' <= tout ce qui est dans 'large'
        val_max_de_small = -heapq.heappop(self.small)
        heapq.heappush(self.large, val_max_de_small)

        # 3. Si 'large' est devenu plus grand que 'small', on rééquilibre
        # (on veut que 'small' ait toujours autant ou 1 élément de plus que 'large')
        if len(self.large) > len(self.small):
            val_min_de_large = heapq.heappop(self.large)
            heapq.heappush(self.small, -val_min_de_large)

    def findMedian(self) -> float:
        # Si le nombre total d'éléments est impair, 'small' a 1 élément de plus :
        # la médiane est simplement son sommet (sans oublier d'inverser le signe '-')
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        
        # Si le total est pair, c'est la moyenne des deux sommets
        return (-self.small[0] + self.large[0]) / 2.0