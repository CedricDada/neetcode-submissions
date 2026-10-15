class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0

        for num in nums:
            if res == 0:
                res = num
            else:
                res = res ^ num
        return res