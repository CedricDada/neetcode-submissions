# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         print(nums)
#         if len(nums) == 1:
#             return nums[0]
#         if nums[-1] > nums[0]:
#             print("O(1)")
#             # le tableau n'a pas subi de rotation, faisons 
#             return nums[0]
#         else:
#             c = len(nums)//2

#             # l'un des tableaux [:c] et [c:] n'a pas subi de rotations
#             return min(self.findMin(nums[:c]), self.findMin(nums[c:]))
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # Fonction d'aide récursive qui utilise les index au lieu du slicing
        def search(l: int, r: int) -> int:
            # Cas de base 1 : un seul élément
            if l == r:
                return nums[l]
            
            # Cas de base 2 : ce sous-tableau n'a pas subi de rotation
            if nums[r] > nums[l]:
                return nums[l]
                
            # Sinon, on calcule l'index du milieu
            c = (l + r) // 2
            
            # On explore virtuellement les deux moitiés 
            # nums[:c] devient de 'l' jusqu'à 'c'
            # nums[c:] devient de 'c + 1' jusqu'à 'r'
            return min(search(l, c), search(c + 1, r))
            
        # On lance la recherche sur l'intégralité du tableau
        return search(0, len(nums) - 1)




