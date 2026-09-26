class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)

        curMin, curMax = 1,1

        for i in range(len(nums)):
            if nums[i] == 0:
                curMin, curMax = 1,1
                continue
            tmp = curMax * nums[i]
            curMax = max(curMax * nums[i], curMin * nums[i], nums[i])
            curMin = min(tmp, curMin * nums[i], nums[i])
            res = max(res, curMax)


        return res