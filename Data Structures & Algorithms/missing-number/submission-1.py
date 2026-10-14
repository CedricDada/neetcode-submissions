class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = 0
        for i in range(len(nums)):
            # on est sensé tombé sur la valeur i 
            sum += nums[i]
        n = len(nums)
        return int(n * (n+1)/2 - sum)
        
        