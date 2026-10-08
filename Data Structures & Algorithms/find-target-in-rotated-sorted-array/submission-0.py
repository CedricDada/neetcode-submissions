class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if not nums:
            return -1
            
        n = len(nums)
        l, r = 0, n - 1
        
        # 1. Trouver l'index du pivot (le plus petit élément)
        while l < r:
            mid = (l + r) // 2
            # Si le milieu est plus grand que la fin, la chute est à droite
            if nums[mid] > nums[r]:
                l = mid + 1
            # Sinon, la chute est à gauche (ou c'est le milieu)
            else:
                r = mid
                
        pivot = l
        
        # 2. Déterminer dans quelle moitié chercher
        l, r = 0, n - 1
        if pivot > 0 and nums[0] <= target <= nums[pivot - 1]:
            # La cible est dans la partie gauche avant le pivot
            r = pivot - 1
        else:
            # La cible est dans la partie droite à partir du pivot
            l = pivot
            
        # 3. Recherche dichotomique classique sur la bonne portion
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
                
        return -1