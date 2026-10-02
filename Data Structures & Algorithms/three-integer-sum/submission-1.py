from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for k in range(len(nums) - 2):
            # On ignore les doublons pour la valeur fixe k
            if k > 0 and nums[k] == nums[k - 1]:
                continue
                
            l = k + 1
            r = len(nums) - 1
            
            while l < r:
                currentSum = nums[k] + nums[l] + nums[r]
                
                if currentSum < 0:
                    l += 1
                elif currentSum > 0:
                    r -= 1
                else:
                    res.append([nums[k], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    
                    # On ignore les doublons pour le pointeur l
                    # Pourquoi pas r ? Mathématiquement : A + B + C = 0. 
                    # Si A (nums[k]) est fixe, et qu'on force B (nums[l]) à changer 
                    # en sautant ses doublons, C (nums[r]) DOIT forcément changer aussi 
                    # pour que la somme reste 0. Le while principal ajustera r au tour suivant.
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                        
        return res