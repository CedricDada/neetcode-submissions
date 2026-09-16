class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        for i in range(len(nums)):
            if i!=0 :
                prefix[i] = nums[i-1] * prefix[i-1]
        for i in range(len(nums)-1, -1, -1):
            if i!= len(nums)-1:
                suffix[i] = nums[i+1] * suffix[i+1]
        for i in range(len(nums)):
            output[i] = prefix[i] * suffix[i]
        
        return output

