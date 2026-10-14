class Solution:
    def reverseBits(self, n: int) -> int:
        # déterminons la position du 1 le plus à gauche 
        res = 0
        for _ in range(32): #while n ne fonctionne pas ici car quand on n'arrivera pas forcément au 32 bits
            res = res << 1
            res += n & 1
            n = n >> 1
        return res
            