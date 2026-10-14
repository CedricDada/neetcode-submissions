class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n!=0:
            res += 1
            n = n & (n-1) # permet de supprimer le 1 le plus à droite
        return res