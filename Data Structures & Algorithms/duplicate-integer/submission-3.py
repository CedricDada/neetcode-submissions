class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = {}

        for i, val in enumerate(nums):
            if val not in hash:
                hash[val] = i
            else:
                return True
        return False
                
