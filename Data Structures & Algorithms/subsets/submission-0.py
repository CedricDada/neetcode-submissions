class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        subsets = []
        
        def dfs(i, path):
            if i > len(nums) - 1:
                subsets.append(path[:])
                return 
            
            # soit je rajoute le noeud i dans le chemin path soit je ne le fais pas
            for take in [True, False]:
                if take:
                    path.append(nums[i])
                    dfs(i+1, path)

                    path.pop()
                else:
                    dfs(i+1, path)


        dfs(0, [])
        return subsets
