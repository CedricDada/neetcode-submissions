from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        # Inutile d'aller jusqu'au bout, on a besoin d'au moins 3 éléments
        for k in range(len(nums) - 2):
            # On ignore les doublons pour le pointeur k
            if k > 0 and nums[k] == nums[k - 1]:
                continue
                
            # On cherche uniquement à droite de k
            l = k + 1
            r = len(nums) - 1
            
            while l < r:
                currentSum = nums[k] + nums[l] + nums[r]
                
                if currentSum < 0:
                    l += 1
                elif currentSum > 0:
                    r -= 1
                else:
                    # On a trouvé un triplet valide
                    res.append([nums[k], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    
                    # On ignore les doublons pour le pointeur l 
                    # (le pointeur r se décalera naturellement au prochain tour de boucle)
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                        
        return res