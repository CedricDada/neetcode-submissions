class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        if len(nums) == 0:
            return [[]]

        subsets = []
        
        def dfs(i, path, target, pathSum):
            if pathSum > target:
                return
            if pathSum == target:
                subsets.append(path[:]) 
                return
            if i > len(nums) - 1:
                return 
            
            
            # soit je rajoute le noeud i dans le chemin path soit je ne le fais pas
            for take in [True, False]:
                if take:
                    path.append(nums[i])
                    pathSum += nums[i]
                    dfs(i, path, target, pathSum)

                    path.pop()
                    pathSum -= nums[i]
                else:
                    dfs(i+1, path, target, pathSum)


        dfs(0, [], target, 0)
        return subsets
