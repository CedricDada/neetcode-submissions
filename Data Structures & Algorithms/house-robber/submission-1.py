class Solution:
    def rob(self, nums: List[int]) -> int:
        #dp[i] correspond à la somme maximale qu'on peut voler en ne considérant que les i premières maisons
        if len(nums)==1:
            return nums[0]
        dp = [ 0 for _ in range(len(nums)+1)]
        
        dp[1] = nums[0]
        dp[2] = max(nums[0], nums[1])

        for i in range(len(nums)+1) : 
            if i>2:
                dp[i] = max(nums[i-1] + dp[i-2], dp[i-1])
        return dp[len(nums)]

